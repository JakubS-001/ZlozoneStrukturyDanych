#decision making to activate different commands

def commandcenter(command, *args):

    known_commands = { # all commands are lowercase
        "help": [info_dump, "Show available commands"],
        "exit": [exit_program, "Exit the program"],
        "print": [print_tree, "Print the tree structure"],
        "inorder" : [in_order_traversal, "Print the tree in order"],
        "postorder" : [post_order_traversal, "Print the tree post order"],
        "preorder" : [pre_order_traversal, "Print the tree pre order"],
        "findminmax" : [find_min_max, "Print the minimun and maximum tree value"]
        # Add more commands here
    }
    
    if command in known_commands:
        if command == "help":
            known_commands[command][0](known_commands, *args)
        else:
            known_commands[command][0](*args)
    else:
        print("Unknown command. Type 'help' for a list of available commands.")


def info_dump(known_commands, *args):
    print("\nAvailable commands:")
    
    for command, (function, description) in known_commands.items():
        print(f"{command} - {description}")  # Print the command and its description
    
    print("\nAll commands are case-insensitive. For example, 'help' and 'Help' are the same command.\n")
    # Some more miscellaneous information for the user


def exit_program(*args):
    pass

def print_tree(node, indent="", last=True, *args):
    if node:
        print(indent + ("└── " if last else "├── ") + str(node.value))
        indent += "    " if last else "│   "
        children = [c for c in (node.right, node.left) if c]
        for i, child in enumerate(children):
            print_tree(child, indent, i == len(children) - 1)
            

def find_min(node):
    current_node = node
    while current_node.left:
        current_node = current_node.left
    return current_node.value

def find_max(node):
    current_node = node
    while current_node.right:
        current_node = current_node.right
    return current_node.value

def find_min_max(node):
    print(f"Min: {find_min(node)}")
    print(f"Max: {find_max(node)}")

def in_order_traversal(node, *args):
    if node:
        in_order_traversal(node.left)
        print(node.value)
        in_order_traversal(node.right)

def pre_order_traversal(node, *args):
    if node:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node, *args):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value)
