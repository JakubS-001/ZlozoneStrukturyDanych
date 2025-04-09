import sys
from commands.searching import find, find_max

def remove_single(root, target):
    parent = target.parent
    children=[]
    if target.left: children.append(target.left)
    if target.right: children.append(target.right)

    if len(children)==0:
        if parent==None: 
            root=None
            return root
        if parent.left == target: parent.left = None
        elif parent.right == target: parent.right=None
        return root
    
    elif len(children)==1: 
        if parent==None:
            root=children[0]
            children[0].parent=None
            return root
        children[0].parent=parent
        if parent.left == target: parent.left = children[0]
        elif parent.right == target: parent.right=children[0]
        return root
    
    #Taking the left in in-order as a substitute
    substitute = find_max(target.left)
    substitute_value = substitute.value
    remove_single(root, substitute)
    target.value = substitute_value
    return root
    
def mass_removal(root):

    while True:
        try:
            print("nodes> ", end="")
            target_number = int(input()) 
            if not sys.stdin.isatty():
                print(target_number)
            if target_number <= 0:
                print("The number of nodes must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of nodes.")
    
    while True:
        try:
            print("delete> ", end="")
            targets_str = input().split()
            targets = list(map(int, targets_str))
            if not sys.stdin.isatty():
                print(" ".join(targets_str))
            if len(targets) != target_number:
                print(f"Please enter exactly {target_number} node values.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter only integers for node values.")
    
    for node_value in targets: # Checking if the values are integers, just to be sure
        if not isinstance(node_value, int):
            print(f"Invalid node value: {node_value}. Please enter integers only.")
            return
    print("Data inserted successfully")

    for target_value in targets:
        target=find(root, target_value)
        if target==0: return root
        root = remove_single(root, target)
        
    return root

def initiate_remove_all(root):
    root = remove_all(root, root)
    print("Tree removed successfully.")
    return root

def remove_all(root, current_node):
    if current_node:
        remove_all(root, current_node.left)
        remove_all(root, current_node.right)
        root = remove_single(root, current_node)