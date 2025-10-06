import tp_jour_3 as m
import runpy
import pytest


def test_demo_sous_classe_runs(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    if hasattr(m, "demo_sous_classe"):
        m.demo_sous_classe()
        assert (tmp_path / "catalogue2.json").exists()
        assert (tmp_path / "catalogue2.csv").exists()
    else:
        b = m.BibliothequeAvecFichier("Test")
        b.ajouter_livre(m.Livre("Titre test", "Auteur test", "000"))

        j = tmp_path / "catalogue2.json"
        c = tmp_path / "catalogue2.csv"

        b.save_json(str(j))
        b.export_csv(str(c))
        assert j.exists() and c.exists()

        b2 = m.BibliothequeAvecFichier.load_json(str(j))
        assert isinstance(b2, m.BibliothequeAvecFichier)
        assert b2.nom == "Test" and len(b2.livres) == 1


def test_demo_safe_wrappers_runs(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    if hasattr(m, "demo_safe_wrappers"):
        m.biblio = m.Bibliotheque("Demo")
        m.biblio.ajouter_livre(m.Livre("A", "B", "1"))
        m.demo_safe_wrappers()
        assert (tmp_path / "catalogue.json").exists()
        assert (tmp_path / "catalogue.csv").exists()
    else:
        b = m.Bibliotheque("Demo")
        b.ajouter_livre(m.Livre("A", "B", "1"))
        m.save_biblio_json_safe(b, "catalogue.json")
        _ = m.load_biblio_json_safe("catalogue.json")
        m.export_biblio_csv_safe(b, "catalogue.csv")
        assert (tmp_path / "catalogue.json").exists()
        assert (tmp_path / "catalogue.csv").exists()


def test_run_module_main(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    runpy.run_module("tp_jour_3", run_name="__main__")

    assert True
