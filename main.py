import sys
from commands.brain import commandcenter
from commands.tree_creation import create_tree


def main():
    # Command-line arguments: python main.py --tree <tree type(AVL/BST)>
    # Write "python3 main.py -t <AVL/BST>" to run the program, just a reminder for me
    if len(sys.argv) != 3 or (sys.argv[1] != "--tree" and sys.argv[1] != "-t"):
        print("Usage: python script.py --tree/-t <tree type (AVL/BST)>")
        sys.exit(1)
    
    tree_type = sys.argv[2]

    # W tym root masz całe drzewo, mam zdefiniowanego print(root), ale nie takiego jak w specyfikacjach zadania, tylko zwykłego
    root = create_tree(tree_type)

    while(True):
        print("action> ", end="")
        command = input().lower()

        if command == "exit":
            print("Exiting...")
            break
        else:
            commandcenter(command, root)

if __name__ == "__main__":
    main()