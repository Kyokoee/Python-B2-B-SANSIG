"""
🎯 PRÉSENTATION COMPLÈTE - GESTION D'ERREURS EN PYTHON
Niveau : Débutant à Intermédiaire
"""

# =============================================================================
# INTRODUCTION - POURQUOI LA GESTION D'ERREURS ?
# =============================================================================

print("=" * 70)
print("🎯 GESTION D'ERREURS EN PYTHON")
print("=" * 70)

print(
    """
📊 POURQUOI EST-CE IMPORTANT ?

1. 💥 Les erreurs arrivent TOUJOURS en programmation
2. 🛡️  Éviter les plantages inattendus
3. 🎯 Donner des messages d'erreur clairs aux utilisateurs
4. 🔄 Permettre la reprise après une erreur
5. 📝 Faciliter le débogage
"""
)

# =============================================================================
# SECTION 1 : LES DIFFÉRENTS TYPES D'ERREURS
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 1 : TYPES D'ERREURS")
print("=" * 70)


def demonstration_erreurs():
    """
    Demonstration des différents types d'erreurs courantes
    """
    print("\n🔍 EXAMEN DES ERREURS COURANTES")
    print("-" * 40)

    # 1. SyntaxError - Erreur de syntaxe
    print("1. ❌ SyntaxError - Erreur dans la structure du code")
    # Exemple: if x = 5:  # Au lieu de if x == 5:
    print("   Exemple: if x = 5: → Mauvaise affectation dans une condition")

    # 2. NameError - Variable non définie
    print("\n2. ❌ NameError - Variable non définie")
    try:
        print(variable_inexistante)
    except NameError as e:
        print(f"   Exemple: {e}")

    # 3. TypeError - Mauvais type de données
    print("\n3. ❌ TypeError - Opération sur des types incompatibles")
    try:
        resultat = "hello" + 5
    except TypeError as e:
        print(f"   Exemple: {e}")

    # 4. ValueError - Valeur inappropriée
    print("\n4. ❌ ValueError - Valeur incorrecte pour l'opération")
    try:
        nombre = int("abc")
    except ValueError as e:
        print(f"   Exemple: {e}")

    # 5. IndexError - Index hors limites
    print("\n5. ❌ IndexError - Accès à un index inexistant")
    try:
        liste = [1, 2, 3]
        element = liste[10]
    except IndexError as e:
        print(f"   Exemple: {e}")

    # 6. KeyError - Clé de dictionnaire inexistante
    print("\n6. ❌ KeyError - Clé de dictionnaire introuvable")
    try:
        dico = {"a": 1, "b": 2}
        valeur = dico["c"]
    except KeyError as e:
        print(f"   Exemple: {e}")

    # 7. AttributeError - Attribut/méthode inexistant
    print("\n7. ❌ AttributeError - Attribut ou méthode inexistant")
    try:
        nombre = 10
        nombre.methode_inexistante()
    except AttributeError as e:
        print(f"   Exemple: {e}")

    # 8. ZeroDivisionError - Division par zéro
    print("\n8. ❌ ZeroDivisionError - Division par zéro")
    try:
        resultat = 10 / 0
    except ZeroDivisionError as e:
        print(f"   Exemple: {e}")


# demonstration_erreurs()

# =============================================================================
# SECTION 2 : LA STRUCTURE TRY/EXCEPT DE BASE
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 2 : STRUCTURE TRY/EXCEPT")
print("=" * 70)


def structure_de_base():
    """
    Structure fondamentale de la gestion d'erreurs
    """
    print(
        """
🧱 STRUCTURE FONDAMENTALE :

    try:
        # Code qui peut générer une erreur
        operation_risquee()
    except ExceptionType:
        # Code exécuté si l'erreur se produit
        gerer_erreur()
    """
    )

    print("\n📝 EXEMPLE PRATIQUE :")
    print("-" * 30)

    # Exemple 1: Gestion simple
    def convertir_en_entier(texte):
        try:
            nombre = int(texte)
            return f"✅ Conversion réussie: {nombre}"
        except ValueError:
            return "❌ Erreur: Ce n'est pas un nombre valide !"

    # Test
    tests = ["123", "45.67", "abc", "1000"]
    for test in tests:
        print(f"'{test}' → {convertir_en_entier(test)}")

    print("\n🎯 AVANTAGES :")
    print("• ✅ Empêche le plantage du programme")
    print("• ✅ Donne un feedback utile à l'utilisateur")
    print("• ✅ Permet de continuer l'exécution")


