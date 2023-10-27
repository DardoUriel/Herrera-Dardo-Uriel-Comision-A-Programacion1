from functions_bingo import *
import pytest

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
matrix_hor = [
    [1, 2, 3, 4, 5],
    ["x", "x", "x", "x", "x"],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
matrix_ver = [
    [1, "x", 3, 4, 5],
    [6, "x", 8, 9, 10],
    [11, "x", 13, 14, 15],
    [16, "x", 18, 19, 20],
    [21, "x", 23, 24, 25],
]
matrix_diag = [
    ["x", 2, 3, 4, 5],
    [6, "x", 8, 9, 10],
    [11, 12, "x", 14, 15],
    [16, 17, 18, "x", 20],
    [21, 22, 23, 24, "x"],
]


@pytest.mark.parametrize("a,res", [
    
    (matrix_hor, True)
    
    ])
def test_bingo(a, res):
    assert row_validator(a) == res
