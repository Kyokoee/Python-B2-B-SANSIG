from tp_jour_3 import Livre, Bibliotheque
import pytest


@pytest.fixture
def biblio():
    return Bibliotheque("Test")


@pytest.fixture
def livre():
    return Livre("Le Petit Prince", "Antoine de St-Exupery", "978-0156013987")