# structure_de_base()

# =============================================================================
# SECTION 3 : GESTION MULTIPLE DES ERREURS
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 3 : GESTION MULTIPLE DES ERREURS")
print("=" * 70)


def gestion_multiple():
    """
    Gestion de différents types d'erreurs
    """
    print(
        """
🎯 GESTIONNER DIFFÉRENTS TYPES D'ERREURS :

    try:
        operation_complexe()
    except TypeError:
        gerer_erreur_type()
    except ValueError:
        gerer_erreur_valeur()
    except ZeroDivisionError:
        gerer_division_zero()
    """
    )

    print("\n🔧 EXEMPLE COMPLET :")
    print("-" * 30)

    def calculer_expression(expression):
        """
        Calcule une expression mathématique avec gestion d'erreurs complète
        """
        try:
            resultat = eval(expression)
            return f"✅ Résultat: {resultat}"

        except SyntaxError:
            return "❌ Erreur de syntaxe dans l'expression"

        except TypeError:
            return "❌ Types de données incompatibles"

        except ZeroDivisionError:
            return "❌ Division par zéro impossible"

        except NameError:
            return "❌ Variable non définie dans l'expression"

        except Exception as e:
            return f"❌ Erreur inattendue: {type(e).__name__} - {e}"

    # Tests
    expressions = [
        "10 + 5",
        "10 / 0",
        "10 + 'abc'",
        "variable_inexistante * 2",
        "10 * (5 + 3",
        "2 ** 1000",
    ]

    for expr in expressions:
        print(f"'{expr}' → {calculer_expression(expr)}")

    print("\n💡 ASTUCE : Capturer plusieurs exceptions en une ligne")
    try:
        print("Simulation de fonction")
    except (ValueError, TypeError) as e:
        print(f"Erreur de valeur ou type: {e}")


# gestion_multiple()

# =============================================================================
# SECTION 4 : ELSE ET FINALLY
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 4 : ELSE ET FINALLY")
print("=" * 70)


def else_et_finally():
    """
    Utilisation de else et finally dans la gestion d'erreurs
    """
    print(
        """
🔄 STRUCTURE COMPLÈTE :

try:
    # Code à risque
    operation_risquee()
except:
    # Si erreur
    gerer_erreur()
else:
    # Si PAS d'erreur
    operation_si_reussite()
finally:
    # TOUJOURS exécuté
    nettoyage_obligatoire()
    """
    )

    print("\n🏗️  EXEMPLE PRATIQUE :")
    print("-" * 30)

    def traiter_fichier(nom_fichier):
        """
        Simule le traitement d'un fichier avec gestion complète
        """
        print(f"\n📁 Traitement du fichier: {nom_fichier}")

        try:
            # Simulation d'ouverture de fichier
            if nom_fichier == "fichier_corrompu.txt":
                raise IOError("Fichier corrompu")
            elif nom_fichier == "fichier_inexistant.txt":
                raise FileNotFoundError("Fichier non trouvé")

            print("   ✅ Fichier ouvert avec succès")
            contenu = "Contenu du fichier"

        except FileNotFoundError:
            print("   ❌ Erreur: Fichier non trouvé")
            return None

        except IOError as e:
            print(f"   ❌ Erreur d'E/S: {e}")
            return None

        except Exception as e:
            print(f"   ❌ Erreur inattendue: {e}")
            return None

        else:
            # Exécuté seulement si aucune exception n'est levée
            print("   ✅ Traitement du contenu réussi")
            return contenu.upper()

        finally:
            # TOUJOURS exécuté, erreur ou non
            print("   🔧 Fermeture des ressources (toujours exécuté)")

    # Tests
    fichiers = ["fichier_normal.txt", "fichier_inexistant.txt", "fichier_corrompu.txt"]

    for fichier in fichiers:
        resultat = traiter_fichier(fichier)
        if resultat:
            print(f"   📄 Résultat: {resultat}")


