import pytest
from .cumuler import cumulerr

def g(x,y):
    return x*y

@pytest.mark.parametrize(
    "fonction, liste, resultat_attendu",
    [
        f,([1,2,3],[1,4,9]),
        (lambda x:x**2,[1,2,3],[1,4,0]),
        (str,[1,2,3],["1","2","3"]),
    ],
)


def test_transformer(fonction,liste,resultat_attendu):
    assert transformer(fonction,liste)==resultat_attendu
