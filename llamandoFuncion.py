def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def todas_las_operaciones(x, y):
    s = sumar(x, y)
    r = restar(x, y)
    m = multiplicar(x, y)
    return s, r, m

resultado = todas_las_operaciones(10, 4)
print(resultado) 
