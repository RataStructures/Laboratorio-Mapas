from DataStructures.List import list_node as ln
from random import randint

# Funciones auxiliares
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación del módulo.


def get_first(my_list):
    first = my_list["first"]
    return first


def get_last(my_list):
    last = my_list["last"]
    return last


def update_size(my_list, size):
    my_list["size"] = size
    return my_list


def update_list(my_list, new_list):
    my_list = update_first(my_list, get_first(new_list))
    my_list = update_last(my_list, get_last(new_list))
    my_list = update_size(my_list, size(new_list))
    return my_list


def update_first(my_list, node):
    my_list["first"] = node
    return my_list


def update_last(my_list, node):
    my_list["last"] = node
    return my_list


def increment_size(my_list):
    my_list["size"] += 1
    return my_list


def decrease_size(my_list):
    my_list["size"] -= 1
    return my_list


def iterator_node(my_list, start, end, step):
    first_node = get_first(my_list)
    current_node = ln.get_node(first_node, start)
    index = start
    while current_node is not None and index < end:
        if index >= start and (index - start) % step == 0:
            yield current_node
        index += step
        current_node = ln.get_node(current_node, step)


# Función extra (no documentada en la API) que permite iterar sobre los elementos de la lista


def iterator(my_list, start, end, step):
    first_node = get_first(my_list)
    current_node = ln.get_node(first_node, start)
    index = start
    while current_node is not None and index < end:
        if index >= start and (index - start) % step == 0:
            current_value = ln.get_element(current_node)
            yield current_value
        index += step
        current_node = ln.get_node(current_node, step)


# Funciones principales de la API


def default_function(element_1, element_2):
    if element_1 == element_2:
        response = 0
    elif element_1 > element_2:
        response = 1
    else:
        response = -1
    return response


def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted


def new_list():
    first, last, size = None, None, 0
    my_list = {"first": first, "last": last, "size": size}
    return my_list


def is_empty(my_list):
    return my_list["size"] == 0


def size(my_list):
    return my_list["size"]


def add_first(my_list, element):
    node = ln.new_single_node(element)
    if is_empty(my_list):
        my_list = update_first(my_list, node)
        my_list = update_last(my_list, node)
    else:
        first_node = get_first(my_list)
        node = ln.update_next(node, first_node)
        my_list = update_first(my_list, node)
    my_list = increment_size(my_list)
    return my_list


def add_last(my_list, element):
    node = ln.new_single_node(element)
    if is_empty(my_list):
        my_list = update_first(my_list, node)
        my_list = update_last(my_list, node)
    else:
        last_node = get_last(my_list)
        last_node = ln.update_next(last_node, node)
        my_list = update_last(my_list, node)
    my_list = increment_size(my_list)
    return my_list


def first_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        first_node = get_first(my_list)
        first = ln.get_element(first_node)
    return first


def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        last_node = get_last(my_list)
        last = ln.get_element(last_node)
    return last


def get_element(my_list, pos):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        first_node = get_first(my_list)
        node = ln.get_node(first_node, pos)
        element = ln.get_element(node)
    return element


def delete_element(my_list, pos):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        if pos == 0:
            _ = remove_first(my_list)
        elif pos == n - 1:
            _ = remove_last(my_list)
        else:
            first_node = get_first(my_list)
            prev_node = ln.get_node(first_node, pos - 1)
            next_node = ln.get_node(first_node, pos + 1)
            prev_node = ln.update_next(prev_node, next_node)
            my_list = update_first(my_list, first_node)
            my_list = decrease_size(my_list)
    return my_list


def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        n = size(my_list)
        if n == 1:
            removed_element = first_element(my_list)
            my_list = update_first(my_list, None)
            my_list = update_last(my_list, None)
            my_list = decrease_size(my_list)
        else:
            first_node = get_first(my_list)
            removed_element = ln.get_element(first_node)
            next_node = ln.get_next(first_node)
            my_list = update_first(my_list, next_node)
            my_list = decrease_size(my_list)
    return removed_element


