def print_brain(func, node):
    #print(func, node)
    def print_tree(node, indent="", last=True, *args):
        if node:
            print(indent + ("└── " if last else "├── ") + str(node.value))
            indent += "    " if last else "│   "
            children = [c for c in (node.right, node.left) if c]
            for i, child in enumerate(children):
                print_tree(child, indent, i == len(children) - 1)

    def in_order_traversal(node, *args):
        if node:
            in_order_traversal(node.left)
            print(node.value, end=" ")
            in_order_traversal(node.right)

    def pre_order_traversal(node, *args):
        if node:
            print(node.value, end=" ")
            pre_order_traversal(node.left)
            pre_order_traversal(node.right)

    def post_order_traversal(node, *args):
        if node:
            post_order_traversal(node.left)
            post_order_traversal(node.right)
            print(node.value, end=" ")

    def print_all_order(node):
        print("In-order: ", end="")
        in_order_traversal(node)
        print("\nPost-order: ", end="")
        post_order_traversal(node)
        print("\nPre-order: ", end="")
        pre_order_traversal(node)
        print()
    
    commands = {
        "tree" : print_tree,
        "in-order": in_order_traversal,
        "pre-order": pre_order_traversal,
        "post-order": post_order_traversal,
        "all":print_all_order
    }
    if func in commands:
        commands[func](node)
    else:
        print("Unknown argument. Type 'help' for a list of available arguments of command print.")