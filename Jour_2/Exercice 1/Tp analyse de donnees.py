etudiants = [
    {"nom": "Alice", "note": 15, "annee": 2},
    {"nom": "Bob", "note": 12, "annee": 1},
    {"nom": "Charlie", "note": 18, "annee": 2},
    {"nom": "Toto", "note": 0, "annee": 1},
    {"nom": "Ethan", "note": 8, "annee": 2},
    {"nom": "Mathis", "note": 11, "annee": 2},
]

admis = [e for e in etudiants if e["note"] >= 12]
nonadmis = list(filter(lambda e: e["note"] < 12, etudiants))

print("Étudiants admis :", [e["nom"] for e in admis])
print("Étudiants non admis :", [e["nom"] for e in nonadmis])

annees = {e["annee"] for e in etudiants}

moy = lambda xs: (sum(xs) / len(xs)) if xs else 0.0

moyennes_par_annee = {
    an: moy([e["note"] for e in etudiants if e["annee"] == an]) for an in annees
}
print("Moyennes par année :", moyennes_par_annee)

mention = lambda n: (
    "Très bien"
    if n >= 16
    else "Bien"
    if n >= 14
    else "Assez bien"
    if n >= 12
    else "Gros looser"
)

mentions = {e["nom"]: m for e in etudiants for m in [mention(e["note"])]}

print("Mentions :", mentions)

notes_admis = {e["nom"]: e["note"] for e in etudiants if e["note"] >= 12}
print("Notes des admis :", notes_admis)
