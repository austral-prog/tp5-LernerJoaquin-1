import math
def roots(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        r1 = ((-b + math.sqrt(discriminante)) / (2*a))
        r2 = ((-b - math.sqrt(discriminante)) / (2*a))
        print(f"({r1}, {r2})")
        return
    elif discriminante == 0:
        r3 = -b / (2*a)
        print(f"({r3})")
    else:
        return "( )"

            
    

def value_y(a, b, c, x):
    ecuacion = ((a*(x**2)) + b*x + c )
    print(ecuacion)


def to_string(a, b, c):
    print(f"f(x) = {a} * X^2 + {b} * X + {c}") 

    


def derivation(a, b, c):
    print(f"f'(x) = {2*a}x + {b}")
