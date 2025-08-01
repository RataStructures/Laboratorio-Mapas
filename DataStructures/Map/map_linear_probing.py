from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as al
from random import randint

# Funciones auxiliares
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación del módulo.


def next_hash_value_probing(hash_value, capacity):
    hash_value = (hash_value + 1) % capacity
    return hash_value


def new_empty_table(capacity):
    table = al.new_list()
    for _ in range(capacity):
        entry = me.new_map_entry(None, None)
        table = al.add_last(table, entry)
    return table


# Funciones principales de la API


def default_compare(key, entry):
    entry_key = me.get_key(entry)
    if key == entry_key:
        response = 0
    else:
        response = 1
    return response


def is_available(table, pos):
    entry = al.get_element(table, pos)
    key = me.get_key(entry)
    if key is None or key == "__EMPTY__":
        response = True
    else:
        response = False
    return response


def find_slot(my_map, key, hash_value):
    first_avail, stop, ocupied = None, False, False
    table, capacity = mf.get_table(my_map), mf.get_capacity(my_map)
    while not stop:
        entry = al.get_element(table, hash_value)
        available = is_available(table, hash_value)
        same_key = default_compare(key, entry) == 0
        stop = same_key or me.get_key(entry) is None
        ocupied = same_key
        if available:
            is_first_avail_empty = not first_avail
            if is_first_avail_empty:
                first_avail = hash_value
        elif same_key:
            first_avail = hash_value
        hash_value = next_hash_value_probing(hash_value, capacity)
    return ocupied, first_avail


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.init_capacity(num_elements, load_factor)
    table = dict()
    table["prime"] = prime
    table["capacity"] = capacity
    table["scale"] = randint(1, prime - 1)
    table["shift"] = randint(0, prime - 1)
    table["table"] = new_empty_table(capacity)
    table["current_factor"] = 0
    table["limit_factor"] = load_factor
    table["size"] = 0

    return table


def put(my_map, key, value):
    hash_value, table = mf.hash_value(my_map, key), mf.get_table(my_map)
    ocupied, first_avail = find_slot(my_map, key, hash_value)
    if ocupied:
        entry = al.get_element(table, first_avail)
        entry = me.set_value(entry, value)
        table = al.change_info(table, first_avail, entry)
        my_map = mf.update_table(my_map, table)
    else:
        my_map = mf.increment_size(my_map)
        my_map = mf.update_current_factor(my_map)
        current_factor = mf.get_current_factor(my_map)
        limit_factor = mf.get_limit_factor(my_map)
        if current_factor <= limit_factor:
            entry = me.new_map_entry(key, value)
            table = al.change_info(table, first_avail, entry)
            my_map = mf.update_table(my_map, table)
        else:
            my_map = mf.rehash(my_map)
            my_map = put(my_map, key, value)
    return my_map


def contains(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    ocupied, _ = find_slot(my_map, key, hash_value)
    return ocupied


def get(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    ocupied, first_avail = find_slot(my_map, key, hash_value)
    if ocupied:
        table = mf.get_table(my_map)
        entry = al.get_element(table, first_avail)
        value = me.get_value(entry)
    else:
        value = None
    return value


def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    ocupied, first_avail = find_slot(my_map, key, hash_value)
    if ocupied:
        table = mf.get_table(my_map)
        entry = al.get_element(table, first_avail)
        entry = me.set_key(entry, "__EMPTY__")
        entry = me.set_value(entry, "__EMPTY__")
        table = al.change_info(table, first_avail, entry)
        my_map = mf.update_table(my_map, table)
        my_map = mf.decrease_size(my_map)
        my_map = mf.update_current_factor(my_map)
    return my_map


def size(my_map):
    size = mf.get_size(my_map)
    return size


def is_empty(my_map):
    response = size(my_map) == 0
    return response


def key_set(my_map):
    table = mf.get_table(my_map)
    keys = al.new_list()
    for index in range(al.size(table)):
        is_not_empty = not is_available(table, index)
        if is_not_empty:
            entry = al.get_element(table, index)
            key = me.get_key(entry)
            keys = al.add_last(keys, key)
    return keys


def value_set(my_map):
    table = mf.get_table(my_map)
    values = al.new_list()
    for index in range(al.size(table)):
        is_not_empty = not is_available(table, index)
        if is_not_empty:
            entry = al.get_element(table, index)
            value = me.get_value(entry)
            values = al.add_last(values, value)
    return values


def rehash(my_map):
    old_table, old_capacity = mf.get_table(my_map), mf.get_capacity(my_map)
    old_size_table = al.size(old_table)
    new_capacity = mf.next_prime(2 * old_capacity)
    new_table = new_empty_table(new_capacity)
    new_size = 0
    my_map = mf.update_table(my_map, new_table)
    my_map = mf.update_capacity(my_map, new_capacity)
    my_map = mf.update_size(my_map, new_size)
    my_map = mf.update_current_factor(my_map)
    for index in range(old_size_table):
        is_not_empty = not is_available(old_table, index)
        if is_not_empty:
            element = al.get_element(old_table, index)
            key = me.get_key(element)
            value = me.get_value(element)
            my_map = put(my_map, key, value)
    return my_map
