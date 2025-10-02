class Vehicule:
    def __init__(self, marque: str, modele: str):
        self.marque = marque
        self.modele = modele

    def demarrer(self):
        return f"{self.marque} {self.modele} démarre."

    def __str__(self):
        return f"Vehicule : {self.marque} {self.modele}"


class Voiture(Vehicule):
    def __init__(self, marque: str, modele: str, nb_portes: int):
        super().__init__(marque, modele)
        self.nb_portes = nb_portes

    def __str__(self):
        return f"Voiture : {self.marque} {self.modele}, {self.nb_portes} portes"


class Moto(Vehicule):
    def __init__(self, marque: str, modele: str, type_moteur: str):
        super().__init__(marque, modele)
        self.type_moteur = type_moteur

    def __str__(self):
        return f"Moto : {self.marque} {self.modele}, moteur {self.type_moteur}"


if __name__ == "__main__":
    vehicule = Vehicule("Generique", "Modele")
    print(vehicule)
    print(vehicule.demarrer())

    voiture = Voiture("Peugeot", "2008", 5)
    print(voiture)
    print(voiture.demarrer())

    moto = Moto("Yamaha", "R6", "4-temps")
    print(moto)
    print(moto.demarrer())
