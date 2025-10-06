import json
import csv
import pytest

from tp_jour_3 import (
    Livre,
    LivreNumerique,
    Bibliotheque,
    save_biblio_json,
    load_biblio_json,
    load_biblio_json_safe,
    export_biblio_csv,
    save_biblio_json_safe,
    export_biblio_csv_safe,
    ErreurFichierBibliotheque,
    ErreurChargementJSON,
    ErreurSauvegardeJSON,
    ErreurExportCSV,
    encode_livre,
    biblio_to_dict,
    dict_to_biblio,
    save_biblio_json_safe,
    load_biblio_json_safe,
    export_biblio_csv_safe,
)


def test_json_save_load(tmp_path):
    b = Bibliotheque("TestIO")
    b.ajouter_livre(Livre("Le petit prince", "Antoine de St-Exupery", "978-0156013987"))
    b.ajouter_livre(LivreNumerique("1984", "George Orwell", "978-0451524935", 2.5))

    p = tmp_path / "cat.json"
    save_biblio_json(b, str(p))

    assert p.exists()

    data = json.loads(p.read_text(encoding="utf-8"))
    assert data["nom"] == "TestIO"
    assert len(data["livres"]) == 2

    b2 = load_biblio_json(str(p))
    assert isinstance(b2, Bibliotheque)
    assert b2.nom == "TestIO"
    assert len(b2.livres) == 2


def test_load_json_safe_fichier_manquant(tmp_path):
    p = tmp_path / "nope.json"
    with pytest.raises(ErreurFichierBibliotheque):
        load_biblio_json_safe(str(p))


def test_export_csv(tmp_path):
    b = Bibliotheque("TestCSV")
    b.ajouter_livre(Livre("A", "B", "111"))
    b.ajouter_livre(LivreNumerique("C", "D", "222", 3.0))

    p = tmp_path / "cat.csv"
    export_biblio_csv(b, str(p))

    assert p.exists()

    with p.open("r", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        rows = list(r)
        assert len(rows) == 2
        assert any(row.get("type") == "LivreNumerique" for row in rows)


def test_load_json_safe_json_invalide(tmp_path):
    p = tmp_path / "mauvais.json"
    p.write_text("pas du json", encoding="utf-8")
    with pytest.raises(ErreurChargementJSON):
        load_biblio_json_safe(str(p))


def test_safe_wrappers_erreurs_sur_repertoires(tmp_path):
    b = Bibliotheque("X")
    with pytest.raises(ErreurSauvegardeJSON):
        save_biblio_json_safe(b, str(tmp_path))

    with pytest.raises(ErreurExportCSV):
        export_biblio_csv_safe(b, str(tmp_path))


def test_roundtrip_dict():
    b = Bibliotheque("DictIO")
    b.ajouter_livre(Livre("A", "B", "1"))
    b.ajouter_livre(LivreNumerique("C", "D", "2", 1.2))
    d = biblio_to_dict(b)
    assert d["nom"] == "DictIO" and len(d["livres"]) == 2
    assert "type" in encode_livre(b.livres[0])
    b2 = dict_to_biblio(d)
    assert isinstance(b2, Bibliotheque) and len(b2.livres) == 2


def test_json_safe_ok(tmp_path):
    b = Bibliotheque("SafeOK")
    b.ajouter_livre(Livre("X", "Y", "9"))
    p = tmp_path / "ok.json"
    save_biblio_json_safe(b, str(p))  # ne doit pas lever
    b2 = load_biblio_json_safe(str(p))  # ne doit pas lever
    assert b2.nom == "SafeOK" and len(b2.livres) == 1


def test_csv_safe_ok(tmp_path):
    b = Bibliotheque("CSVOK")
    b.ajouter_livre(Livre("A", "B", "1"))
    p = tmp_path / "ok.csv"
    export_biblio_csv_safe(b, str(p))  # ne doit pas lever
    assert p.exists() and p.read_text(encoding="utf-8").strip() != ""
