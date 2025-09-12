import math

def roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2*a)
        r2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"

def value_y(a, b, c, x):
    return a * x**2 + b * x + c

def to_string(a, b, c):
    return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    return f"f'(x) = {2*a}x + {b}"
