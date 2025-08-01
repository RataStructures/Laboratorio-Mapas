from math import sqrt

# Funciones auxiliares
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación del módulo.


def get_table(my_map):
    table = my_map["table"]
    return table


def update_size(my_map, size):
    my_map["size"] = size
    return my_map


def get_capacity(my_map):
    capacity = my_map["capacity"]
    return capacity


def update_capacity(my_map, capacity):
    my_map["capacity"] = capacity
    return my_map


def init_capacity(num_elements, load_factor):
    capacity_no_prime = num_elements / load_factor
    capacity_prime = next_prime(capacity_no_prime)
    return capacity_prime


def get_size(my_map):
    size = my_map["size"]
    return size


def get_current_factor(my_map):
    current_factor = my_map["current_factor"]
    return current_factor


def get_limit_factor(my_map):
    limit_factor = my_map["limit_factor"]
    return limit_factor


def increment_size(my_map):
    my_map["size"] += 1
    return my_map


def decrease_size(my_map):
    my_map["size"] -= 1
    return my_map


def update_table(my_map, table):
    my_map["table"] = table
    return my_map


def update_current_factor(my_map):
    n = get_size(my_map)
    capacity = get_capacity(my_map)
    current_factor = n / capacity
    my_map["current_factor"] = current_factor
    return my_map


# Funciones principales de la API


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(sqrt(n) + 1), 6):
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