# else_et_finally()

# =============================================================================
# SECTION 5 : LEVER DES EXCEPTIONS (RAISE)
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 5 : LEVER DES EXCEPTIONS")
print("=" * 70)


def lever_exceptions():
    """
    Comment et pourquoi lever des exceptions
    """
    print(
        """
🚨 POURQUOI LEVER DES EXCEPTIONS ?

1. 🎯 Valider des données d'entrée
2. 🛡️  Empêcher des états invalides
3. 📢 Signaler des problèmes métier
4. 🔄 Forcer la gestion d'erreurs
    """
    )

    print("\n🎯 EXEMPLE : VALIDATION D'ÂGE")
    print("-" * 30)

    def verifier_age(age):
        """
        Valide un âge avec des exceptions personnalisées
        """
        if not isinstance(age, (int, float)):
            raise TypeError("L'âge doit être un nombre")

        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")

        if age > 150:
            raise ValueError("Âge invraisemblable (max 150 ans)")

        if age < 18:
            raise PermissionError("Accès réservé aux majeurs")

        return f"✅ Âge {age} validé !"

    # Tests
    ages_test = [25, -5, "vingt", 200, 15]

    for age in ages_test:
        try:
            resultat = verifier_age(age)
            print(f"Âge {age}: {resultat}")
        except (TypeError, ValueError, PermissionError) as e:
            print(f"Âge {age}: ❌ {e}")

    print("\n🔧 EXEMPLE AVEC EXCEPTION PERSONNALISÉE")
    print("-" * 40)

    class SoldeInsuffisantError(Exception):
        """Exception personnalisée pour un solde insuffisant"""

        def __init__(self, solde, montant):
            self.solde = solde
            self.montant = montant
            super().__init__(f"Solde insuffisant: {solde}€ pour retirer {montant}€")

    class CompteBancaire:
        def __init__(self, solde_initial=0):
            self.solde = solde_initial

        def retirer(self, montant):
            if montant <= 0:
                raise ValueError("Le montant doit être positif")

            if montant > self.solde:
                raise SoldeInsuffisantError(self.solde, montant)

            self.solde -= montant
            return f"✅ Retrait de {montant}€ effectué. Nouveau solde: {self.solde}€"

    # Test du compte bancaire
    compte = CompteBancaire(1000)

    operations = [500, 2000, -100, 300]

    for montant in operations:
        try:
            resultat = compte.retirer(montant)
            print(f"Retrait {montant}€: {resultat}")
        except (ValueError, SoldeInsuffisantError) as e:
            print(f"Retrait {montant}€: ❌ {e}")


# lever_exceptions()

# =============================================================================
# SECTION 6 : EXCEPTIONS PERSONNALISÉES
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 6 : EXCEPTIONS PERSONNALISÉES")
print("=" * 70)


