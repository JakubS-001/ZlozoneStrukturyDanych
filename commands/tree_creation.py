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

def create_tree_from_terminal(root=None):
    while True:
        print("Tree type> ", end="")
        tree_type=input().lower()
        if tree_type=="avl" or tree_type=="bst":
            break
        else: print("The available tree types are AVL or BST")
    new_root = create_tree(tree_type)
    return new_root


def create_tree(tree_type, data=None):
    global nodes_values

    print(f"Creating a {tree_type} tree...")
    nodes_values = None
    while True:
        try:
            print("nodes> ", end="")
            if data:
                nodes_number = len(data)
                nodes_values = data
            else:

                input_nodes = list(map(int, input().replace(',', ' ').split()))

                if not input_nodes or len(input_nodes) < 1:
                    return None

                nodes_number = input_nodes[0]

                if len(input_nodes) > 1:
                    nodes_number = len(input_nodes)
                    nodes_values = input_nodes

                
                if nodes_number <= 0:
                    print("The number of nodes must be a positive integer.")
                    continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of nodes.")
        except KeyboardInterrupt:
            print("\nCancelling...")
            return None
        except EOFError:
            print("\nExiting...")
            return None

    while True:
        if nodes_values:
            break

        try:
            print("insert> ", end="")
            nodes_values = list(map(int, input().replace(',', ' ').split()))

            if len(nodes_values) != nodes_number:
                print(f"Please enter exactly {nodes_number} node values.")
                nodes_values = None
                continue
            break
        except ValueError:
            print("Invalid input. Please enter only integers for node values.")
        except KeyboardInterrupt:
            print("\nCancelling...")
            return None
        except EOFError:
            print("\nExiting...")
            return None


    print("Data inserted successfully.")

    for node_value in nodes_values: # Checking if the values are integers, just to be sure
        if not isinstance(node_value, int):
            print(f"Invalid node value: {node_value}. Please enter integers only.")
            return None

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
        def parenting(node):
            if node.left:
                node.left.parent=node
                parenting(node.left)
            if node.right:
                node.right.parent=node
                parenting(node.right)
            

        mid = len(nodes_values) // 2
        root.left = temp(nodes_values[:mid])
        root.right = temp(nodes_values[mid + 1:])
        parenting(root)
        print("AVL created successfully.")
        

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
                        current_node.left = new_node
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                elif node_value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        new_node.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    print(f"Duplicate value found: {node_value}. Please enter unique values.")
                    return None
            
        print("BST created successfully.")
        #print(root)
    if tree_type.lower() == "avl":
        create_avl_tree()
    elif tree_type.lower() == "bst":
        create_bst_tree()
    else:
        print(f"Invalid tree type: {tree_type}. Please enter 'AVL' or 'BST'.")
        return None
    return root