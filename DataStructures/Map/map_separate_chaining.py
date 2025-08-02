from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from random import randint

# Funciones auxiliares
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación del módulo.


def new_empty_table(capacity):
    table = al.new_list()
    elements = [sl.new_list() for _ in range(capacity)]
    table = al.update_list(table, elements)
    return table


# Funciones principales de la API


def default_compare(key, entry):
    entry_key = me.get_key(entry)
    if key == entry_key:
        response = 0
    else:
        response = 1
    return response


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
    bucket = al.get_element(table, hash_value)
    bucket_size = sl.size(bucket)
    found = False
    for index in range(bucket_size):
        entry = sl.get_element(bucket, index)
        same_key = default_compare(key, entry) == 0
        if same_key:
            entry = me.set_value(entry, value)
            bucket = sl.change_info(bucket, index, entry)
            table = al.change_info(table, hash_value, bucket)
            my_map = mf.update_table(my_map, table)
            found = True
            break
    if not found:
        my_map = mf.increment_size(my_map)
        my_map = mf.update_current_factor(my_map)
        current_factor = mf.get_current_factor(my_map)
        limit_factor = mf.get_limit_factor(my_map)
        if current_factor <= limit_factor:
            entry = me.new_map_entry(key, value)
            bucket = sl.add_last(bucket, entry)
            table = al.change_info(table, hash_value, bucket)
            my_map = mf.update_table(my_map, table)
        else:
            my_map = rehash(my_map)
            my_map = put(my_map, key, value)

    return my_map


def contains(my_map, key):
    response = False
    hash_value = mf.hash_value(my_map, key)
    table = mf.get_table(my_map)
    bucket = al.get_element(table, hash_value)
    bucket_size = sl.size(bucket)
    for entry in sl.iterator(bucket, 0, bucket_size, 1):
        entry_key = me.get_key(entry)
        if entry_key == key:
            response = True
            break
    return response


def get(my_map, key):
    value = None
    hash_value = mf.hash_value(my_map, key)
    table = mf.get_table(my_map)
    bucket = al.get_element(table, hash_value)
    bucket_size = sl.size(bucket)
    for entry in sl.iterator(bucket, 0, bucket_size, 1):
        entry_key = me.get_key(entry)
        if entry_key == key:
            value = me.get_value(entry)
            break
    return value


def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    table = mf.get_table(my_map)
    bucket = al.get_element(table, hash_value)
    bucket_size = sl.size(bucket)
    for index in range(bucket_size):
        entry = sl.get_element(bucket, index)
        same_key = default_compare(key, entry) == 0
        if same_key:
            bucket = sl.delete_element(bucket, index)
            table = al.change_info(table, hash_value, bucket)
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
    table_size = al.size(table)
    for bucket in al.iterator(table, 0, table_size, 1):
        if not sl.is_empty(bucket):
            bucket_size = sl.size(bucket)
            for entry in sl.iterator(bucket, 0, bucket_size, 1):
                key = me.get_key(entry)
                keys = al.add_last(keys, key)
    return keys


def value_set(my_map):
    table = mf.get_table(my_map)
    values = al.new_list()
    table_size = al.size(table)
    for bucket in al.iterator(table, 0, table_size, 1):
        if not sl.is_empty(bucket):
            bucket_size = sl.size(bucket)
            for entry in sl.iterator(bucket, 0, bucket_size, 1):
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
    for bucket in al.iterator(old_table, 0, old_size_table, 1):
        size_bucket = sl.size(bucket)
        for entry in sl.iterator(bucket, 0, size_bucket, 1):
            key = me.get_key(entry)
            value = me.get_value(entry)
            my_map = put(my_map, key, value)
    return my_map
