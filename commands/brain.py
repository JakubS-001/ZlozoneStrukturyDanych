#decision making to activate different commands

def commandcenter(command): #Process the command
    if command == "help":
        Help()
    else:
        print("Command not recognized. Type 'Help' for available commands.")


def Help():
    print("\nAvailable commands:")
    print("1. Help - Show available commands")
    print("2. Exit - Exit the program")
    
    # Add more commands as needed

    print()