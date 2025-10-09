"""
FORMATION PYTHON - FICHIER COMPLET D'APPRENTISSAGE
Niveau : Débutant à Intermédiaire
Auteur : Assistant Pédagogique
Description : Ce fichier couvre tous les concepts de base de Python avec explications détaillées
               et exemples pratiques. Exécutez-le section par section.
"""

# =============================================================================
# SECTION 1 : LES BASES ABSOLUES
# =============================================================================

print("=" * 60)
print("SECTION 1 : LES BASES ABSOLUES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.1 Commentaires
# -----------------------------------------------------------------------------

# Ceci est un commentaire sur une ligne
print("Les commentaires sont ignorés par Python")  # Commentaire en fin de ligne

"""
Ceci est un commentaire
sur plusieurs lignes.
Très utile pour expliquer
des parties complexes.
"""

# -----------------------------------------------------------------------------
# 1.2 Affichage avec print()
# -----------------------------------------------------------------------------

print("\n--- 1.2 AFFICHAGE ---")

# Affichage simple
print("Bonjour le monde !")

# Affichage multiple
print("Python", "est", "génial !")  # Séparé par des espaces
print("Ligne 1", end=" ")  # Pas de retour à la ligne
print("Ligne 1 suite")

# Affichage formaté (f-strings - recommandé)
nom = "Alice"
age = 25
print(f"Je m'appelle {nom} et j'ai {age} ans")

# Anciennes méthodes (pour culture)
print("Je m'appelle {} et j'ai {} ans".format(nom, age))
print("Je m'appelle %s et j'ai %d ans" % (nom, age))

# -----------------------------------------------------------------------------
# 1.3 Variables et types de base
# -----------------------------------------------------------------------------

print("\n--- 1.3 VARIABLES ET TYPES ---")

# Chaînes de caractères (string)
prenom = "Alice"  # Guillemets doubles
nom = "Dupont"  # Guillemets simples
message = "J'aime Python"  # Texte

# Nombres entiers (integer)
age = 25
nombre_etudiants = 30
temperature = -5

# Nombres décimaux (float)
prix = 19.99
taille = 1.75
pourcentage = 0.15

# Booléens (boolean)
est_actif = True
est_connecte = False
majeur = age >= 18  # Résultat d'une comparaison

# None (vide)
resultat = None
valeur_par_defaut = None

# Affichons tout ça
print(f"Prénom: {prenom} (type: {type(prenom)})")
print(f"Âge: {age} (type: {type(age)})")
print(f"Prix: {prix} (type: {type(prix)})")
print(f"Est actif: {est_actif} (type: {type(est_actif)})")
print(f"Résultat: {resultat} (type: {type(resultat)})")

# -----------------------------------------------------------------------------
# 1.4 Opérations de base
# -----------------------------------------------------------------------------

print("\n--- 1.4 OPÉRATIONS ---")

# Opérations mathématiques
a = 10
b = 3

print(f"{a} + {b} = {a + b}")  # Addition
print(f"{a} - {b} = {a - b}")  # Soustraction
print(f"{a} * {b} = {a * b}")  # Multiplication
print(f"{a} / {b} = {a / b}")  # Division normale
print(f"{a} // {b} = {a // b}")  # Division entière
print(f"{a} % {b} = {a % b}")  # Modulo (reste)
print(f"{a} ** {b} = {a**b}")  # Puissance

# Opérations sur les chaînes
texte1 = "Hello"
texte2 = "World"

print(f"{texte1} + {texte2} = {texte1 + texte2}")  # Concaténation
print(f"{texte1} * 3 = {texte1 * 3}")  # Répétition

# Conversions de types
nombre_texte = "123"
nombre_reel = float("3.14")
texte_nombre = str(456)
booleen = bool(1)  # 0 → False, autre → True

print(f"'{nombre_texte}' → int: {int(nombre_texte)}")
print(f"'{nombre_texte}' → float: {float(nombre_texte)}")
print(f"123 → str: '{str(123)}'")

# =============================================================================
# SECTION 2 : STRUCTURES DE CONTRÔLE
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2 : STRUCTURES DE CONTRÔLE")
print("=" * 60)

# -----------------------------------------------------------------------------
# 2.1 Les conditions (if, elif, else)
# -----------------------------------------------------------------------------

print("\n--- 2.1 CONDITIONS ---")

# Opérateurs de comparaison
x = 10
y = 5

print(f"{x} == {y} → {x == y}")  # Égal à
print(f"{x} != {y} → {x != y}")  # Différent de
print(f"{x} > {y} → {x > y}")  # Plus grand que
print(f"{x} < {y} → {x < y}")  # Plus petit que
print(f"{x} >= {y} → {x >= y}")  # Plus grand ou égal
print(f"{x} <= {y} → {x <= y}")  # Plus petit ou égal

# Opérateurs logiques
print(f"True and False → {True and False}")  # ET
print(f"True or False → {True or False}")  # OU
print(f"not True → {not True}")  # NON


# Structure if/elif/else
def evaluer_note(note):
    """Évalue une note et donne un commentaire"""
    if note < 0 or note > 20:
        return "Note invalide"
    elif note >= 16:
        return "Très bien !"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"


# Testons notre fonction
notes_test = [8, 11, 15, 18, 25]
for note in notes_test:
    print(f"Note {note}/20 : {evaluer_note(note)}")


# Conditions imbriquées
def peut_conduire(age, permis):
    """Détermine si une personne peut conduire"""
    if age >= 18:
        if permis:
            return "Peut conduire"
        else:
            return "Doit passer le permis"
    else:
        return "Trop jeune pour conduire"


print(f"18 ans, sans permis: {peut_conduire(18, False)}")

# -----------------------------------------------------------------------------
# 2.2 Les boucles
# -----------------------------------------------------------------------------

print("\n--- 2.2 BOUCLES ---")

# Boucle FOR - Parcours de séquences
print("Boucle FOR avec range():")
for i in range(5):  # 0 à 4
    print(f"Tour {i}")

print("Boucle FOR avec range() et paramètres:")
for i in range(2, 6):  # 2 à 5
    print(f"Nombre: {i}")

for i in range(0, 10, 2):  # 0 à 8, pas de 2
    print(f"Pair: {i}")

# Parcours de liste
fruits = ["pomme", "banane", "orange"]
print("Parcours de liste:")
for fruit in fruits:
    print(f"J'aime les {fruits}")

# Avec l'index
print("Avec index:")
for i, fruit in enumerate(fruits):
    print(f"{i + 1}. {fruit}")

# Boucle WHILE - Répétition conditionnelle
print("Boucle WHILE:")
compteur = 0
while compteur < 3:
    print(f"Compteur: {compteur}")
    compteur += 1  # Ne pas oublier d'incrémenter !

# Boucle avec break et continue
print("Avec break et continue:")
for i in range(10):
    if i == 2:
        continue  # Passe cette itération
    if i == 5:
        break  # Arrête la boucle
    print(i)

# =============================================================================
# SECTION 3 : STRUCTURES DE DONNÉES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3 : STRUCTURES DE DONNÉES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 3.1 Les listes (lists)
# -----------------------------------------------------------------------------

print("\n--- 3.1 LISTES ---")

# Création de listes
liste_vide = []
nombres = [1, 2, 3, 4, 5]
fruits = ["pomme", "banane", "orange"]
mixte = [1, "texte", 3.14, True]

print(f"Liste de nombres: {nombres}")
print(f"Liste de fruits: {fruits}")

# Accès aux éléments
print(f"Premier fruit: {fruits[0]}")  # Index 0
print(f"Dernier fruit: {fruits[-1]}")  # Index -1
print(f"Deuxième fruit: {fruits[1]}")  # Index 1

# Slicing (tranches)
print(f"2 premiers: {fruits[0:2]}")  # Index 0 à 1
print(f"A partir du 2ème: {fruits[1:]}")  # Index 1 à fin
print(f"Tous sauf dernier: {fruits[:-1]}")  # Tous sauf -1

# Méthodes utiles des listes
ma_liste = [3, 1, 4, 1, 5]

ma_liste.append(9)  # Ajouter à la fin
print(f"Après append(9): {ma_liste}")

ma_liste.insert(2, 2)  # Insérer à position
print(f"Après insert(2, 2): {ma_liste}")

ma_liste.remove(1)  # Supprimer première occurrence
print(f"Après remove(1): {ma_liste}")

element = ma_liste.pop()  # Retirer et retourner dernier
print(f"pop() a retiré: {element}")
print(f"Après pop(): {ma_liste}")

ma_liste.sort()  # Trier
print(f"Après sort(): {ma_liste}")

ma_liste.reverse()  # Inverser
print(f"Après reverse(): {ma_liste}")

# Opérations sur les listes
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

concat = liste1 + liste2  # Concaténation
print(f"Concaténation: {concat}")

repetition = liste1 * 2  # Répétition
print(f"Répétition: {repetition}")

# List comprehension (création avancée)
carres = [x**2 for x in range(1, 6)]
print(f"Carrés de 1-5: {carres}")

pairs = [x for x in range(10) if x % 2 == 0]
print(f"Nombres pairs: {pairs}")

# -----------------------------------------------------------------------------
# 3.2 Les dictionnaires (dicts)
# -----------------------------------------------------------------------------

print("\n--- 3.2 DICTIONNAIRES ---")

# Création de dictionnaires
dict_vide = {}
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris",
    "hobbies": ["lecture", "sport"],
}

