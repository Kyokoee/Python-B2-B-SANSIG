import json
import csv
from models import Livre, LivreNumerique, Bibliotheque
from exceptions import (
    ErreurBibliotheque,
    ErreurFichierBibliotheque,
    ErreurChargementJSON,
    ErreurSauvegardeJSON,
    ErreurExportCSV,
)


class BibliothequeAvecFichier(Bibliotheque):
    def _encode_livre(self, livre):
        d = {
            "type": livre.__class__.__name__,
            "titre": livre.titre,
            "auteur": livre.auteur,
            "isbn": livre.isbn,
        }
        if isinstance(livre, LivreNumerique):
            d["taille_fichier"] = livre.taille_fichier
        return d

    def _to_dict(self):
        return {"nom": self.nom, "livres": [self._encode_livre(l) for l in self.livres]}

    @staticmethod
    def _decode_livre(item):
        typ = item.get("type", "Livre")
        if typ == "LivreNumerique":
            return LivreNumerique(
                item["titre"],
                item["auteur"],
                item["isbn"],
                item.get("taille_fichier", 0.0),
            )
        return Livre(item["titre"], item["auteur"], item["isbn"])

    @classmethod
    def _from_dict(cls, data):
        b = cls(data.get("nom", "SansNom"))
        for item in data.get("livres", []):
            b.ajouter_livre(cls._decode_livre(item))
        return b

    def save_json(self, path="catalogue.json"):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self._to_dict(), f, ensure_ascii=False, indent=2)
        except (OSError, TypeError, ValueError) as e:
            raise ErreurSauvegardeJSON(
                "Erreur lors de la sauvegarde JSON '{}': {}".format(path, e)
            ) from e

    @classmethod
    def load_json(cls, path="catalogue.json"):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise ErreurFichierBibliotheque(
                "Fichier JSON introuvable: '{}'".format(path)
            ) from e
        except json.JSONDecodeError as e:
            raise ErreurChargementJSON(
                "JSON invalide dans '{}': {}".format(path, e)
            ) from e
        except OSError as e:
            raise ErreurFichierBibliotheque(
                "Erreur d'accès au fichier '{}': {}".format(path, e)
            ) from e

        if not isinstance(data, dict) or "nom" not in data or "livres" not in data:
            raise ErreurChargementJSON(
                "Structure JSON invalide: champs 'nom' et 'livres' requis"
            )
        if not isinstance(data["livres"], list):
            raise ErreurChargementJSON("'livres' doit être une liste")

        return cls._from_dict(data)

    def export_csv(self, path="catalogue.csv"):
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["type", "titre", "auteur", "isbn", "taille_fichier"]
                )
                writer.writeheader()
                for l in self.livres:
                    row = self._encode_livre(l)
                    if "taille_fichier" not in row:
                        row["taille_fichier"] = ""
                    writer.writerow(row)
        except OSError as e:
            raise ErreurExportCSV(
                "Erreur lors de l'export CSV '{}': {}".format(path, e)
            ) from e
