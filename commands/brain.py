#decision making to activate different commands
import ast, inspect
from commands.printing import *
from commands.removing_children import mass_removal, initiate_remove_all
from commands.searching import find_min_max
from commands.dsw import *
from commands.tree_creation import create_tree_from_terminal
from commands.export_tik import export_print_tree_tikz

def commandcenter(command, root, *args):
    global known_commands
    known_commands = { # all commands are lowercase
        "help": [info_dump, "Show available commands"],
        "exit": [None, "Exit the program"],
        "print": [None, "Print the tree based on given arguments:\n\tall - prints the elements in tree in in-order, post-order and pre-order\n\ttree - prints tree structure\n\t....-order - prints the elements in tree in the respective order (look argument all)"],
        "findminmax" : [find_min_max, "Print the minimum and maximum tree value"],
        "delete": [mass_removal, "Delete given amount of nodes from the tree"],
        "delete all": [initiate_remove_all, "Delete all nodes from the tree in post-order"],
        "create tree": [create_tree_from_terminal, "Create a new tree from beggining"],
        "dsw": [dsw_balance, "Balance tree using DSW"],
        "export": [export_print_tree_tikz, "Export tree to tickzpicture (Latex)"]
        # Add more commands here
    }
    
    
    if command[0:5]=="print":
        print_brain(command[6:], root, *args)
    elif command in known_commands:
        function = known_commands[command][0]
        if function == None:
            return root
        elif contains_explicit_return(function):
            root = function(root, *args)
        else:
            function(root, *args)
    else:
        print("Unknown command. Type 'help' for a list of available commands.")
    return root

def contains_explicit_return(f):
    return any(isinstance(node, ast.Return) for node in ast.walk(ast.parse(inspect.getsource(f))))

def info_dump(root, *args):
    print("\nAvailable commands:")
    
    for command, (function, description) in known_commands.items():
        print(f"{command} - {description}")  # Print the command and its description
    
    print("\nAll commands are case-insensitive. For example, 'help' and 'Help' are the same command.")
    # Some more miscellaneous information for the user