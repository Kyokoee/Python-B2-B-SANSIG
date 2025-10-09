from tp_jour_3 import Livre, LivreNumerique, Bibliotheque
import tp_jour_3 as tp


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


def test_bibliotheque_str_vide_et_apres_ajout():
    b = tp.Bibliotheque("Mediatek")
    txt0 = str(b)
    assert "Mediatek" in txt0

    b.ajouter_livre(tp.Livre("T", "A", "I1"))
    txt1 = str(b)
    assert "Mediatek" in txt1 and "1" in txt1


def test_recherche_insensible_a_la_casse_et_partielle():
    b = tp.Bibliotheque("B")
    b.ajouter_livre(tp.Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "P1"))
    r1 = b.rechercher_par_titre("petit")
    r2 = b.rechercher_par_titre("PETIT")
    assert len(r1) == 1 and len(r2) == 1

    r3 = b.rechercher_par_auteur("exup")
    r4 = b.rechercher_par_auteur("EXUP")
    assert len(r3) == 1 and len(r4) == 1


def test_str_livre_et_eventuel_livre_numerique():
    l = tp.Livre("Titre", "Auteur", "XYZ")
    s = str(l)
    assert "Titre" in s and "XYZ" in s

    if hasattr(tp, "LivreNumerique"):
        e = tp.LivreNumerique("Ebook", "AA", "123", 2.5)
        s2 = str(e)
        assert "Ebook" in s2 and "2.5" in s2


def test_retira_sans_casser_selon_nom_de_methode():
    """On couvre la branche de retrait, quel que soit le nom (retirer_livre ou supprimer_livre)."""
    b = tp.Bibliotheque("B")
    b.ajouter_livre(tp.Livre("T", "A", "I1"))

    if hasattr(b, "retirer_livre"):
        b.retirer_livre("I1")  # retrait normal
        # retrait d'un ISBN inexistant : on n'exige PAS d'exception (selon ton implémentation)
        try:
            b.retirer_livre("I1")
        except Exception:
            pass
    elif hasattr(b, "supprimer_livre"):
        b.supprimer_livre("I1")
        try:
            b.supprimer_livre("I1")
        except Exception:
            pass


import tp_jour_3 as tp


def test_bibliotheque_str_vide_et_apres_ajout():
    b = tp.Bibliotheque("Mediatek")
    txt0 = str(b)
    assert "Mediatek" in txt0
    b.ajouter_livre(tp.Livre("T", "A", "I1"))
    txt1 = str(b)
    assert "Mediatek" in txt1 and "1" in txt1


def test_recherche_insensible_a_la_casse_et_partielle():
    b = tp.Bibliotheque("B")
    b.ajouter_livre(tp.Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "P1"))
    r1 = b.rechercher_par_titre("petit")
    r2 = b.rechercher_par_titre("PETIT")
    assert len(r1) == 1 and len(r2) == 1

    r3 = b.rechercher_par_auteur("exup")
    r4 = b.rechercher_par_auteur("EXUP")
    assert len(r3) == 1 and len(r4) == 1


def test_str_livre_et_eventuel_livre_numerique():
    l = tp.Livre("Titre", "Auteur", "XYZ")
    s = str(l)
    assert "Titre" in s and "XYZ" in s
    if hasattr(tp, "LivreNumerique"):
        e = tp.LivreNumerique("Ebook", "AA", "123", 2.5)
        s2 = str(e)
        assert "Ebook" in s2 and "2.5" in s2


def test_retrait_deux_fois_sans_planter():
    b = tp.Bibliotheque("B")
    b.ajouter_livre(tp.Livre("T", "A", "I1"))
    if hasattr(b, "retirer_livre"):
        b.retirer_livre("I1")
        try:
            b.retirer_livre("I1")
        except Exception:
            pass
    elif hasattr(b, "supprimer_livre"):
        b.supprimer_livre("I1")
        try:
            b.supprimer_livre("I1")
        except Exception:
            pass
