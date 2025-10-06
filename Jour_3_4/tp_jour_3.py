import json
import csv


class Livre:
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titre}' écrit par {self.auteur} (ISBN: {self.isbn})"


class LivreNumerique(Livre):
    def __init__(self, titre: str, auteur: str, isbn: str, taille_fichier: float):
        super().__init__(titre, auteur, isbn)
        self.taille_fichier = taille_fichier

    def __str__(self):
        return (
            f"'{self.titre}' écrit par {self.auteur} "
            f"(ISBN: {self.isbn}, fichier : {self.taille_fichier} Mo)"
        )


class Bibliotheque:
    def __init__(self, nom: str):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

    def supprimer_livre(self, isbn: str):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]

    def rechercher_par_titre(self, titre: str):
        return [livre for livre in self.livres if titre.lower() in livre.titre.lower()]

    def rechercher_par_auteur(self, auteur: str):
        return [
            livre for livre in self.livres if auteur.lower() in livre.auteur.lower()
        ]

    def __str__(self):
        return f"Bibliothèque '{self.nom}' avec {len(self.livres)} livre(s)."


if __name__ == "__main__":
    biblio = Bibliotheque("Municipale")

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


# Tp Jour 2
def encode_livre(livre: Livre) -> dict:
    d = {
        "type": livre.__class__.__name__,
        "titre": livre.titre,
        "auteur": livre.auteur,
        "isbn": livre.isbn,
    }
    if isinstance(livre, LivreNumerique):
        d["taille_fichier"] = livre.taille_fichier
    return d


def biblio_to_dict(biblio: Bibliotheque) -> dict:
    return {
        "nom": biblio.nom,
        "livres": [encode_livre(l) for l in biblio.livres],
    }


def dict_to_biblio(data: dict) -> Bibliotheque:
    b = Bibliotheque(data.get("nom", "SansNom"))
    for item in data.get("livres", []):
        typ = item.get("type", "Livre")
        if typ == "LivreNumerique":
            l = LivreNumerique(
                item["titre"],
                item["auteur"],
                item["isbn"],
                item.get("taille_fichier", 0.0),
            )
        else:
            l = Livre(item["titre"], item["auteur"], item["isbn"])
        b.ajouter_livre(l)
    return b


def save_biblio_json(biblio: Bibliotheque, path: str = "catalogue.json") -> None:
    data = biblio_to_dict(biblio)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_biblio_json(path: str = "catalogue.json") -> Bibliotheque:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return dict_to_biblio(data)


