import pytest
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import letter_spacing 
@pytest.mark.parametrize("sentence, res",[
    ("Hola, tú","H o l a , t ú "),
    ("chau","c h a u " ),
    

])
def test__letter_spacing(sentence, res):
    assert letter_spacing(sentence) == res