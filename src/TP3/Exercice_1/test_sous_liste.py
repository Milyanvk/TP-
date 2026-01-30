import pytest
from .sous_liste import sous_liste

@pytest.mark.parametrize(
    "element, liste, depart, resultat_attendu",
    [
        ([1,3],[0,1,2,3,4],True),
        ([1,6],[0,1,2,3,4],False),
        ([3,2],[0,1,2,3,4],False),
    ],
)

def test_sous_liste(petite_liste,grande_liste,resultat_attendu):
    assert sous_liste(petite_liste,grande_liste)==resultat_attendu