def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        n = size(my_list)
        if n == 1:
            removed_element = first_element(my_list)
            my_list = update_first(my_list, None)
            my_list = update_last(my_list, None)
            my_list = decrease_size(my_list)
        else:
            last_node = get_last(my_list)
            removed_element = ln.get_element(last_node)
            first_node = get_first(my_list)
            prev_node = ln.get_node(first_node, n - 2)
            prev_node = ln.update_next(prev_node, None)
            my_list = update_last(my_list, prev_node)
            my_list = decrease_size(my_list)
    return removed_element


def insert_element(my_list, element, pos):
    n = size(my_list)
    if pos < 0 or pos > n:
        raise Exception("IndexError: list index out of range")
    else:
        if pos == 0:
            my_list = add_first(my_list, element)
        elif pos == n:
            my_list = add_last(my_list, element)
        else:
            first = get_first(my_list)
            prev_node = ln.get_node(first, pos - 1)
            next_node = ln.get_node(first, pos)
            node = ln.new_single_node(element)
            prev_node = ln.update_next(prev_node, node)
            node = ln.update_next(node, next_node)
            my_list = update_first(my_list, first)
            my_list = increment_size(my_list)
    return my_list


def is_present(my_list, element, cmp_function):
    result, index, n = -1, 0, size(my_list)
    for current in iterator(my_list, 0, n, 1):
        are_equal = cmp_function(element, current) == 0
        if are_equal:
            result = index
            break
        index += 1
    return result


def change_info(my_list, pos, new_info):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        first_node = get_first(my_list)
        node = ln.get_node(first_node, pos)
        node = ln.update_info(node, new_info)
        my_list = update_first(my_list, first_node)
    return my_list


def exchange(my_list, pos_1, pos_2):
    n = size(my_list)
    if pos_1 < 0 or pos_1 >= n or pos_2 < 0 or pos_2 >= n:
        raise Exception("IndexError: list index out of range")
    else:
        first_node = get_first(my_list)
        node_1 = ln.get_node(first_node, pos_1)
        node_2 = ln.get_node(first_node, pos_2)
        info_1 = ln.get_element(node_1)
        info_2 = ln.get_element(node_2)
        node_1 = ln.update_info(node_1, info_2)
        node_2 = ln.update_info(node_2, info_1)
        my_list = update_first(my_list, first_node)
    return my_list


def sub_list(my_list, pos, num_elements):
    n = size(my_list)
    if pos < 0 or pos >= size(my_list) or num_elements < 0 or pos + num_elements > n:
        raise Exception("IndexError: list index out of range")
    else:
        sublist, index = new_list(), 0
        for current in iterator(my_list, 0, n, 1):
            if index >= pos and index < pos + num_elements:
                sublist = add_last(sublist, current)
            if index == pos + num_elements:
                break
            index += 1
    return sublist


# Funciones auxiliares para algoritmos de ordenamiento iterativos
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación de los algoritmos de ordenamiento.


def compute_init_gap(n):
    gap = 1
    while gap * 3 + 1 <= n // 3:
        gap = gap * 3 + 1
    return gap


def insertion_sort_with_gap(my_list, start_index, gap, sort_crit):
    n = size(my_list)
    need_sort = n > 1
    if need_sort:
        for index in range(start_index + gap, n, gap):
            continue_sorting = True
            while continue_sorting:
                current = get_element(my_list, index)
                previous = get_element(my_list, index - gap)
                swap = not sort_crit(previous, current)
                if swap:
                    my_list = exchange(my_list, index, index - gap)
                index -= gap
                continue_sorting = swap and index >= gap
    return my_list


# Algoritmos de ordenamiento iterativos
def selection_sort(my_list, sort_crit):
    n = size(my_list)
    need_sort = n > 1
    if need_sort:
        my_sort_list, continue_sorting = new_list(), True
        while continue_sorting:
            n, index = size(my_list), -1
            min, min_index = first_element(my_list), 0
            for element in iterator(my_list, 0, n, 1):
                index += 1
                update = sort_crit(element, min)
                if update:
                    min = element
                    min_index = index
            my_sort_list = add_last(my_sort_list, min)
            my_list = delete_element(my_list, min_index)
            continue_sorting = not is_empty(my_list)
        my_list = update_list(my_list, my_sort_list)
    return my_list


