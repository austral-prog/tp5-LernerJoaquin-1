def max_of_two(x, y):
    if x >= y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    return max_of_two(max_of_two(x, y), z)
