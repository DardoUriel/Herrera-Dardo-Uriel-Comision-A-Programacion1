import pytest
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import sumar_digitos
@pytest.mark.parametrize("num, res",[
    (10, 1),
    (38, 11),
])
def test_sumar_digitos (num ,res):
    assert sumar_digitos(num)==res