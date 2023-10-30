import pytest
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import multiple
@pytest.mark.parametrize("number,number2, res",[
    (4,5,"4 no es multiplo de 5" ),
    (10,5,"10 es multiplo de 5" ),
    

])
def test_multiple(number,number2 , res):
    assert multiple(number,number2) == res