def exceptions_personnalisees():
    """
    Création et utilisation d'exceptions personnalisées
    """
    print(
        """
🎨 POURQUOI DES EXCEPTIONS PERSONNALISÉES ?

1. 🎯 Clarifier la sémantique des erreurs métier
2. 🏷️  Catégoriser les erreurs spécifiques
3. 📊 Ajouter des informations contextuelles
4. 🔧 Faciliter la gestion spécifique
    """
    )

    print("\n🔧 CRÉATION D'EXCEPTIONS MÉTIER")
    print("-" * 30)

    # Exceptions personnalisées pour un système d'authentification
    class ErreurAuthentification(Exception):
        """Classe de base pour les erreurs d'authentification"""

        pass

    class UtilisateurInexistantError(ErreurAuthentification):
        """L'utilisateur n'existe pas"""

        def __init__(self, nom_utilisateur):
            self.nom_utilisateur = nom_utilisateur
            super().__init__(f"L'utilisateur '{nom_utilisateur}' n'existe pas")

    class MotDePasseIncorrectError(ErreurAuthentification):
        """Le mot de passe est incorrect"""

        def __init__(self, nom_utilisateur):
            self.nom_utilisateur = nom_utilisateur
            super().__init__(f"Mot de passe incorrect pour '{nom_utilisateur}'")

    class CompteBloqueError(ErreurAuthentification):
        """Le compte est bloqué"""

        def __init__(self, nom_utilisateur, duree_blocage=30):
            self.nom_utilisateur = nom_utilisateur
            self.duree_blocage = duree_blocage
            super().__init__(
                f"Compte '{nom_utilisateur}' bloqué pour {duree_blocage} minutes"
            )

    print("\n🏗️  SYSTÈME D'AUTHENTIFICATION")
    print("-" * 30)

    class SystemeAuthentification:
        def __init__(self):
            self.utilisateurs = {
                "alice": {
                    "mot_de_passe": "secret123",
                    "tentatives": 0,
                    "bloque": False,
                },
                "bob": {"mot_de_passe": "password", "tentatives": 0, "bloque": False},
            }
            self.max_tentatives = 3

        def authentifier(self, nom_utilisateur, mot_de_passe):
            # Vérifier si l'utilisateur existe
            if nom_utilisateur not in self.utilisateurs:
                raise UtilisateurInexistantError(nom_utilisateur)

            utilisateur = self.utilisateurs[nom_utilisateur]

            # Vérifier si le compte est bloqué
            if utilisateur["bloque"]:
                raise CompteBloqueError(nom_utilisateur)

            # Vérifier le mot de passe
            if utilisateur["mot_de_passe"] != mot_de_passe:
                utilisateur["tentatives"] += 1

                # Bloquer le compte si trop de tentatives
                if utilisateur["tentatives"] >= self.max_tentatives:
                    utilisateur["bloque"] = True
                    raise CompteBloqueError(nom_utilisateur)
                else:
                    raise MotDePasseIncorrectError(nom_utilisateur)

            # Réinitialiser les tentatives en cas de succès
            utilisateur["tentatives"] = 0
            return f"✅ Authentification réussie pour '{nom_utilisateur}'"

    # Test du système
    auth = SystemeAuthentification()

    scenarios = [
        ("alice", "secret123"),  # ✅ Succès
        ("charlie", "mdp"),  # ❌ Utilisateur inexistant
        ("alice", "mauvais_mdp"),  # ❌ Mot de passe incorrect
        ("bob", "mauvais"),  # ❌ Tentatives multiples
        ("bob", "encore_mauvais"),  # ❌ Compte bloqué
        ("bob", "password"),  # ❌ Compte toujours bloqué
    ]

    for nom, mdp in scenarios:
        try:
            resultat = auth.authentifier(nom, mdp)
            print(f"{nom}/{mdp}: {resultat}")
        except ErreurAuthentification as e:
            print(f"{nom}/{mdp}: ❌ {e}")


# exceptions_personnalisees()

# =============================================================================
# SECTION 7 : BONNES PRATIQUES
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 7 : BONNES PRATIQUES")
print("=" * 70)


