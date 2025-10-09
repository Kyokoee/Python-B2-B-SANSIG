class BankAccount:
    def __init__(self, titulaire: str, solde_initial: float = 0):
        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif.")
        self.titulaire = titulaire
        self.solde = solde_initial
        pass

    def deposer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.solde += montant
        return self.solde
        pass

    def retirer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        if montant > self.solde:
            raise ValueError("Fonds insuiffisants")
        self.solde -= montant
        return self.solde
        pass

    def __str__(self):
        return f"Compte de {self.titulaire}, solde : {self.solde:.2f} €"


if __name__ == "__main__":
    compte = BankAccount("Clement", 500)
    print(compte)
    compte.deposer(50)
    print(compte)
    compte.retirer(100)
    print(compte)