def insertion_sort(my_list, sort_crit):
    n = size(my_list)
    need_sort = n > 1
    if need_sort:
        my_sort_list, first_element = new_list(), remove_first(my_list)
        my_sort_list = add_first(my_sort_list, first_element)
        continue_sorting = True
        while continue_sorting:
            current = remove_first(my_list)
            index = -1
            for potential_node in iterator_node(my_sort_list, 0, size(my_sort_list), 1):
                index += 1
                potential = ln.get_element(potential_node)
                is_last = not ln.get_next(potential_node)
                if sort_crit(current, potential):
                    my_sort_list = insert_element(my_sort_list, current, index)
                    break
                elif is_last:
                    my_sort_list = add_last(my_sort_list, current)
            continue_sorting = not is_empty(my_list)
        my_list = update_list(my_list, my_sort_list)
    return my_list


def shell_sort(my_list, sort_crit):
    n = size(my_list)
    need_sort = n > 1
    if need_sort:
        gap = compute_init_gap(n)
        while gap > 0:
            for start_index in range(gap):
                my_list = insertion_sort_with_gap(my_list, start_index, gap, sort_crit)
            gap = (gap - 1) // 3
    return my_list


# Funciones auxiliares para algoritmos de ordenamiento recursivos
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación de los algoritmos de ordenamiento recursivos.


def merge(left, right, sort_crit):
    merged = new_list()
    run, is_empty_left, is_empty_right = True, False, False
    while run:
        if is_empty_right:
            left_element = remove_first(left)
            merged = add_last(merged, left_element)
        elif is_empty_left:
            right_element = remove_first(right)
            merged = add_last(merged, right_element)
        else:
            left_element = first_element(left)
            right_element = first_element(right)
            add_left = not sort_crit(right_element, left_element)
            if add_left:
                left_element = remove_first(left)
                merged = add_last(merged, left_element)

            else:
                right_element = remove_first(right)
                merged = add_last(merged, right_element)
        is_empty_right = is_empty(right)
        is_empty_left = is_empty(left)
        run = (not is_empty_left) or (not is_empty_right)
    return merged


def partition(my_list, sort_crit):
    n = size(my_list)
    pivot = first_element(my_list)
    less = new_list()
    greater = new_list()
    equal = new_list()
    for element in iterator(my_list, 0, n, 1):
        is_less = sort_crit(element, pivot)
        is_greater = sort_crit(pivot, element)
        if is_less:
            less = add_last(less, element)
        elif is_greater:
            greater = add_last(greater, element)
        else:
            equal = add_last(equal, element)
    return (
        less,
        equal,
        greater,
    )


def combine(less, equal, greater):
    my_list, n_l, n_e, n_g = new_list(), size(less), size(equal), size(greater)
    for element in iterator(less, 0, n_l, 1):
        my_list = add_last(my_list, element)
    for element in iterator(equal, 0, n_e, 1):
        my_list = add_last(my_list, element)
    for element in iterator(greater, 0, n_g, 1):
        my_list = add_last(my_list, element)
    return my_list


# Algoritmos de ordenamiento recursivos


def merge_sort(my_list, sort_crit):
    n = size(my_list)
    base_case = n <= 1
    if not base_case:
        left = sub_list(my_list, 0, n // 2)
        right = sub_list(my_list, n // 2, n - n // 2)
        sorted_left = merge_sort(left, sort_crit)
        sorted_right = merge_sort(right, sort_crit)
        my_list = merge(sorted_left, sorted_right, sort_crit)
    return my_list


def quick_sort(my_list, sort_crit):
    n = size(my_list)
    base_case = n <= 1
    if not base_case:
        (
            less,
            equal,
            greater,
        ) = partition(my_list, sort_crit)
        sorted_less = quick_sort(less, sort_crit)
        sorted_greater = quick_sort(greater, sort_crit)
        my_list = combine(sorted_less, equal, sorted_greater)
    return my_list
