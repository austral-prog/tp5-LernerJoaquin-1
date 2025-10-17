import math


def roots(a, b, c):
    D = b*b - 4*a*c
    if D < 0:
        return "( )"
    elif D == 0:
        r = -b / (2*a)
        return f"({float(r)})"
    else:
        sqrtD = math.sqrt(D)
        r1 = (-b + sqrtD) / (2*a)
        r2 = (-b - sqrtD) / (2*a)
        r_hi, r_lo = (r1, r2) if r1 >= r2 else (r2, r1)
        return f"({float(r_hi)}, {float(r_lo)})"

def value_y(a, b, c, x):
    return a*(x**2) + b*x + c

def to_string(a, b, c):
    terms = []
    if a != 0:
        terms.append(f"{a} * X^2")
    if b != 0:
        terms.append(f"{b} * X")
    if c != 0 or not terms:  
        terms.append(f"{c}")
    body = " + ".join(terms)
    return f"f(x) = {body}"

def derivation(a, b, c):
    A = 2*a
    B = b
    if A != 0 and B != 0:
        return f"f'(x) = {A} * X + {B}"
    elif A != 0 and B == 0:
        return f"f'(x) = {A} * X"
    elif A == 0 and B != 0:
        return f"f'(x) = {B}"
    else:
        return "f'(x) = 0"