etudiant = dict(nom="Bob", age=22)  # Autre syntaxe

print(f"Dictionnaire personne: {personne}")

# Accès aux valeurs
print(f"Nom: {personne['nom']}")  # Avec crochets
print(f"Âge: {personne.get('age')}")  # Avec get (plus sûr)

# get() avec valeur par défaut
print(f"Téléphone: {personne.get('telephone', 'Non renseigné')}")

# Modification
personne["age"] = 26  # Modifier
personne["telephone"] = "01 23 45 67 89"  # Ajouter
print(f"Après modifications: {personne}")

# Méthodes utiles
print(f"Clés: {list(personne.keys())}")  # Toutes les clés
print(f"Valeurs: {list(personne.values())}")  # Toutes les valeurs
print(f"Items: {list(personne.items())}")  # Paires clé-valeur

# Parcours d'un dictionnaire
print("Parcours par clé-valeur:")
for cle, valeur in personne.items():
    print(f"  {cle}: {valeur}")

# Dictionnaires imbriqués
catalogue = {
    "livres": {"python": {"prix": 35, "stock": 10}, "java": {"prix": 40, "stock": 5}},
    "formations": {"debutant": 200, "avance": 350},
}

print(f"Prix du livre Python: {catalogue['livres']['python']['prix']}€")

