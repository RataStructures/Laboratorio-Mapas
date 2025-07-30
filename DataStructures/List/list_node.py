# Funciones extras (no documentada en la API)


def update_next(node, next):
    node["next"] = next
    return node


def update_info(node, info):
    node["info"] = info
    return node


def get_node(node, pos):
    current = node
    for _ in range(pos):
        if current is not None:
            current = current["next"]
    return current


# Funciones principales de la API


def new_single_node(element):
    node = {"info": element, "next": None}
    return node


def get_element(node):
    element = node["info"]
    return element


def get_next(node):
    next = node["next"]
    return next
