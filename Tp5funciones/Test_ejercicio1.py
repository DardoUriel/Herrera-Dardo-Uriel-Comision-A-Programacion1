import pytest
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import number_dni_validate
@pytest.mark.parametrize("num, res",[
    ("45718024", True),
    ("457180242", False),
    

])
def test__number_dni_validate(num ,res):
    assert number_dni_validate(num)==res