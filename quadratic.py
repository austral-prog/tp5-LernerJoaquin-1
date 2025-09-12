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
    terms = []
    if a != 0:
        terms.append(f"{a} * X^2")
    if b != 0:
        terms.append(f"{b} * X")
    if c != 0 or not terms:  # si todos son 0 → "f(x) = 0"
        terms.append(f"{c}")
    return "f(x) = " + " + ".join(terms)

def derivation(a, b, c):
    terms = []
    if 2*a != 0:
        terms.append(f"{2*a} * X")
    if b != 0 or not terms:  # si derivada = 0 → "f'(x) = 0"
        terms.append(f"{b}")
    return "f'(x) = " + " + ".join(terms)
