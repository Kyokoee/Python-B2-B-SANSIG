from models import Livre, LivreNumerique
from file_manager import BibliothequeAvecFichier
from exceptions import (
    ErreurFichierBibliotheque,
    ErreurChargementJSON,
    ErreurSauvegardeJSON,
    ErreurExportCSV,
)


def main():
    biblio = BibliothequeAvecFichier("Municipale")

    livre1 = Livre("Le problème à 3 corps", "Liu Cixin", "978-0765377067")
    ebook = LivreNumerique("1984", "George Orwell", "978-0451524935", 2.5)
    livre2 = Livre("Le petit prince", "Antoine de St-Exupery", "978-0156013987")
    livre3 = Livre("Harry potter", "Jk Rowling", "978-156013987")
    livre4 = Livre("jsp", "brother", "978-015601987")
    livre5 = Livre("monte cristo", "je sais pas", "978-056013987")

    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(ebook)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_livre(livre3)
    biblio.ajouter_livre(livre4)
    biblio.ajouter_livre(livre5)

    print(biblio)

    print("Recherche par titre '1984':")
    for livre in biblio.rechercher_par_titre("1984"):
        print(" ", livre)

    print("Recherche par auteur 'Liu Cixin':")
    for livre in biblio.rechercher_par_auteur("Liu Cixin"):
        print(" ", livre)

    biblio.supprimer_livre("978-0156013987")
    print("Le livre a bien été supprimé")
    print(biblio)

    try:
        biblio.save_json("catalogue.json")
        print("Sauvegarde JSON : catalogue.json")
    except ErreurSauvegardeJSON as e:
        print("Erreur lors de la sauvegarde JSON :", e)

    try:
        b2 = BibliothequeAvecFichier.load_json("catalogue.json")
        print("Chargement JSON OK :", b2)
    except (ErreurFichierBibliotheque, ErreurChargementJSON) as e:
        print("Erreur au chargement JSON :", e)

    try:
        biblio.export_csv("catalogue.csv")
        print("Export CSV : catalogue.csv")
    except ErreurExportCSV as e:
        print("Erreur lors de l'export CSV :", e)


if __name__ == "__main__":
    main()
