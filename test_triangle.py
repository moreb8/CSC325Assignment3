import math
import pytest

from triangle import classify_triangle, is_valid_triangle

@pytest.mark.parametrize("sides", [(0, 4, 5), (3, 0, 5), (3, 4, 0), (-1, 4, 5), (-3, -4, -5)])
def test_non_positive_side_is_invalid(sides):
    assert is_valid_triangle(*sides) is False
    assert classify_triangle(*sides) == "Invalid"

def test_triangle_inequality_violation_is_invalid():
    assert is_valid_triangle(1, 2, 10) is False
    assert classify_triangle(1, 2, 10) == "Invalid"
    assert classify_triangle(10, 1, 2) == "Invalid" 

@pytest.mark.parametrize("sides", [(1, 2, 3), (3, 1, 2), (2, 3, 1), (5, 5, 10)])
def test_degenerate_triangle_is_invalid(sides):
    assert is_valid_triangle(*sides) is False
    assert classify_triangle(*sides) == "Invalid"

def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(0.5, 0.5, 0.5) == "Equilateral"

@pytest.mark.parametrize("sides", [(5, 5, 8), (5, 8, 5), (8, 5, 5)])
def test_isosceles(sides):
    assert classify_triangle(*sides) == "Isosceles"

def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"

@pytest.mark.parametrize("sides", [(3, 4, 5), (5, 4, 3), (5, 12, 13)])
def test_right_scalene_integer_sides(sides):
    assert classify_triangle(*sides) == "Right Scalene"

def test_right_isosceles_non_integer_hypotenuse():
    hyp = 5 * math.sqrt(2)
    assert hyp * hyp != 50 
    assert classify_triangle(5, 5, hyp) == "Right Isosceles"
    assert classify_triangle(hyp, 5, 5) == "Right Isosceles"


def test_not_right_when_clearly_off():
    assert classify_triangle(3, 4, 5.1) == "Scalene"