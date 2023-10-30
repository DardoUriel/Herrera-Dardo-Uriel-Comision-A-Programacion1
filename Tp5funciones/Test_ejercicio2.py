import pytest
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import access_last_word
@pytest.mark.parametrize("word, res",[
    ("Hola papu", "papu"),
    ("Im uriel herrera ", "herrera"),
    

])
def test_access_last_word(word , res):
    assert access_last_word(word) == res