def bonnes_pratiques():
    """
    Les bonnes pratiques de la gestion d'erreurs
    """
    print(
        """
📚 LES 10 COMMANDEMENTS DE LA GESTION D'ERREURS :

1. 🎯 Soyez SPÉCIFIQUE dans les except
2. ❌ N'utilisez PAS except: tout seul
3. 📝 Logguez les erreurs pour le débogage
4. 🎪 Ne masquez PAS les erreurs silencieusement
5. 🔧 Utilisez finally pour le nettoyage
6. 🏷️  Créez des exceptions personnalisées pour le métier
7. 📊 Fournissez des messages d'erreur UTILES
8. 🔄 Pensez à la REPRISE après erreur
9. 🎨 Utilisez l'encapsulation pour la gestion d'erreurs
10. 🧪 TESTEZ vos gestionnaires d'erreurs
    """
    )

    print("\n✅ CE QU'IL FAUT FAIRE")
    print("-" * 25)

    print(
        """
# ✅ BON - Gestion spécifique
try:
    nombre = int(entree_utilisateur)
except ValueError:
    print("Veuillez entrer un nombre valide")

# ✅ BON - Capture multiple
except (FileNotFoundError, PermissionError) as e:
    print(f"Problème de fichier: {e}")

# ✅ BON - Exception personnalisée
class ErreurMetier(Exception):
    pass
    """
    )

    print("\n❌ CE QU'IL NE FAUT PAS FAIRE")
    print("-" * 30)

    print(
        """
# ❌ MAUVAIS - Trop général
try:
    operation()
except:  # Capture TOUTES les erreurs
    pass  # Et les ignore !

# ❌ MAUVAIS - Message inutile
except Exception as e:
    print("Une erreur est survenue")  # Quel erreur ??

# ❌ MAUVAIS - Gestion silencieuse
except ValueError:
    pass  # L'utilisateur ne sait pas ce qui ne va pas
    """
    )

    print("\n🔧 EXEMPLE DE BONNE GESTION")
    print("-" * 30)

    def bon_exemple():
        """Exemple de bonne gestion d'erreurs"""
        import logging

        # Configuration du logging
        logging.basicConfig(level=logging.INFO)

        def charger_configuration(fichier_config):
            try:
                # Simulation de chargement
                if not fichier_config.endswith(".json"):
                    raise ValueError(
                        "Le fichier de configuration doit être au format JSON"
                    )

                if fichier_config == "config_corrompue.json":
                    raise IOError("Fichier corrompu")

                config = {"theme": "sombre", "langue": "fr"}
                logging.info(f"✅ Configuration chargée depuis {fichier_config}")
                return config

            except ValueError as e:
                logging.error(f"❌ Erreur de validation: {e}")
                # Retourne une configuration par défaut
                return {"theme": "clair", "langue": "fr"}

            except IOError as e:
                logging.error(f"❌ Erreur d'E/S: {e}")
                raise  # Relance l'exception pour que l'appelant sache

            except Exception as e:
                logging.error(f"❌ Erreur inattendue: {e}")
                raise
            finally:
                logging.info("🔧 Nettoyage des ressources de configuration")

        # Test
        try:
            config = charger_configuration("config.json")
            print(f"Configuration: {config}")
        except Exception as e:
            print(f"Échec du chargement: {e}")

    bon_exemple()


# bonnes_pratiques()

# =============================================================================
# SECTION 8 : EXEMPLE PRATIQUES
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 8 : EXEMPLE PRATIQUES")
print("=" * 70)


