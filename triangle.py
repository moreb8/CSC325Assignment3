import math

def is_valid_triangle(a, b, c) -> bool:
    for s in (a, b, c):
        if isinstance(s, bool) or not isinstance(s, (int, float)) or not math.isfinite(s):
            return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        kind = "Equilateral"
    elif a == b or b == c or a == c:
        kind = "Isosceles"
    else:
        kind = "Scalene"

    x, y, z = sorted((a, b, c))
    if math.isclose(x * x + y * y, z * z, rel_tol=1e-9, abs_tol=1e-9):
        return f"Right {kind}"

    return kind


if __name__ == "__main__":
    tests = [
        ((3, 4, 5), "Right Scalene"),
        ((5, 5, 5), "Equilateral"),
        ((5, 5, 8), "Isosceles"),
        ((4, 5, 6), "Scalene"),
        ((1, 2, 3), "Invalid"),   # degenerate
        ((0, 4, 5), "Invalid"),   # non-positive side
        ((-1, 4, 5), "Invalid"),
        ((1, 1, math.sqrt(2)), "Right Isosceles"),
        ((0.3, 0.4, 0.5), "Right Scalene"),  # float tolerance
    ]
    for args, expected in tests:
        got = classify_triangle(*args)
        status = "ok" if got == expected else "FAIL"
        print(f"{status}: classify_triangle{args} -> {got!r} (expected {expected!r})")