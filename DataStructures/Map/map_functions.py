import math

# Funciones principales de la API


def is_prime(n):
    """Valida si un número es primo o no

    :param n: Número a validar
    :type n: int

    :return: True si es primo, False en caso contrario
    """
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def next_prime(n):
    found = False
    next_p = 1
    if n <= 1:
        next_p = 2
        found = True
    if found is False:
        next_p = int(n)
        while not found:
            next_p = next_p + 1
            if is_prime(next_p):
                found = True
    return int(next_p)


def hash_value(table, key):
    h = hash(key)
    a = table["scale"]
    b = table["shift"]
    p = table["prime"]
    m = table["capacity"]

    value = int((abs(a * h + b) % p) % m)
    return value