# -----------------------------------------------------------------------------
# 3.3 Tuples et sets
# -----------------------------------------------------------------------------

print("\n--- 3.3 TUPLES ET SETS ---")

# Tuples (immuables)
coordonnees = (48.8566, 2.3522)  # Latitude, longitude
jours_semaine = ("lundi", "mardi", "mercredi")

print(f"Coordonnées: {coordonnees}")
print(f"Premier jour: {jours_semaine[0]}")

# Les tuples ne peuvent pas être modifiés
# coordonnees[0] = 50.0  # ❌ Erreur !

# Sets (ensembles - éléments uniques)
ensemble_vide = set()
nombres_uniques = {1, 2, 3, 2, 1}  # Les doublons sont supprimés
print(f"Set avec doublons: {nombres_uniques}")  # Affiche {1, 2, 3}

# Opérations sur les sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(f"Union: {set1 | set2}")  # {1, 2, 3, 4, 5}
print(f"Intersection: {set1 & set2}")  # {3}
print(f"Différence: {set1 - set2}")  # {1, 2}

# =============================================================================
# SECTION 4 : FONCTIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4 : FONCTIONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 Définition et appel de fonctions
# -----------------------------------------------------------------------------

print("\n--- 4.1 FONCTIONS DE BASE ---")


# Fonction simple sans paramètres
def dire_bonjour():
    """Affiche un message de bienvenue"""
    print("Bonjour ! Bienvenue en Python !")


# Fonction avec paramètres
def saluer_personne(nom, age):
    """Saluer une personne avec son nom et âge"""
    print(f"Bonjour {nom}, vous avez {age} ans !")


# Fonction avec retour
def calculer_carre(nombre):
    """Retourne le carré d'un nombre"""
    return nombre**2


# Appel des fonctions
dire_bonjour()
saluer_personne("Alice", 25)
resultat = calculer_carre(5)
print(f"5 au carré = {resultat}")

# -----------------------------------------------------------------------------
# 4.2 Paramètres avancés
# -----------------------------------------------------------------------------

print("\n--- 4.2 PARAMÈTRES AVANCÉS ---")


# Paramètres avec valeurs par défaut
def decrire_animal(nom, type_animal="chien", age=1):
    """Décrit un animal avec des paramètres optionnels"""
    print(f"{nom} est un {type_animal} de {age} an(s)")


decrire_animal("Rex")  # Utilise les valeurs par défaut
decrire_animal("Félix", "chat", 3)  # Spécifie toutes les valeurs
decrire_animal("Tweety", age=2)  # Spécifie seulement l'âge