def export_biblio_csv(biblio: Bibliotheque, path: str = "catalogue.csv") -> None:
    fieldnames = ["type", "titre", "auteur", "isbn", "taille_fichier"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for l in biblio.livres:
            row = {
                "type": l.__class__.__name__,
                "titre": l.titre,
                "auteur": l.auteur,
                "isbn": l.isbn,
                "taille_fichier": getattr(l, "taille_fichier", ""),
            }
            writer.writerow(row)


if __name__ == "__main__":
    try:
        save_biblio_json(biblio, "catalogue.json")
        print("Sauvegarde JSON : catalogue.json")
    except (OSError, TypeError, ValueError) as e:
        print("Erreur lors de la sauvegarde JSON :", e)

    try:
        b2 = load_biblio_json("catalogue.json")
        print("Chargement JSON OK :", b2)
    except FileNotFoundError:
        print("Fichier JSON introuvable (catalogue.json).")
    except (OSError, json.JSONDecodeError) as e:
        print("Erreur de lecture/décodage JSON :", e)

    try:
        export_biblio_csv(biblio, "catalogue.csv")
        print("Export CSV : catalogue.csv")
    except OSError as e:
        print("Erreur lors de l'export CSV :", e)

    try:
        _ = load_biblio_json("fichier_qui_n_existe_pas.json")
    except FileNotFoundError:
        print("Exemple : fichier JSON manquant bien intercepté.")


class ErreurBibliotheque(Exception):
    pass


class ErreurFichierBibliotheque(ErreurBibliotheque):
    pass


class ErreurChargementJSON(ErreurBibliotheque):
    pass


class ErreurSauvegardeJSON(ErreurBibliotheque):
    pass


class ErreurExportCSV(ErreurBibliotheque):
    pass


def save_biblio_json_safe(biblio, path="catalogue.json"):
    try:
        save_biblio_json(biblio, path)
    except (OSError, TypeError, ValueError) as e:
        raise ErreurSauvegardeJSON(
            "Erreur lors de la sauvegarde JSON '{}': {}".format(path, e)
        ) from e


def load_biblio_json_safe(path="catalogue.json"):
    try:
        return load_biblio_json(path)
    except FileNotFoundError as e:
        raise ErreurFichierBibliotheque(
            "Fichier JSON introuvable: '{}'".format(path)
        ) from e
    except json.JSONDecodeError as e:
        raise ErreurChargementJSON("JSON invalide dans '{}': {}".format(path, e)) from e
    except OSError as e:
        raise ErreurFichierBibliotheque(
            "Erreur d'accès au fichier '{}': {}".format(path, e)
        ) from e


def export_biblio_csv_safe(biblio, path="catalogue.csv"):
    try:
        export_biblio_csv(biblio, path)
    except OSError as e:
        raise ErreurExportCSV(
            "Erreur lors de l'export CSV '{}': {}".format(path, e)
        ) from e


class BibliothequeAvecFichier(Bibliotheque):
    def save_json(self, path="catalogue.json"):
        save_biblio_json_safe(self, path)

    @classmethod
    def load_json(cls, path="catalogue.json"):
        b = load_biblio_json_safe(path)
        nb = cls(b.nom)
        for l in b.livres:
            nb.ajouter_livre(l)
        return nb

    def export_csv(self, path="catalogue.csv"):
        export_biblio_csv_safe(self, path)


def demo_safe_wrappers():
    print("\n-DEMO: wrappers *_safe")
    try:
        save_biblio_json_safe(biblio, "catalogue.json")
        print("OK sauvegarde (safe) -> catalogue.json")
    except ErreurSauvegardeJSON as e:
        print("Erreur (safe save):", e)

    try:
        b2 = load_biblio_json_safe("catalogue.json")
        print("OK chargement (safe):", b2)
    except ErreurFichierBibliotheque as e:
        print("Fichier introuvable (safe load):", e)
    except ErreurChargementJSON as e:
        print("JSON invalide (safe load):", e)

    try:
        export_biblio_csv_safe(biblio, "catalogue.csv")
        print("OK export CSV (safe) -> catalogue.csv")
    except ErreurExportCSV as e:
        print("Erreur CSV (safe export):", e)

    try:
        _ = load_biblio_json_safe("fichier_qui_n_existe_pas.json")
    except ErreurFichierBibliotheque as e:
        print("Fichier manquant bien intercepté (safe load):", e)


if __name__ == "__main__":

    def demo_sous_classe():
        print("\n--- DEMO: sous-classe BibliothequeAvecFichier ---")

    b = BibliothequeAvecFichier("Test")
    b.ajouter_livre(Livre("Titre test", "Auteur test", "000"))
    try:
        b.save_json("catalogue2.json")
        print("OK save via méthode -> catalogue2.json")
    except ErreurSauvegardeJSON as e:
        print("Erreur save (méthode):", e)

    try:
        b3 = BibliothequeAvecFichier.load_json("catalogue2.json")
        print("OK load via classe:", b3)
    except ErreurFichierBibliotheque as e:
        print("Fichier introuvable (méthode load):", e)
    except ErreurChargementJSON as e:
        print("JSON invalide (méthode load):", e)

    try:
        b.export_csv("catalogue2.csv")
        print("OK export CSV via méthode -> catalogue2.csv")
    except ErreurExportCSV as e:
        print("Erreur export CSV (méthode):", e)


if __name__ == "__main__":
    demo_safe_wrappers()
    demo_sous_classe()
