from tp_jour_3 import Livre, LivreNumerique, Bibliotheque


def test_creation_bibliotheque(biblio):
    assert biblio.nom == "Test"
    assert biblio.livres == []  # vide au départ


def test_ajout_livre(biblio, livre):
    biblio.ajouter_livre(livre)
    assert len(biblio.livres) == 1
    assert biblio.livres[0] is livre


def test_supprimer_livre():
    b = Bibliotheque("X")
    l1 = Livre("A", "B", "111")
    l2 = Livre("C", "D", "222")
    b.ajouter_livre(l1)
    b.ajouter_livre(l2)
    b.supprimer_livre("111")
    assert len(b.livres) == 1
    assert b.livres[0].isbn == "222"


def test_rechercher_par_titre():
    b = Bibliotheque("X")
    b.ajouter_livre(Livre("Le Petit Prince", "Exupéry", "1"))
    b.ajouter_livre(Livre("Harry Potter", "Rowling", "2"))
    r = b.rechercher_par_titre("petit")
    assert len(r) == 1
    assert r[0].titre == "Le Petit Prince"


def test_rechercher_par_auteur():
    b = Bibliotheque("X")
    b.ajouter_livre(Livre("1984", "George Orwell", "1"))
    b.ajouter_livre(LivreNumerique("Autre", "Quelqu'un", "2", 1.0))
    r = b.rechercher_par_auteur("orwell")
    assert len(r) == 1
    assert r[0].auteur == "George Orwell"


def test_strs():
    l = Livre("Titre", "Auteur", "XYZ")
    e = LivreNumerique("Ebook", "AA", "123", 2.5)
    b = Bibliotheque("B1")
    b.ajouter_livre(l)
    assert "Titre" in str(l) and "XYZ" in str(l)
    assert "Ebook" in str(e) and "2.5" in str(e)
    assert "1 livre(s)" in str(b) and "B1" in str(b)
