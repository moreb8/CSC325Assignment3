import math
import pytest

from triangle import is_valid_triangle, classify_triangle

def test_invalid_side_non_positive():
    assert is_valid_triangle(-1, 2, 3) == False
    assert classify_triangle(-1, 2, 3) == "Invalid"

def test_invalid_triangle_inequality():
    assert is_valid_triangle(1, 2, 3) == False
    assert classify_triangle(1, 2, 3) == "Invalid"

def test_degenerate_boundary_case():
    assert is_valid_triangle(1, 2, 3) == False
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 2) == "Isosceles"
    assert classify_triangle(3, 2, 3) == "Isosceles"
    assert classify_triangle(2, 3, 3) == "Isosceles"

def test_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene"
    assert classify_triangle(5, 4, 3) == "Scalene"
    assert classify_triangle(4, 5, 3) == "Scalene"




