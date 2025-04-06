class Tree_node:
    def __init__(self, value=None, parent=None):
        self.parent = None
        self.right = None
        self.left = None
        self.value = value
    
    def add_child(self, child, position):
        if position == 'left':
            self.left = child
        elif position == 'right':
            self.right = child
        else:
            print("Invalid position. Use 'left' or 'right' to add a child.")
    
    def __str__(self):
        return f"Tree(value={self.value}, left={self.left}, right={self.right})"

def create_tree(tree_type):
    global nodes_values

    print(f"Creating a {tree_type} tree...")
    print("nodes> ", end="")
    nodes_number = int(input())
    print("insert> ", end="")
    nodes_values = list(map(int, input().split(',')))
    print("Data inserted successfully.")

    for node_value in nodes_values: # Checking if the values are integers, just to be sure
        if not isinstance(node_value, int):
            print(f"Invalid node value: {node_value}. Please enter integers only.")
            return

    def create_avl_tree():
        global root
        nodes_values.sort()
        root = Tree_node(nodes_values[len(nodes_values) // 2])
        
        def temp(node_values_avl):
            if len(node_values_avl) == 0:
                return None
            
            mid = len(node_values_avl) // 2
            node = Tree_node(node_values_avl[mid])
            node.left = temp(node_values_avl[:mid])
            node.right = temp(node_values_avl[mid + 1:])
            return node
        mid = len(nodes_values) // 2
        root.left = temp(nodes_values[:mid])
        root.right = temp(nodes_values[mid + 1:])
        print("AVL tree created successfully??????? Gotta check with print\n")
        

    def create_bst_tree():
        global root
        root = Tree_node(nodes_values[0])

        for i in range(1, nodes_number):
            node_value = nodes_values[i]
            new_node = Tree_node(node_value)

            current_node = root
            while True:
                if node_value < current_node.value:
                    if current_node.left is None:
                        current_node.add_child(new_node, 'left')
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif node_value > current_node.value:
                    if current_node.right is None:
                        current_node.add_child(new_node, 'right')
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    print(f"Duplicate value found: {node_value}. Please enter unique values.")
                    return
            
        print("BST created successfully.\n")
    
    if tree_type.lower() == "avl":
        create_avl_tree()
    elif tree_type.lower() == "bst":
        create_bst_tree()
    else:
        print(f"Invalid tree type: {tree_type}. Please enter 'AVL' or 'BST'.")
        return
    return root