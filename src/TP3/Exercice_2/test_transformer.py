pip3 install pytest
import pytest
from .transformer import transformer

def f(x):
    return x**2

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
