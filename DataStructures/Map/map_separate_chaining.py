from DataStructures.Map import map_functions as mf
from random import randint

def new_map(num_elements, load_factor, prime = 109345121):
    capacity = mf.new_capacity(num_elements, load_factor)
    my_table = dict()
    my_table['prime'] = prime
    my_table['capacity'] = capacity
    my_table['scale'] = randint(1, prime-1)
    my_table['shift'] = randint(0, prime-1)
    my_table['table'] = mf.new_table(capacity)
    my_table['current_factor'] = 0
    my_table['limit_factor'] = load_factor
    my_table['size'] = 0

    return my_table