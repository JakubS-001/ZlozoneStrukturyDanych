#decision making to activate different commands
from commands.printing import *
from commands.child_genocide import mass_murder,kill_all
from commands.searching import find_min_max

def commandcenter(command, *args):
    global known_commands
    known_commands = { # all commands are lowercase
        "help": [info_dump, "Show available commands"],
        "exit": [exit_program, "Exit the program"],
        "print": [print_brain, "Print the tree based on given arguments:\n\tall - prints the elements in tree in in-order, post-order and pre-order\n\ttree - prints tree structure\n\t....-order - prints the elements in tree in the respective order (look argument all)"],
        "findminmax" : [find_min_max, "Print the minimum and maximum tree value"],
        "delete": [mass_murder, "Delete given amount of nodes from the tree"],
        "delete all": [kill_all, "Delete all nodes from the tree in post-order"],
        "create tree": [ "create_tree", "Create a new tree from beggining"]
        # Add more commands here
    }
    
    if command in known_commands:
        if command == "help":
            known_commands[command][0](*args)
        elif command[0:5]=="print":
            return
        else:
            known_commands[command][0](*args)
    elif command[0:5]=="print":
        print_brain(command[6:], *args)
    else:
        print("Unknown command. Type 'help' for a list of available commands.")


def info_dump(*args):
    print("\nAvailable commands:")
    
    for command, (function, description) in known_commands.items():
        print(f"{command} - {description}")  # Print the command and its description
    
    print("\nAll commands are case-insensitive. For example, 'help' and 'Help' are the same command.")
    # Some more miscellaneous information for the user

def exit_program(*args):
    pass