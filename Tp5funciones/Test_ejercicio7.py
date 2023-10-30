import pytest
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import max_and_min_value 
@pytest.mark.parametrize("num, res",[
    ([1,12,45,10,3,4,9,6],"el valor maximo es: 45 y el valor minimo es: 1" ),
    ([4,10,60],"el valor maximo es: 60 y el valor minimo es: 4"),
])
def test__max_and_min_value(num, res):
    assert max_and_min_value(num) == res