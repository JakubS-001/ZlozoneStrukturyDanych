#decision making to activate different commands

def commandcenter(command):

    known_commands = { # all commands are lowercase
        "help": Info_dump
        # Add more commands here
    }
    
    if command in known_commands:
        known_commands[command]()
    else:
        print("Unknown command. Type 'help' for a list of available commands.")


def Info_dump():
    print("\nAvailable commands:")
    print("1. Help - Show available commands")
    print("2. Exit - Exit the program")
    # Add more commands as needed
    print("\nAll commands are case-insensitive. For example, 'help' and 'Help' are the same command.")
    # Some more miscellaneous information for the user

    print()