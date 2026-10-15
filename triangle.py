def is_valid_triangle(a, b, c) -> bool:
    return a + b > c and a + c > b and b + c > a

def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    if a == b == c:
        
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

