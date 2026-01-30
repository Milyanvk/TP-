def position(elt, liste, depart):
        for i in range(depart,len(liste)):
            if liste[i]==elt:
                return i
    return -1

import pytest
from .position import position

@pytest.mark.parametrize(
    "element, liste, depart, resultat_attendu",
    [
        (1,[1,2,3],0,0),
        (2,[1,2,3],2,-1),
        (5,[1,2,3],0,-1)
    ]
)

def test_resultat_position(element,liste,depart,resultat_attendu):

    