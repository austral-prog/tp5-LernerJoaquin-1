def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x > y:
        print(x)
        return
    elif y > x:
        print(y)
        return
    else:
        print(x)
        return

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x > y and x > z:
        print(x)
        return
    elif y > x  and y > z:
        print(y)
    else:
        print(z)
        return
