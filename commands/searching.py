def find_min(node):
    if not node:
        print("The given tree is empty. Can't find min node.\nAborting...")
        return None
    current_node = node
    while current_node.left:
        current_node = current_node.left
    return current_node

def find_max(node):
    if not node:
        print("The given tree is empty. Can't find max node.\nAborting...")
        return None
    current_node = node
    while current_node.right:
        current_node = current_node.right
    return current_node

def find_min_max(node):
    print(f"Min: {find_min(node).value}")
    print(f"Max: {find_max(node).value}")

def find(root, target):
    current_node=root
    while True:
        if current_node.value==target:
            return current_node
        if target > current_node.value:
            if current_node.right: current_node=current_node.right
            else:
                print(f"Couldn't find node {target}")
                return 0
        if target < current_node.value:
            if current_node.left: current_node=current_node.left
            else:
                print(f"Couldn't find node {target}")
                return 0