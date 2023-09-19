from calculator import add
from calculator import Multiply
from calculator import Subtract
from calculator import div


def test_add():
    assert 4 == add(2,2)
    
def test_Multiply():
    assert 4 == Multiply(2,2)

def test_Subtract():
    assert 0 == Subtract(2,2)
    
def test_div():
    assert 1 == div(2,2)

