from DataStructures.List import single_linked_list as sl


def iterator(my_stack, start, end, step):
    iterator = sl.iterator(my_stack, start, end, step)
    return iterator


def new_stack():
    stack = sl.new_list()
    return stack


def push(my_stack, element):
    my_stack = sl.add_first(my_stack, element)
    return my_stack


def pop(my_stack):
    if is_empty(my_stack):
        raise Exception("EmptyStructureError: stack is empty")
    else:
        pop = sl.first_element(my_stack)
        my_stack = sl.remove_first(my_stack)
    return pop


def is_empty(my_stack):
    is_empty = sl.is_empty(my_stack)
    return is_empty


def top(my_stack):
    if is_empty(my_stack):
        raise Exception("EmptyStructureError: stack is empty")
    else:
        top = sl.first_element(my_stack)
    return top


def size(my_stack):
    size = sl.size(my_stack)
    return size