def exemples_pratiques():
    """
    exemples pour pratiquer la gestion d'erreurs
    """
    print(
        """
💪 EXEMPLE PRATIQUES :

1. 🎯 Gestion d'erreurs de base
2. 🔧 Exceptions personnalisées  
3. 🏗️  Système complet avec gestion d'erreurs
    """
    )

    print("\n🎯 EXERCICE 1 : CALCULATRICE ROBUSTE")
    print("-" * 35)

    class Calculatrice:
        """Calculatrice avec gestion complète des erreurs"""

        def __init__(self):
            self.historique = []

        def calculer(self, operation, a, b):
            try:
                if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                    raise TypeError("Les opérandes doivent être des nombres")

                if operation == "+":
                    resultat = a + b
                elif operation == "-":
                    resultat = a - b
                elif operation == "*":
                    resultat = a * b
                elif operation == "/":
                    if b == 0:
                        raise ZeroDivisionError("Division par zéro")
                    resultat = a / b
                elif operation == "**":
                    resultat = a**b
                else:
                    raise ValueError(f"Opération non supportée: {operation}")

                self.historique.append(f"{a} {operation} {b} = {resultat}")
                return resultat

            except (TypeError, ValueError, ZeroDivisionError) as e:
                self.historique.append(f"ERREUR: {a} {operation} {b} → {e}")
                raise
            except Exception as e:
                self.historique.append(f"ERREUR INATTENDUE: {e}")
                raise

        def afficher_historique(self):
            print("📋 Historique des calculs:")
            for calcul in self.historique[-5:]:
                print(f"  {calcul}")

    # Test de la calculatrice
    calc = Calculatrice()

    tests = [
        ("+", 10, 5),
        ("-", 10, 5),
        ("*", 10, 5),
        ("/", 10, 0),  # ❌ Division par zéro
        ("/", 10, 2),
        ("^", 10, 2),  # ❌ Opération invalide
        ("+", "10", 5),  # ❌ Type invalide
    ]

    for op, a, b in tests:
        try:
            resultat = calc.calculer(op, a, b)
            print(f"✅ {a} {op} {b} = {resultat}")
        except Exception as e:
            print(f"❌ {a} {op} {b} → {e}")

    calc.afficher_historique()

    print("\n🔧 EXERCICE 2 : SYSTÈME DE RÉSERVATION")
    print("-" * 35)

    class ErreurReservation(Exception):
        pass

    class DateInvalideError(ErreurReservation):
        pass

    class CapaciteDepasseeError(ErreurReservation):
        pass

    class SystemeReservation:
        def __init__(self, capacite_max=100):
            self.capacite_max = capacite_max
            self.reservations = []

        def reserver(self, nom, date, nombre_personnes):
            try:
                # Validation de la date
                if not self._date_valide(date):
                    raise DateInvalideError(f"Date invalide: {date}")

                # Validation du nombre de personnes
                if not isinstance(nombre_personnes, int) or nombre_personnes <= 0:
                    raise ValueError(
                        "Le nombre de personnes doit être un entier positif"
                    )

                # Vérification de la capacité
                total_reservations = sum(
                    r["nombre_personnes"] for r in self.reservations
                )
                if total_reservations + nombre_personnes > self.capacite_max:
                    raise CapaciteDepasseeError(
                        f"Capacité dépassée: {total_reservations + nombre_personnes}/{self.capacite_max}"
                    )

                # Création de la réservation
                reservation = {
                    "nom": nom,
                    "date": date,
                    "nombre_personnes": nombre_personnes,
                }
                self.reservations.append(reservation)

                return f"✅ Réservation confirmée pour {nom} le {date}"

            except (DateInvalideError, CapaciteDepasseeError, ValueError) as e:
                raise ErreurReservation(f"Échec de la réservation: {e}")

        def _date_valide(self, date):
            # Simulation simple de validation de date
            return isinstance(date, str) and len(date) == 10

    # Test du système de réservation
    reservation_system = SystemeReservation(capacite_max=50)

    scenarios_reservation = [
        ("Alice", "2024-01-15", 4),
        ("Bob", "2024-01-15", 45),  # ❌ Capacité dépassée
        ("Charlie", "date_invalide", 2),  # ❌ Date invalide
        ("David", "2024-01-16", -2),  # ❌ Nombre invalide
        ("Eve", "2024-01-15", 10),
    ]

    for nom, date, personnes in scenarios_reservation:
        try:
            resultat = reservation_system.reserver(nom, date, personnes)
            print(resultat)
        except ErreurReservation as e:
            print(f"❌ {e}")


# exemples_pratiques()

# =============================================================================
# SECTION 9 : OUTILS ET TECHNIQUES AVANCÉES
# =============================================================================

print("\n" + "=" * 70)
print("SECTION 9 : TECHNIQUES AVANCÉES")
print("=" * 70)


