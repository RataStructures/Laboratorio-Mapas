from DataStructures.List import single_linked_list as sl


def new_queue():
    queue = sl.new_list()
    return queue


def enqueue(my_queue, element):
    my_queue = sl.add_last(my_queue, element)
    return my_queue


def dequeue(my_queue):
    if is_empty(my_queue):
        raise Exception("EmptyStructureError: queue is empty")
    else:
        peek = sl.first_element(my_queue)
        my_queue = sl.remove_first(my_queue)
    return peek


def is_empty(my_queue):
    is_empty = sl.is_empty(my_queue)
    return is_empty


def peek(my_queue):
    if is_empty(my_queue):
        raise Exception("EmptyStructureError: queue is empty")
    else:
        peek = sl.first_element(my_queue)
    return peek


def size(my_queue):
    size = sl.size(my_queue)
    return size
