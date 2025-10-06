import os
import tempfile
from models import Livre, LivreNumerique
from file_manager import BibliothequeAvecFichier
from exceptions import ErreurFichierBibliotheque


def ok(msg):
    print("ok", msg)


def ko(msg):
    print("pas ok", msg)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        json_path = os.path.join(tmp, "catalogue.json")
        csv_path = os.path.join(tmp, "catalogue.csv")

        b = BibliothequeAvecFichier("Test")
        b.ajouter_livre(Livre("A", "B", "1"))
        b.ajouter_livre(LivreNumerique("Ebook", "C", "2", 1.2))

        b.save_json(json_path)
        assert os.path.exists(json_path)
        ok("save_json a créé le fichier JSON")

        b2 = BibliothequeAvecFichier.load_json(json_path)
        assert b2.nom == "Test"
        assert len(b2.livres) == 2
        assert isinstance(b2.livres[1], LivreNumerique)
        ok("load_json a reconstruit la bibliothèque correctement")

        b.export_csv(csv_path)
        assert os.path.exists(csv_path)
        first_line = open(csv_path, encoding="utf-8").readline().strip()
        assert first_line == "type,titre,auteur,isbn,taille_fichier"
        ok("export_csv a créé le CSV avec l'entête attendu")

        try:
            BibliothequeAvecFichier.load_json(os.path.join(tmp, "absent.json"))
            ko("load_json aurait dû lever ErreurFichierBibliotheque")
        except ErreurFichierBibliotheque:
            ok("load_json lève ErreurFichierBibliotheque quand le fichier manque")


if __name__ == "__main__":
    main()
