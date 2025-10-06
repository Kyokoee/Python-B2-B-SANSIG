class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return "'{}' écrit par {} (ISBN: {})".format(self.titre, self.auteur, self.isbn)


class LivreNumerique(Livre):
    def __init__(self, titre, auteur, isbn, taille_fichier):
        super().__init__(titre, auteur, isbn)
        self.taille_fichier = taille_fichier

    def __str__(self):
        return "'{}' écrit par {} (ISBN: {}, fichier : {} Mo)".format(
            self.titre, self.auteur, self.isbn, self.taille_fichier
        )


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, isbn):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]

    def rechercher_par_titre(self, titre):
        return [livre for livre in self.livres if titre.lower() in livre.titre.lower()]

    def rechercher_par_auteur(self, auteur):
        return [
            livre for livre in self.livres if auteur.lower() in livre.auteur.lower()
        ]

    def __str__(self):
        return "Bibliothèque '{}' avec {} livre(s).".format(self.nom, len(self.livres))
