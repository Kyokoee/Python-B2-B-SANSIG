class ErreurBibliotheque(Exception):
    pass


class ErreurFichierBibliotheque(ErreurBibliotheque):
    pass


class ErreurChargementJSON(ErreurBibliotheque):
    pass


class ErreurSauvegardeJSON(ErreurBibliotheque):
    pass


class ErreurExportCSV(ErreurBibliotheque):
    pass
