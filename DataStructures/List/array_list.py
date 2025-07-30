from random import randint

# Funciones auxiliares
# Estas funciones NO son parte de la API y NO deben ser utilizadas directamente.
# Son funciones auxiliares internas para la implementación del módulo.


def update_list(my_list, elements):
    size = len(elements)
    my_list["elements"] = elements
    my_list["size"] = size
    return my_list


def get_elements(my_list):
    elements = my_list["elements"]
    return elements


# Función extra (no documentada en la API) que permite iterar sobre los elementos de la lista


def iterator(my_list, start, end, step):
    for index in range(start, end, step):
        yield get_element(my_list, index)


# Funciones principales de la API


def default_sort_criteria(element_1, element_2):
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted


def default_function(element_1, element_2):
    if element_1 == element_2:
        response = 0
    elif element_1 > element_2:
        response = 1
    else:
        response = -1
    return response


def new_list():
    elements = []
    size = 0
    my_list = {"elements": elements, "size": size}
    return my_list


def add_first(my_list, element):
    elements = get_elements(my_list)
    elements.insert(0, element)
    my_list = update_list(my_list, elements)
    return my_list


def add_last(my_list, element):
    elements = get_elements(my_list)
    elements.append(element)
    my_list = update_list(my_list, elements)
    return my_list


def is_empty(my_list):
    is_empty = size(my_list) == 0
    return is_empty


def size(my_list):
    size = my_list["size"]
    return size


def first_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        first = elements[0]
    return first


def last_element(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        last = elements[-1]
    return last


def get_element(my_list, pos):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        element = elements[pos]
    return element


def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        first = elements.pop(0)
        my_list = update_list(my_list, elements)
    return first


def remove_last(my_list):
    if is_empty(my_list):
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        last = elements.pop()
        my_list = update_list(my_list, elements)
    return last


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
            elements = get_elements(my_list)
            elements.insert(pos, element)
            my_list = update_list(my_list, elements)
    return my_list


def is_present(my_list, element, cmp_function):
    result, n = -1, size(my_list)
    for index in range(n):
        current = get_element(my_list, index)
        are_equal = cmp_function(element, current) == 0
        if are_equal:
            result = index
            break
    return result


def delete_element(my_list, pos):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        del elements[pos]
        my_list = update_list(my_list, elements)
    return my_list


def change_info(my_list, pos, new_info):
    n = size(my_list)
    if pos < 0 or pos >= n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        elements[pos] = new_info
        my_list = update_list(my_list, elements)
    return my_list


def exchange(my_list, pos_1, pos_2):
    n = size(my_list)
    if pos_1 < 0 or pos_1 >= n or pos_2 < 0 or pos_2 >= n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        elements[pos_1], elements[pos_2] = elements[pos_2], elements[pos_1]
        my_list = update_list(my_list, elements)
    return my_list


def sub_list(my_list, pos_i, num_elements):
    n = size(my_list)
    if pos_i < 0 or pos_i >= n or num_elements < 0 or pos_i + num_elements > n:
        raise Exception("IndexError: list index out of range")
    else:
        elements = get_elements(my_list)
        sub_elements = elements[pos_i : pos_i + num_elements]
        my_sub_list = new_list()
        my_sub_list = update_list(my_sub_list, sub_elements)
    return my_sub_list


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
        for index in range(n):
            min_index = index
            min = get_element(my_list, min_index)
            for potential_index in range(index + 1, n):
                potential = get_element(my_list, potential_index)
                update = sort_crit(potential, min)
                if update:
                    min_index = potential_index
                    min = get_element(my_list, min_index)
            swap = min_index != index
            if swap:
                my_list = exchange(my_list, index, min_index)
    return my_list


def insertion_sort(my_list, sort_crit):
    n = size(my_list)
    need_sort = n > 1
    if need_sort:
        for index in range(1, n):
            continue_sorting = True
            while continue_sorting:
                current = get_element(my_list, index)
                previous = get_element(my_list, index - 1)
                swap = not sort_crit(previous, current)
                if swap:
                    my_list = exchange(my_list, index, index - 1)
                index -= 1
                continue_sorting = swap and index >= 1
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
    n_left, n_right = size(left), size(right)
    left_index, right_index = 0, 0
    run, left_full, right_full = True, False, False
    while run:
        if left_full:
            right_element = get_element(right, right_index)
            merged = add_last(merged, right_element)
            right_index += 1
        elif right_full:
            left_element = get_element(left, left_index)
            merged = add_last(merged, left_element)
            left_index += 1
        else:
            left_element = get_element(left, left_index)
            right_element = get_element(right, right_index)
            add_left = not sort_crit(right_element, left_element)
            if add_left:
                merged = add_last(merged, left_element)
                left_index += 1
            else:
                merged = add_last(merged, right_element)
                right_index += 1
        left_full = left_index == n_left
        right_full = right_index == n_right
        run = (not left_full) or (not right_full)
    return merged


def partition(my_list, sort_crit):
    n = size(my_list)
    pivot_index = randint(0, n - 1)
    pivot = get_element(my_list, pivot_index)
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


def combine(my_list, less, equal, greater):
    less_elements = get_elements(less)
    equal_elements = get_elements(equal)
    greater_elements = get_elements(greater)
    combine_elements = less_elements + equal_elements + greater_elements
    my_list = update_list(my_list, combine_elements)
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
        my_list = combine(my_list, sorted_less, equal, sorted_greater)
    return my_list
