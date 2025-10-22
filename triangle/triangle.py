def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b >= c

def equilateral(sides):
    return is_valid_triangle(sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    return is_valid_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])

def scalene(sides):
    return is_valid_triangle(sides) and len(set(sides)) == 3