def techniques_avancees():
    """
    Techniques avancées de gestion d'erreurs
    """
    print(
        """
🚀 TECHNIQUES AVANCÉES :

1. 🔧 Context managers personnalisés
2. 🎭 Décorateurs de gestion d'erreurs
3. 📊 Logging structuré
4. 🔄 Retry automatique
    """
    )

    print("\n🔧 CONTEXT MANAGERS PERSONNALISÉS")
    print("-" * 35)

    class GestionnaireTransaction:
        """Context manager pour gérer les transactions avec rollback"""

        def __enter__(self):
            print("🚀 Début de la transaction")
            self.etat_initial = "sauvegardé"
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                # Une exception s'est produite → rollback
                print(f"🔙 Rollback à cause de: {exc_type.__name__}: {exc_val}")
                self.rollback()
            else:
                # Tout s'est bien passé → commit
                print("✅ Commit de la transaction")

            print("🔧 Fin de la transaction")
            return True  # Empêche la propagation de l'exception

        def rollback(self):
            print("↩️  Restauration de l'état initial")

    # Utilisation du context manager
    print("Scénario sans erreur:")
    with GestionnaireTransaction():
        print("   Exécution d'opérations...")
        resultat = 10 + 5
        print(f"   Résultat: {resultat}")

    print("\nScénario avec erreur:")
    with GestionnaireTransaction():
        print("   Exécution d'opérations...")
        resultat = 10 / 0  # ❌ Division par zéro
        print(f"   Résultat: {resultat}")  # Cette ligne ne sera pas exécutée

    print("\n🔄 DÉCORATEUR DE RETRY AUTOMATIQUE")
    print("-" * 35)

    def retry(max_tentatives=3, delai=1):
        """Décorateur pour réessayer automatiquement en cas d'échec"""
        import time

        def decorateur(fonction):
            def wrapper(*args, **kwargs):
                tentatives = 0
                while tentatives < max_tentatives:
                    try:
                        return fonction(*args, **kwargs)
                    except Exception as e:
                        tentatives += 1
                        if tentatives == max_tentatives:
                            print(f"❌ Échec après {max_tentatives} tentatives: {e}")
                            raise
                        else:
                            print(
                                f"🔄 Tentative {tentatives}/{max_tentatives} échouée: {e}"
                            )
                            time.sleep(delai)

            return wrapper

        return decorateur

    @retry(max_tentatives=3, delai=0.5)
    def appel_api_simule():
        """Simule un appel API qui peut échouer aléatoirement"""
        import random

        if random.random() < 0.7:  # 70% de chance d'échec
            raise ConnectionError("Échec de connexion à l'API")
        return "✅ Données reçues de l'API"

    # Test du décorateur de retry
    print("Test d'appel API avec retry automatique:")
    try:
        resultat = appel_api_simule()
        print(resultat)
    except Exception as e:
        print(f"Échec définitif: {e}")

    print("\n📊 LOGGING STRUCTURÉ")
    print("-" * 25)

    def setup_logging():
        """Configuration du logging structuré"""
        import logging
        import json

        class JSONFormatter(logging.Formatter):
            def format(self, record):
                log_entry = {
                    "timestamp": self.formatTime(record),
                    "level": record.levelname,
                    "message": record.getMessage(),
                    "module": record.module,
                    "function": record.funcName,
                }
                return json.dumps(log_entry)

        logger = logging.getLogger()
        handler = logging.StreamHandler()
        handler.setFormatter(JSONFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger

    # Exemple de logging structuré
    logger = setup_logging()

    def operation_risquee():
        try:
            # Simulation d'opération
            resultat = 10 / 2
            logger.info("Opération réussie", extra={"resultat": resultat})
            return resultat
        except Exception as e:
            logger.error("Échec de l'opération", extra={"erreur": str(e)})
            raise

    print("Logging structuré (format JSON):")
    operation_risquee()


# techniques_avancees()

# =============================================================================
# CONCLUSION
# =============================================================================

print("\n" + "=" * 70)
print("🎓 CONCLUSION - RÉCAPITULATIF")
print("=" * 70)

print(
    """
✅ CE QUE VOUS SAVEZ MAINTENANT :

1. 🎯 Identifier les différents types d'erreurs
2. 🛡️  Utiliser try/except/else/finally
3. 🚨 Lever des exceptions avec raise
4. 🎨 Créer des exceptions personnalisées
5. 📝 Appliquer les bonnes pratiques
6. 🔧 Utiliser des techniques avancées

🔮 PROCHAINES ÉTAPES :

1. 🧪 Pratiquer avec vos propres projets
2. 📚 Explorer la documentation officielle
3. 🔧 Étudier les gestionnaires de contexte
4. 🏗️  Implementer la gestion d'erreurs dans des applications réelles

📚 RESSOURCES UTILES :
• Documentation Python: https://docs.python.org/3/tutorial/errors.html
• Real Python: Gestion d'erreurs avancée
• PEP 8: Style guide pour Python

🎯 SOUVENez-VOUS :
« Une bonne gestion d'erreurs ne consiste pas à éviter les erreurs,
mais à les gérer avec élégance et à fournir une expérience utilisateur fluide. »
"""
)

# =============================================================================
# MENU PRINCIPAL
# =============================================================================


def afficher_menu():
    """Affiche le menu principal de la présentation"""
    print("\n" + "=" * 70)
    print("📚 MENU PRINCIPAL - GESTION D'ERREURS")
    print("=" * 70)
    print("1. 🎯 Introduction - Pourquoi gérer les erreurs ?")
    print("2. 🔍 Section 1 - Types d'erreurs")
    print("3. 🧱 Section 2 - Structure try/except")
    print("4. 🎯 Section 3 - Gestion multiple")
    print("5. 🔄 Section 4 - Else et Finally")
    print("6. 🚨 Section 5 - Lever des exceptions")
    print("7. 🎨 Section 6 - Exceptions personnalisées")
    print("8. 📚 Section 7 - Bonnes pratiques")
    print("9. 💪 Section 8 - exemples pratiques")
    print("10. 🚀 Section 9 - Techniques avancées")
    print("11. 🎓 Conclusion")
    print("12. 🧪 Tout exécuter")
    print("0. 🚪 Quitter")
    print("=" * 70)


def main():
    """Fonction principale avec menu interactif"""
    while True:
        afficher_menu()
        choix = input("\nChoisissez une section (0-12): ").strip()

        if choix == "0":
            print("👋 Au revoir ! Bonne continuation avec Python !")
            break
        elif choix == "1":
            print("\n" + "=" * 70)
            print("🎯 INTRODUCTION")
            print("=" * 70)
            # L'introduction est déjà affichée au début
        elif choix == "2":
            demonstration_erreurs()
        elif choix == "3":
            structure_de_base()
        elif choix == "4":
            gestion_multiple()
        elif choix == "5":
            else_et_finally()
        elif choix == "6":
            lever_exceptions()
        elif choix == "7":
            exceptions_personnalisees()
        elif choix == "8":
            bonnes_pratiques()
        elif choix == "9":
            exemples_pratiques()
        elif choix == "10":
            techniques_avancees()
        elif choix == "11":
            # Conclusion déjà affichée
            print("✅ Présentation terminée !")
        elif choix == "12":
            print("🧪 Exécution de toute la présentation...")
            demonstration_erreurs()
            structure_de_base()
            gestion_multiple()
            else_et_finally()
            lever_exceptions()
            exceptions_personnalisees()
            bonnes_pratiques()
            exemples_pratiques()
            techniques_avancees()
            print("✅ Toutes les sections ont été exécutées !")
        else:
            print("❌ Choix invalide ! Veuillez choisir entre 0 et 12.")

        if choix != "0":
            input("\nAppuyez sur Entrée pour continuer...")


# =============================================================================
# LANCEMENT
# =============================================================================

if __name__ == "__main__":
    print("🚀 PRÉSENTATION SUR LA GESTION D'ERREURS EN PYTHON")
    print("Décommentez main() pour le menu interactif ou les fonctions individuelles")

    # Décommentez la ligne suivante pour le menu interactif
    # main()

    print("\n💡 CONSEILS D'UTILISATION :")
    print("• Décommentez les fonctions une par une pour étudier")
    print("• Expérimentez avec le code")
    print("• Créez vos propres exemples")
    print("• Pratiquez avec vos projets personnels")
