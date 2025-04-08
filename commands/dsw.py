from commands.tree_creation import Tree_node

def rotate_right(grandparent, parent):
    child = parent.left
    if child is None:
        return

    parent.left = child.right
    if child.right:
        child.right.parent = parent

    child.right = parent
    child.parent = grandparent

    if grandparent:
        if grandparent.left == parent:
            grandparent.left = child
        else:
            grandparent.right = child
    parent.parent = child


def rotate_left(grandparent, parent):
    child = parent.right
    if child is None:
        return

    parent.right = child.left
    if child.left:
        child.left.parent = parent

    child.left = parent
    child.parent = grandparent

    if grandparent:
        if grandparent.left == parent:
            grandparent.left = child
        else:
            grandparent.right = child
    parent.parent = child


def create_vine(root):
    pseudo_root = Tree_node(None)
    pseudo_root.right = root
    root.parent = pseudo_root

    tail = pseudo_root
    rest = root

    while rest:
        if rest.left:
            rotate_right(tail, rest)
            rest = tail.right
        else:
            tail = rest
            rest = rest.right
    return pseudo_root

def count_nodes_in_vine(pseudo_root):
    count = 0
    current = pseudo_root.right
    while current:
        count += 1
        current = current.right
    return count

def compress(pseudo_root, count):
    scanner = pseudo_root
    for _ in range(count):
        child = scanner.right
        if child:
            rotate_left(scanner, child)
            scanner = scanner.right

def balance_vine(pseudo_root, size):
    import math
    m = 2 ** math.floor(math.log2(size + 1)) - 1
    compress(pseudo_root, size - m)
    while m > 1:
        m = m // 2
        compress(pseudo_root, m)

def dsw_balance(root):
    if not root: 
        return None

    pseudo_root = create_vine(root)
    size = count_nodes_in_vine(pseudo_root)
    balance_vine(pseudo_root, size)
    new_root = pseudo_root.right
    new_root.parent = None
    return new_root
