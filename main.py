import sys
import argparse
from commands.brain import commandcenter
from commands.tree_creation import create_tree
from commands.removing_children import mass_removal, remove_all
from commands.dsw import dsw_balance

def main():

    parser = argparse.ArgumentParser(description="Tree creation and manipulation.")
    
    parser.add_argument("-t", "--tree", type=str, required=True,
                        help="Specify the tree type (AVL or BST).")
    parser.add_argument("-d", "--data", type=str, default=None,
                        help="Comma or space separated list of integers to insert into the tree.")

    args = parser.parse_args()

    tree_type = args.tree.lower()
    allowed_types = ["avl", "bst"]

    if tree_type not in allowed_types:
        print("Wrong tree type specified")
        return

    data = None
    
    if args.data:
        data = list(map(int, args.data.replace(',', ' ').split()))
    
    root = create_tree(tree_type, data=data)
    
    if not root:
        print(f"Failed to create {tree_type} tree.")
        return

    while True:
        try:
            print("\naction> ", end="")
            command = input().lower()
            if not sys.stdin.isatty(): print(command)
            
            if command == "exit":
                print("Exiting...")
                break
            else:
                root = commandcenter(command, root)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            sys.stdin=open('/dev/tty')
            print("\nEnding file input...")
            #break


if __name__ == "__main__":
    main()