# Paramètres nommés (keyword arguments)
def creer_personne(nom, age, ville, profession="étudiant"):
    """Crée une description de personne"""
    return f"{nom}, {age} ans, habite à {ville}, {profession}"


# Appels équivalents
personne1 = creer_personne("Alice", 25, "Paris")
personne2 = creer_personne(age=25, nom="Alice", ville="Paris")
print(personne1)
print(personne2)


# Nombre variable d'arguments
def additionner(*nombres):
    """Additionne un nombre variable de paramètres"""
    total = 0
    for nombre in nombres:
        total += nombre
    return total


print(f"Addition: {additionner(1, 2, 3)}")  # 3 paramètres
print(f"Addition: {additionner(1, 2, 3, 4, 5)}")  # 5 paramètres


# Paramètres keyword variables
def afficher_infos(**infos):
    """Affiche des informations sous forme de dictionnaire"""
    for cle, valeur in infos.items():
        print(f"{cle}: {valeur}")


afficher_infos(nom="Alice", age=25, ville="Paris")

# -----------------------------------------------------------------------------
# 4.3 Portée des variables
# -----------------------------------------------------------------------------

print("\n--- 4.3 PORTÉE DES VARIABLES ---")

variable_globale = "Je suis globale"


def tester_portee():
    """Démontre la portée des variables"""
    variable_locale = "Je suis locale"
    global variable_globale  # Permet de modifier la variable globale

    print(f"Dans la fonction: {variable_locale}")
    print(f"Dans la fonction: {variable_globale}")

    # Modification de la variable globale
    variable_globale = "Modifiée dans la fonction"


print(f"Avant fonction: {variable_globale}")
tester_portee()
print(f"Après fonction: {variable_globale}")

# -----------------------------------------------------------------------------
# 4.4 Fonctions lambda
# -----------------------------------------------------------------------------

print("\n--- 4.4 FONCTIONS LAMBDA ---")

# Fonction lambda simple
carre = lambda x: x**2
print(f"Carre de 4: {carre(4)}")

# Utilisation avec map()
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))
print(f"Nombres: {nombres}")
print(f"Carrés: {carres}")

# Utilisation avec filter()
pairs = list(filter(lambda x: x % 2 == 0, nombres))
print(f"Nombres pairs: {pairs}")

# =============================================================================
# SECTION 5 : GESTION DES ERREURS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5 : GESTION DES ERREURS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 5.1 Try/Except de base
# -----------------------------------------------------------------------------

print("\n--- 5.1 GESTION D'ERREURS ---")


# Gestion simple
def diviser_nombres(a, b):
    """Divise deux nombres avec gestion d'erreur"""
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        return "Erreur: Division par zéro !"
    except TypeError:
        return "Erreur: Types de données incorrects !"


print(f"10 / 2 = {diviser_nombres(10, 2)}")
print(f"10 / 0 = {diviser_nombres(10, 0)}")
print(f"10 / 'a' = {diviser_nombres(10, 'a')}")


# Gestion multiple
def convertir_et_calculer(texte):
    """Convertit un texte en nombre et effectue un calcul"""
    try:
        nombre = float(texte)
        carre = nombre**2
        return f"Le carré de {nombre} est {carre}"

    except ValueError:
        return "Erreur: Ce n'est pas un nombre valide !"
    except Exception as e:
        return f"Erreur inattendue: {e}"


print(convertir_et_calculer("10"))
print(convertir_et_calculer("abc"))


# Try/Except/Else/Finally
def ouvrir_fichier(nom_fichier):
    """Simule l'ouverture d'un fichier"""
    try:
        print(f"Tentative d'ouverture de {nom_fichier}...")
        # Simuler une erreur
        if nom_fichier == "erreur.txt":
            raise FileNotFoundError("Fichier non trouvé")

        resultat = "Contenu du fichier"

    except FileNotFoundError:
        print("❌ Fichier non trouvé !")
        return None

    else:
        print("✅ Fichier ouvert avec succès !")
        return resultat

    finally:
        print("🔧 Cette partie s'exécute toujours !")


ouvrir_fichier("normal.txt")
print()
ouvrir_fichier("erreur.txt")

# -----------------------------------------------------------------------------
# 5.2 Lever des exceptions
# -----------------------------------------------------------------------------

print("\n--- 5.2 LEVER DES EXCEPTIONS ---")


