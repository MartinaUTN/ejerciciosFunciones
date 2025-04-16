def operaciones(a, b):
    def sumar(x, y):
        return x + y

    def restar(x, y):
        return x - y

    def multiplicar(x, y):
        return x * y

    suma = sumar(a, b)
    resta = restar(a, b)
    producto = multiplicar(a, b)

    return suma, resta, producto


s, r, p = operaciones(10, 4)
print(f"Suma: {s}, Resta: {r}, Multiplicar {p}")

#📌 Observación: sumar, restar y multiplicar están definidas dentro de operaciones y no existen fuera de ella.