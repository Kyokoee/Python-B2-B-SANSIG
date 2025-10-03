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
        pass

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

biblio.ajouter_livre(livre1)
biblio.ajouter_livre(ebook)
biblio.ajouter_livre(livre2)

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
