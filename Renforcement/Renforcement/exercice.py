"""
🎯 PYTHON EXERCICES COMPLET - VARIABLES, SCOPES, FONCTIONS & POO
Niveau : Débutant à Intermédiaire
Objectif : Maîtriser les concepts fondamentaux de Python
"""

# =============================================================================
# PARTIE 1 : VARIABLES ET SCOPES
# =============================================================================

print("=" * 60)
print("PARTIE 1 : VARIABLES ET SCOPES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercice 1.1 : Comprendre les types de variables
# -----------------------------------------------------------------------------


def exercice_1_1():
    """
    Créez des variables de différents types et affichez leurs types
    """
    print("\n--- Exercice 1.1 : Types de variables ---")

    prenom = "Clément"
    age = 22
    taille = 1.80
    aime_python = False
    hobbies = ["Cinéma", "Jeux videos", "musique"]
    infos = {"nom": "Sansig", "ville": "Bordeaux"}

    print(f"prenom: {prenom} (type: {type(prenom)})")
    print(f"age: {age} (type: {type(age)})")
    print(f"taille: {taille} (type: {type(taille)})")
    print(f"aime_python: {aime_python} (type: {type(aime_python)})")
    print(f"hobbies: {hobbies} (type: {type(hobbies)})")
    print(f"infos: {infos} (type: {type(infos)})")


# -----------------------------------------------------------------------------
# Exercice 1.2 : Portée des variables (scope)
# -----------------------------------------------------------------------------

variable_globale = "Je suis globale"


def exercice_1_2():
    """
    Comprenez la différence entre variables globales et locales
    """
    print("\n--- Exercice 1.2 : Portée des variables ---")

    variable_locale = "Je suis locale"

    # TODO: Essayez de modifier la variable globale (sans global)
    # variable_globale = "Modifiée sans global"  # Que se passe-t-il ?

    # TODO: Utilisez 'global' pour modifier la variable globale
    global variable_globale
    variable_globale = "Modifiée avec global"

    print(f"Variable globale modifiée: {variable_globale}")


def test_scope():
    """Testez la portée des variables"""
    print("\nTest de portée:")
    print(f"Variable globale avant fonction: {variable_globale}")
    exercice_1_2()
    print(f"Variable globale après fonction: {variable_globale}")
    # print(f"Essai d'accès à variable_locale: {variable_locale}")  # ❌ Erreur !


# -----------------------------------------------------------------------------
# Exercice 1.3 : Réaffectation et mutation
# -----------------------------------------------------------------------------


def exercice_1_3():
    """
    Comprenez la différence entre réaffectation et mutation
    """
    print("\n--- Exercice 1.3 : Réaffectation vs Mutation ---")

    # Variables immuables (réaffectation)
    a = 10
    b = a  # b pointe vers la même valeur que a
    a = 20  # Réaffectation : a pointe vers une nouvelle valeur

    print(f"a = {a}, b = {b}")  # a change, b reste inchangé

    # Variables muables (mutation)
    liste1 = [1, 2, 3]
    liste2 = liste1  # liste2 pointe vers le même objet que liste1
    liste1.append(4)  # Mutation : l'objet est modifié

    print(f"liste1 = {liste1}, liste2 = {liste2}")  # Les deux changent !

    # TODO: Créez une copie indépendante de liste1
    liste3 = liste1.copy()  # ou liste1[:]
    liste1.append(5)
    print(f"liste1 = {liste1}, liste3 = {liste3}")  # Seule liste1 change


# -----------------------------------------------------------------------------
# Exercice 1.4 : Constantes et conventions
# -----------------------------------------------------------------------------


def exercice_1_4():
    """
    Utilisez les conventions de nommage Python
    """
    print("\n--- Exercice 1.4 : Conventions de nommage ---")

    # Convention pour les constantes (MAJUSCULES)
    TAUX_TVA = 0.20
    PI = 3.14159
    NOMBRE_MAX_UTILISATEURS = 100

    # Convention pour les variables (snake_case)
    nom_utilisateur = "alice_dupont"
    age_utilisateur = 25
    est_connecte = True

    # Convention pour les fonctions (snake_case)
    def calculer_prix_ttc(prix_ht):
        return prix_ht * (1 + TAUX_TVA)

    # TODO: Créez des variables respectant les conventions
    # Ville par defaut (str)
    # nombre de tentatives (int)

    prix = 100
    prix_ttc = calculer_prix_ttc(prix)
    print(f"Prix HT: {prix}€, Prix TTC: {prix_ttc:.2f}€")


# -----------------------------------------------------------------------------
# TEST PARTIE 1
# -----------------------------------------------------------------------------


def tester_partie_1():
    """Testez tous les exercices de la partie 1"""
    exercice_1_1()
    test_scope()
    exercice_1_3()
    exercice_1_4()


# Décommentez pour tester
# tester_partie_1()

# =============================================================================
# PARTIE 2 : FONCTIONS - BASES
# =============================================================================

print("\n" + "=" * 60)
print("PARTIE 2 : FONCTIONS - BASES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercice 2.1 : Fonctions simples sans paramètres
# -----------------------------------------------------------------------------


def exercice_2_1():
    """
    Créez des fonctions simples sans paramètres
    """
    print("\n--- Exercice 2.1 : Fonctions sans paramètres ---")

    # TODO: Créez une fonction qui affiche "Bonjour !"

    def dire_bonjour():
        print("Bonjour !")

    # TODO: Créez une fonction qui retourne le nombre 42
    def donner_quarante_deux(donner_quarante_deux):
        print("42")

    # TODO: Créez une fonction qui affiche l'heure actuelle
    def heure():
        print()

    # TODO: Testez vos fonctions, décommenter
    # dire_bonjour()
    # resultat = donner_quarante_deux()
    # print(f"La fonction a retourné: {resultat}")
    # afficher_heure()


# -----------------------------------------------------------------------------
# Exercice 2.2 : Fonctions avec paramètres
# -----------------------------------------------------------------------------


def exercice_2_2():
    """
    Créez des fonctions avec paramètres
    """
    print("\n--- Exercice 2.2 : Fonctions avec paramètres ---")

    # TODO: Créez une fonction qui prend un nom et dit bonjour

    # TODO: Créez une fonction qui prend deux nombres et retourne leur somme

    # TODO: Créez une fonction qui prend une liste et retourne sa longueur

    # TODO: Testez vos fonctions, décommenter
    # saluer("Alice")
    # somme = additionner(5, 3)
    # print(f"5 + 3 = {somme}")

    # ma_liste = [1, 2, 3, 4, 5]
    # longueur = longueur_liste(ma_liste)
    # print(f"La liste {ma_liste} a {longueur} éléments")


# -----------------------------------------------------------------------------
# Exercice 2.3 : Fonctions avec valeurs de retour
# -----------------------------------------------------------------------------


def exercice_2_3():
    """
    Travaillez avec les valeurs de retour
    """
    print("\n--- Exercice 2.3 : Valeurs de retour ---")

    # TODO: Créez une fonction qui calcule la surface d'un rectangle

    # TODO: Créez une fonction qui vérifie si un nombre est pair

    # TODO: Créez une fonction qui retourne le plus grand de deux nombres

    # TODO: Créez une fonction qui retourne multiple valeurs

    # TODO: Testez vos fonctions, décommenter
    # surface = surface_rectangle(5, 3)
    # print(f"Surface du rectangle: {surface}")

    # print(f"4 est pair: {est_pair(4)}")
    # print(f"5 est pair: {est_pair(5)}")

    # max_nombre = maximum(10, 15)
    # print(f"Le maximum entre 10 et 15 est: {max_nombre}")

    # s, d, p, q = operations_completes(10, 2)
    # print(f"10 et 2 → Somme: {s}, Différence: {d}, Produit: {p}, Quotient: {q}")


# -----------------------------------------------------------------------------
# TEST PARTIE 2
# -----------------------------------------------------------------------------


def tester_partie_2():
    """Testez tous les exercices de la partie 2"""
    exercice_2_1()
    exercice_2_2()
    exercice_2_3()


# Décommentez pour tester
# tester_partie_2()

# =============================================================================
# PARTIE 3 : FONCTIONS - PARAMÈTRES AVANCÉS
# =============================================================================

print("\n" + "=" * 60)
print("PARTIE 3 : FONCTIONS - PARAMÈTRES AVANCÉS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercice 3.1 : Paramètres avec valeurs par défaut
# -----------------------------------------------------------------------------


def exercice_3_1():
    """
    Utilisez des paramètres avec valeurs par défaut
    """
    print("\n--- Exercice 3.1 : Paramètres par défaut ---")

    # TODO: Créez une fonction avec des paramètres optionnels

    # TODO: Créez une fonction de salutation personnalisable

    # Testez avec différentes combinaisons, décommenter
    # decrire_animal("Rex")  # Utilise les valeurs par défaut
    # decrire_animal("Félix", "chat")  # Spécifie l'espèce
    # decrire_animal("Tweety", "oiseau", 2)  # Spécifie tout
    # decrire_animal("Médor", age=3)  # Spécifie seulement l'âge

    # saluer("Alice")
    # saluer("Bob", "Salut")
    # saluer("Charlie", "Bonsoir", ".")


# -----------------------------------------------------------------------------
# Exercice 3.2 : Paramètres nommés (keyword arguments)
# -----------------------------------------------------------------------------


def exercice_3_2():
    """
    Utilisez les paramètres nommés
    """
    print("\n--- Exercice 3.2 : Paramètres nommés ---")

    # TODO: Créez une fonction avec plusieurs paramètres

    # TODO: Testez avec des paramètres nommés, décommenter
    # profil1 = creer_profil("Alice", 25, "Paris")
    # profil2 = creer_profil(age=30, nom="Bob", ville="Lyon", profession="ingénieur")
    # profil3 = creer_profil("Charlie", 22, "Marseille", hobbies=["sport", "lecture"])

    # print("Profil 1:", profil1)
    # print("Profil 2:", profil2)
    # print("Profil 3:", profil3)

    # TODO: Que se passe-t-il si vous mélangez positionnel et nommé ?
    # profil4 = creer_profil("David", age=28, "Toulouse")  # ❌ Erreur !
    # profil4 = creer_profil("David", 28, "Toulouse")  # ✅ Correct


# -----------------------------------------------------------------------------
# Exercice 3.3 : Nombre variable d'arguments
# -----------------------------------------------------------------------------


def exercice_3_3():
    """
    Utilisez *args et **kwargs
    """
    print("\n--- Exercice 3.3 : Arguments variables ---")

    # TODO: Créez une fonction qui accepte un nombre variable d'arguments

    # TODO: Créez une fonction qui crée un dictionnaire à partir de kwargs

    # TODO: Testez vos fonctions, décommenter
    # resultat1 = additionner_tout(1, 2, 3)
    # resultat2 = additionner_tout(10, 20, 30, 40, 50)
    # print(f"Somme 1: {resultat1}")
    # print(f"Somme 2: {resultat2}")

    # config1 = creer_configuration()
    # config2 = creer_configuration(theme="sombre", notifications=False)
    # config3 = creer_configuration(langue="en", son=True, vitesse=2)

    # print("Config 1:", config1)
    # print("Config 2:", config2)
    # print("Config 3:", config3)


# -----------------------------------------------------------------------------
# Exercice 3.4 : Fonctions comme paramètres
# -----------------------------------------------------------------------------


def exercice_3_4():
    """
    Passez des fonctions en paramètres
    """
    print("\n--- Exercice 3.4 : Fonctions comme paramètres ---")

    # Fonctions utilitaires
    def doubler(x):
        return x * 2

    def carre(x):
        return x**2

    def est_pair(x):
        return x % 2 == 0

    # TODO: Créez une fonction qui applique une fonction à tous les éléments d'une liste
    def appliquer_fonction(liste, fonction):
        """TODO"""
        return

    # TODO: Créez une fonction qui filtre une liste selon une condition
    def filtrer_liste(liste, condition):
        """TODO"""
        return

    # TODO: Testez vos fonctions, décommenter
    # nombres = [1, 2, 3, 4, 5]

    # doubles = appliquer_fonction(nombres, doubler)
    # carres = appliquer_fonction(nombres, carre)
    # pairs = filtrer_liste(nombres, est_pair)

    # print(f"Nombres: {nombres}")
    # print(f"Doubles: {doubles}")
    # print(f"Carrés: {carres}")
    # print(f"Pairs: {pairs}")


# -----------------------------------------------------------------------------
# TEST PARTIE 3
# -----------------------------------------------------------------------------


def tester_partie_3():
    """Testez tous les exercices de la partie 3"""
    exercice_3_1()
    exercice_3_2()
    exercice_3_3()
    exercice_3_4()


# Décommentez pour tester
# tester_partie_3()

# =============================================================================
# PARTIE 4 : FONCTIONS - CONCEPTS AVANCÉS
# =============================================================================

print("\n" + "=" * 60)
print("PARTIE 4 : FONCTIONS - CONCEPTS AVANCÉS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercice 4.1 : Fonctions lambda
# -----------------------------------------------------------------------------


def exercice_4_1():
    """
    Utilisez les fonctions lambda
    """
    print("\n--- Exercice 4.1 : Fonctions lambda ---")

    # TODO: Créez des fonctions lambda équivalentes
    # doubler = Compléter
    # additionner = Compléter
    # est_positif = Compléter

    # TODO: Utilisez lambda avec map, filter, sorted
    nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Map avec lambda
    # carres = list(map(TODO, nombres))
    # print(f"Carrés: {carres}")

    # Filter avec lambda
    # pairs = list(filter(TODO, nombres))
    # print(f"Nombres pairs: {pairs}")

    # Sorted avec lambda
    # mots = ["python", "java", "c", "javascript", "html"]
    # tries_par_longueur = sorted(mots, key=TODO)
    # print(f"Mots triés par longueur: {tries_par_longueur}")

    # TODO: Créez un tri personnalisé
    personnes = [
        {"nom": "Alice", "age": 25},
        {"nom": "Bob", "age": 30},
        {"nom": "Charlie", "age": 22},
    ]

    # tries_par_age = sorted(personnes, key=TODO)
    # print("Personnes triées par âge:")
    # for personne in tries_par_age:
    #     print(f"  {personne['nom']}: {personne['age']} ans")


# -----------------------------------------------------------------------------
# Exercice 4.2 : Portée et closure
# -----------------------------------------------------------------------------


def exercice_4_2():
    """
    Comprenez les closures et la portée imbriquée
    """
    print("\n--- Exercice 4.2 : Closures ---")

    # TODO: Créez une fonction qui retourne une fonction

    # TODO: Créez une fonction compteur qui garde l'état

    # TODO: Testez vos closures
    # doubleur = createur_multiplicateur(2)
    # tripleur = createur_multiplicateur(3)

    # print(f"Doubleur: 5 → {doubleur(5)}")
    # print(f"Tripleur: 5 → {tripleur(5)}")

    # compteur1 = createur_compteur()
    # compteur2 = createur_compteur()

    # print("Compteur 1:", compteur1(), compteur1(), compteur1())
    # print("Compteur 2:", compteur2(), compteur2())
    # print("Compteur 1 à nouveau:", compteur1())


# -----------------------------------------------------------------------------
# Exercice 4.3 : Décorateurs simples
# -----------------------------------------------------------------------------


def exercice_4_3():
    """
    Créez des décorateurs simples
    """
    print("\n--- Exercice 4.3 : Décorateurs ---")

    # TODO: Créez un décorateur qui chronomètre une fonction

    # TODO: Créez un décorateur qui loggue les appels

    # TODO: Appliquez les décorateurs
    # @chronometre
    # @logger
    # def attendre_et_calculer(secondes, a, b):
    #     import time

    #     time.sleep(secondes)
    #     return a + b

    # # Testez
    # resultat = attendre_et_calculer(1, 5, 3)
    # print(f"Résultat final: {resultat}")


# -----------------------------------------------------------------------------
# TEST PARTIE 4
# -----------------------------------------------------------------------------


def tester_partie_4():
    """Testez tous les exercices de la partie 4"""
    exercice_4_1()
    exercice_4_2()
    exercice_4_3()


# Décommentez pour tester
# tester_partie_4()

# =============================================================================
# PARTIE 5 : PROGRAMMATION ORIENTÉE OBJET - BASES
# =============================================================================

print("\n" + "=" * 60)
print("PARTIE 5 : POO - BASES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercice 5.1 : Classes et objets simples
# -----------------------------------------------------------------------------


def exercice_5_1():
    """
    Créez des classes et objets simples
    """
    print("\n--- Exercice 5.1 : Classes simples ---")

    # TODO: Créez une classe Personne

    # TODO: Créez une classe Rectangle

    # TODO: Testez vos classes
    # personne1 = Personne("Alice", 25)
    # personne2 = Personne("Bob", 30)

    # print(personne1.se_presenter())
    # print(personne2.se_presenter())
    # personne1.feter_anniversaire()

    # rectangle = Rectangle(5, 3)
    # print(
    #     f"Rectangle: surface={rectangle.surface()}, périmètre={rectangle.perimetre()}"
    # )
    # print(f"Est un carré: {rectangle.est_carre()}")

    # carre = Rectangle(4, 4)
    # print(f"Carré: surface={carre.surface()}, est carré: {carre.est_carre()}")


# -----------------------------------------------------------------------------
# Exercice 5.2 : Attributs de classe vs d'instance
# -----------------------------------------------------------------------------


def exercice_5_2():
    """
    Comprenez la différence entre attributs de classe et d'instance
    """
    print("\n--- Exercice 5.2 : Attributs de classe vs instance ---")

    class Compteur:
        # Attribut de classe (partagé par toutes les instances)
        compteur_global = 0

        def __init__(self, nom):
            # Attributs d'instance (spécifiques à chaque objet)
            self.nom = nom
            self.compteur_local = 0
            Compteur.compteur_global += 1  # Modifie l'attribut de classe

        def incrementer(self):
            self.compteur_local += 1
            Compteur.compteur_global += 1

        def afficher(self):
            print(
                f"{self.nom}: local={self.compteur_local}, global={Compteur.compteur_global}"
            )

    # TODO: Testez la différence
    c1 = Compteur("Premier")
    c2 = Compteur("Deuxième")

    c1.incrementer()
    c1.incrementer()
    c2.incrementer()

    c1.afficher()
    c2.afficher()

    # TODO: Que se passe-t-il si on modifie un attribut de classe via une instance ?
    c1.compteur_global = 999  # Crée un attribut d'instance, ne modifie pas la classe !
    print(f"Compteur.compteur_global = {Compteur.compteur_global}")
    print(f"c1.compteur_global = {c1.compteur_global}")
    print(f"c2.compteur_global = {c2.compteur_global}")


# -----------------------------------------------------------------------------
# Exercice 5.3 : Méthodes spéciales (magic methods)
# -----------------------------------------------------------------------------


def exercice_5_3():
    """
    Utilisez les méthodes spéciales
    """
    print("\n--- Exercice 5.3 : Méthodes spéciales ---")

    class Vecteur:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # TODO: Implémentez les méthodes spéciales
        def __str__(self):
            pass

        def __add__(self, autre):
            pass

        def __eq__(self, autre):
            pass

        def __len__(self):
            # Longueur euclidienne approximative
            pass

    # Testez vos méthodes spéciales
    v1 = Vecteur(3, 4)
    v2 = Vecteur(1, 2)

    print(f"v1 = {v1}")  # Utilise __str__
    print(f"v2 = {v2}")

    v3 = v1 + v2  # Utilise __add__
    print(f"v1 + v2 = {v3}")

    print(f"v1 == v2: {v1 == v2}")  # Utilise __eq__
    print(f"Longueur de v1: {len(v1)}")  # Utilise __len__


# -----------------------------------------------------------------------------
# TEST PARTIE 5
# -----------------------------------------------------------------------------


def tester_partie_5():
    """Testez tous les exercices de la partie 5"""
    exercice_5_1()
    exercice_5_2()
    exercice_5_3()


# Décommentez pour tester
# tester_partie_5()

# =============================================================================
# PARTIE 6 : POO - CONCEPTS AVANCÉS
# =============================================================================

print("\n" + "=" * 60)
print("PARTIE 6 : POO - CONCEPTS AVANCÉS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Exercice 6.1 : Héritage
# -----------------------------------------------------------------------------


def exercice_6_1():
    """
    Utilisez l'héritage
    """
    print("\n--- Exercice 6.1 : Héritage ---")

    class Animal:
        def __init__(self, nom, age):
            self.nom = nom
            self.age = age

        def parler(self):
            return "Je ne sais pas quoi dire..."

        def se_presenter(self):
            return f"Je m'appelle {self.nom} et j'ai {self.age} an(s)"

    # TODO: Créez des classes qui héritent de Animal

    # TODO: Testez l'héritage
    # animaux = [
    #     Chien("Rex", 3),
    #     Chat("Félix", 2),
    #     Oiseau("Tweety", 1),
    #     Oiseau("Pingouin", 4, False),
    # ]

    # for animal in animaux:
    #     print(f"{animal.se_presenter()} - {animal.parler()}")

    #     # Testez les méthodes spécifiques
    #     if isinstance(animal, Chien):
    #         print(f"  {animal.aboyer()}")
    #     elif isinstance(animal, Chat):
    #         print(f"  {animal.ronronner()}")
    #     elif isinstance(animal, Oiseau):
    #         print(f"  {animal.voler()}")


# -----------------------------------------------------------------------------
# Exercice 6.2 : Encapsulation et propriétés
# -----------------------------------------------------------------------------


def exercice_6_2():
    """
    Utilisez l'encapsulation
    """
    print("\n--- Exercice 6.2 : Encapsulation ---")

    class CompteBancaire:
        def __init__(self, titulaire, solde_initial=0):
            self.titulaire = titulaire
            self.__solde = solde_initial  # Attribut privé
            self.historique = []

        # TODO: Créez des getters et setters appropriés
        def deposer(self, montant):
            pass

        def retirer(self, montant):
            pass

        # TODO: Getter pour le solde (lecture seule)

        # TODO: Créez une propriété calculée
        @property
        def solde_formatte(self):
            pass

        def afficher_historique(self):
            print(f"Historique de {self.titulaire}:")
            for operation in self.historique[-5:]:  # 5 dernières opérations
                print(f"  {operation}")
            print(f"Solde actuel: {self.solde_formatte}")

    # Testez l'encapsulation
    compte = CompteBancaire("Alice", 1000)
    compte.deposer(500)
    compte.retirer(200)

    print(f"Solde: {compte.solde_formatte}")
    # print(compte.__solde)  # ❌ Erreur ! Attribut privé
    compte.afficher_historique()


# -----------------------------------------------------------------------------
# TEST PARTIE 6
# -----------------------------------------------------------------------------


def tester_partie_6():
    """Testez tous les exercices de la partie 6"""
    exercice_6_1()
    exercice_6_2()


# Décommentez pour tester
# tester_partie_6()

# =============================================================================
# MENU PRINCIPAL
# =============================================================================


def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "=" * 60)
    print("🎯 MENU PRINCIPAL - EXERCICES PYTHON")
    print("=" * 60)
    print("1. Partie 1 - Variables et Scopes")
    print("2. Partie 2 - Fonctions Bases")
    print("3. Partie 3 - Paramètres de fonctions")
    print("4. Partie 4 - Fonctions avancées")
    print("5. Partie 5 - POO Bases")
    print("6. Partie 6 - POO Avancée")
    print("8. Tout tester")
    print("0. Quitter")
    print("=" * 60)


def main():
    """Fonction principale"""
    while True:
        afficher_menu()
        choix = input("\nChoisissez une option (0-8): ").strip()

        if choix == "0":
            print("👋 Au revoir !")
            break
        elif choix == "1":
            tester_partie_1()
        elif choix == "2":
            tester_partie_2()
        elif choix == "3":
            tester_partie_3()
        elif choix == "4":
            tester_partie_4()
        elif choix == "5":
            tester_partie_5()
        elif choix == "6":
            tester_partie_6()
        elif choix == "8":
            print("🧪 Test de tous les exercices...")
            tester_partie_1()
            tester_partie_2()
            tester_partie_3()
            tester_partie_4()
            tester_partie_5()
            tester_partie_6()
        else:
            print("❌ Option invalide !")

        input("\nAppuyez sur Entrée pour continuer...")


# =============================================================================
# EXÉCUTION
# =============================================================================

if __name__ == "__main__":
    print("🚀 LANCEMENT DES EXERCICES PYTHON")
    print("Décommentez les appels aux fonctions pour tester les exercices")
    print("Ou exécutez main() pour avoir un menu interactif")

    # Décommentez la ligne suivante pour le menu interactif
    main()

    print("\n" + "=" * 60)
    print("💡 CONSEILS POUR UTILISER CE FICHIER:")
    print("1. Décommentez les appels aux fonctions une par une")
    print("2. Modifiez le code pour expérimenter")
    print("3. Ajoutez vos propres exercices")
    print("4. Utilisez le débogueur pour comprendre l'exécution")
    print("=" * 60)