def verifier_age(age):
    """Vérifie si l'âge est valide"""
    if not isinstance(age, (int, float)):
        raise TypeError("L'âge doit être un nombre")

    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")

    if age > 150:
        raise ValueError("Âge invraisemblable")

    return True


# Test des exceptions
ages_test = [25, -5, "vingt", 200]
for age in ages_test:
    try:
        verifier_age(age)
        print(f"✅ Âge {age} valide")
    except (TypeError, ValueError) as e:
        print(f"❌ Âge {age}: {e}")

# =============================================================================
# SECTION 6 : PROGRAMMATION ORIENTÉE OBJET (POO)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6 : PROGRAMMATION ORIENTÉE OBJET")
print("=" * 60)

# -----------------------------------------------------------------------------
# 6.1 Classes et objets
# -----------------------------------------------------------------------------

print("\n--- 6.1 CLASSES ET OBJETS ---")


class Personne:
    """Classe représentant une personne"""

    # Attribut de classe (partagé par toutes les instances)
    espece = "Homo sapiens"

    def __init__(self, nom, age):
        """Constructeur - initialise l'objet"""
        # Attributs d'instance (spécifiques à chaque objet)
        self.nom = nom
        self.age = age
        self.amis = []  # Liste vide par défaut

    def se_presenter(self):
        """Méthode pour se présenter"""
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"

    def feter_anniversaire(self):
        """Augmente l'âge de 1 an"""
        self.age += 1
        print(
            f"🎂 Joyeux anniversaire {self.nom} ! Vous avez maintenant {self.age} ans"
        )

    def ajouter_ami(self, ami):
        """Ajoute un ami à la liste"""
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"👋 {self.nom} est maintenant ami avec {ami.nom}")

    def afficher_amis(self):
        """Affiche la liste des amis"""
        if not self.amis:
            print(f"{self.nom} n'a pas encore d'amis 😢")
        else:
            print(f"Amis de {self.nom}:")
            for ami in self.amis:
                print(f"  - {ami.nom} ({ami.age} ans)")


# Création d'objets
personne1 = Personne("Alice", 25)
personne2 = Personne("Bob", 30)

# Utilisation des méthodes
print(personne1.se_presenter())
print(personne2.se_presenter())

print(f"\nEspèce: {Personne.espece}")  # Attribut de classe

personne1.feter_anniversaire()
personne1.ajouter_ami(personne2)
personne1.afficher_amis()

# -----------------------------------------------------------------------------
# 6.2 Héritage
# -----------------------------------------------------------------------------

print("\n--- 6.2 HÉRITAGE ---")


class Etudiant(Personne):
    """Classe Étudiant qui hérite de Personne"""

    def __init__(self, nom, age, numero_etudiant, moyenne=0.0):
        # Appel du constructeur parent
        super().__init__(nom, age)
        self.numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.notes = []

    def se_presenter(self):  # Redéfinition de méthode
        presentation = super().se_presenter()
        return f"{presentation} (Étudiant n°{self.numero_etudiant})"

    def ajouter_note(self, note):
        """Ajoute une note et recalcule la moyenne"""
        if 0 <= note <= 20:
            self.notes.append(note)
            self.moyenne = sum(self.notes) / len(self.notes)
            print(f"📝 Note {note}/20 ajoutée. Moyenne: {self.moyenne:.2f}")
        else:
            print("❌ Note invalide (doit être entre 0 et 20)")

    def obtenir_statut(self):
        """Retourne le statut académique"""
        if self.moyenne >= 16:
            return "Très bien"
        elif self.moyenne >= 14:
            return "Bien"
        elif self.moyenne >= 12:
            return "Assez bien"
        elif self.moyenne >= 10:
            return "Passable"
        else:
            return "Insuffisant"


# Test de l'héritage
etudiant = Etudiant("Charlie", 20, "ETU12345")
print(etudiant.se_presenter())

etudiant.ajouter_note(15)
etudiant.ajouter_note(18)
print(f"Statut: {etudiant.obtenir_statut()}")

# -----------------------------------------------------------------------------
# 6.3 Encapsulation et propriétés
# -----------------------------------------------------------------------------

print("\n--- 6.3 ENCAPSULATION ---")


