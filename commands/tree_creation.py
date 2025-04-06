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

    def create_avl_tree():
        pass

    def create_bst_tree():
        root = Tree_node(nodes_values[0])
        nodes_in_tree = [root]

        for i in range(1, nodes_number):
            node_value = nodes_values[i]
            if not isinstance(node_value, int):
                print(f"Invalid node value: {node_value}. Please enter integers only.")
                return
            nodes_in_tree.append(Tree_node(node_value))

            current_node = root
            while True:
                if node_value < current_node.value:
                    if current_node.left is None:
                        current_node.add_child(nodes_in_tree[i], 'left')
                        nodes_in_tree[i].parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif node_value > current_node.value:
                    if current_node.right is None:
                        current_node.add_child(nodes_in_tree[i], 'right')
                        nodes_in_tree[i].parent = current_node
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