class CompteBancaire:
    """Classe représentant un compte bancaire avec encapsulation"""

    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self.__solde = solde_initial  # Attribut privé (double underscore)
        self.historique = []

    def deposer(self, montant):
        """Dépose de l'argent sur le compte"""
        if montant > 0:
            self.__solde += montant
            self.historique.append(f"Dépôt: +{montant}€")
            print(f"✅ {montant}€ déposés. Nouveau solde: {self.__solde}€")
            return True
        else:
            print("❌ Le montant doit être positif")
            return False

    def retirer(self, montant):
        """Retire de l'argent du compte"""
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self.historique.append(f"Retrait: -{montant}€")
            print(f"✅ {montant}€ retirés. Nouveau solde: {self.__solde}€")
            return True
        else:
            print("❌ Montant invalide ou solde insuffisant")
            return False

    # Getter pour le solde (lecture seule)
    @property
    def solde(self):
        return self.__solde

    def afficher_historique(self):
        """Affiche l'historique des transactions"""
        print(f"\n📊 Historique du compte de {self.titulaire}:")
        if not self.historique:
            print("Aucune transaction")
        else:
            for transaction in self.historique:
                print(f"  {transaction}")
        print(f"Solde actuel: {self.__solde}€")


# Test de l'encapsulation
compte = CompteBancaire("Alice", 1000)
compte.deposer(500)
compte.retirer(200)
# compte.__solde = 5000  # ❌ Ne fonctionne pas (attribut privé)
print(f"Solde via getter: {compte.solde}€")  # ✅ Fonctionne
compte.afficher_historique()


# =============================================================================
# CONCLUSION
# =============================================================================

print("\n" + "=" * 60)
print("🎓 FÉLICITATIONS !")
print("=" * 60)

print(
    """
Vous avez complété ce cours complet de Python ! 🐍

Récapitulatif des concepts couverts :
✓ Bases de la syntaxe Python
✓ Structures de contrôle (conditions, boucles)
✓ Structures de données (listes, dictionnaires, tuples, sets)
✓ Fonctions et portée des variables
✓ Gestion des erreurs et exceptions
✓ Programmation Orientée Objet (classes, héritage, encapsulation)

Prochaines étapes recommandées :
1. Pratiquer régulièrement avec des petits projets
2. Explorer les bibliothèques standards (os, datetime, json)
3. Apprendre à utiliser les modules externes (requests, pandas)
4. Découvrir le développement web avec Flask ou Django
5. Contribuer à des projets open source

Rappel : La pratique est la clé de la maîtrise !
Codez tous les jours, même 15 minutes. 💻

Bonne continuation dans votre apprentissage de Python !
"""
)

# =============================================================================
# BONUS : FONCTIONNALITÉS AVANCÉES
# =============================================================================

print("\n" + "=" * 60)
print("BONUS : FONCTIONNALITÉS AVANCÉES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Décorateurs
# -----------------------------------------------------------------------------

print("\n--- DÉCORATEURS ---")


def chronometrer(fonction):
    """Décorateur qui mesure le temps d'exécution"""
    import time

    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print(f"⏱️  {fonction.__name__} a pris {fin - debut:.4f} secondes")
        return resultat

    return wrapper


@chronometrer
def attendre_seconde():
    """Fonction qui attend 1 seconde"""
    import time

    time.sleep(1)
    return "Terminé !"


print(attendre_seconde())

# -----------------------------------------------------------------------------
# Générateurs
# -----------------------------------------------------------------------------

print("\n--- GÉNÉRATEURS ---")


def generateur_nombres_pairs(limite):
    """Générateur qui produit des nombres pairs"""
    for i in range(0, limite, 2):
        yield i  # yield au lieu de return


# Utilisation du générateur
print("Nombres pairs jusqu'à 10:")
for nombre in generateur_nombres_pairs(10):
    print(nombre, end=" ")
print()

# Expression de générateur
carres = (x**2 for x in range(5))
print("Carrés via expression:", list(carres))

# -----------------------------------------------------------------------------
# Context Managers (with)
# -----------------------------------------------------------------------------

print("\n--- GESTIONNAIRES DE CONTEXTE ---")


class Temporisateur:
    """Context manager qui mesure le temps"""

    def __enter__(self):
        import time

        self.debut = time.time()
        print("⏰ Début du chronomètre")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time

        self.fin = time.time()
        print(f"⏰ Fin du chronomètre: {self.fin - self.debut:.4f} secondes")


# Utilisation
with Temporisateur():
    import time

    time.sleep(0.5)
    print("Pause de 0.5 seconde")

print("\n" + "=" * 60)
print("🌟 VOUS ÊTES MAINTENANT UN DÉVELOPPEUR PYTHON ! 🌟")
print("=" * 60)
