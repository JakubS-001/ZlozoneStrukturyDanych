def find(root, target):#Tried to put it in brain, didn't work
    current_node=root
    while True:
        if current_node.value==target:
            return current_node
        if target > current_node.value:
            if current_node.right: current_node=current_node.right
            else:
                print(f"Couldn't find node {target}")
                return 0
        if target < current_node.value:
            if current_node.left: current_node=current_node.left
            else:
                print(f"Couldn't find node {target}")
                return 0

def single_murder(root, sacrifice):
    parent = sacrifice.parent
    kids=[]
    if sacrifice.left: kids.append(sacrifice.left)
    if sacrifice.right: kids.append(sacrifice.right)

    if len(kids)==0: #if sacrifice has no kids
        if parent==None: 
            root=None
            return root
        if parent.left == sacrifice: parent.left = None
        elif parent.right == sacrifice: parent.right=None
        return root
    
    elif len(kids)==1: #sacrifice has one kid
        if parent==None:
            root=kids[0]
            kids[0].parent=None
            return root
        kids[0].parent=parent
        if parent.left == sacrifice: parent.left = kids[0]
        elif parent.right == sacrifice: parent.right=kids[0]
        return root
    
    


def mass_murder(root):

    while True:
        try:
            print("nodes> ", end="")
            victim_number = int(input()) 
            if victim_number <= 0:
                print("The number of nodes must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the number of nodes.")
    
    while True:
        try:
            print("delete> ", end="")
            victims = list(map(int, input().split()))
            if len(victims) != victim_number:
                print(f"Please enter exactly {victim_number} node values.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter only integers for node values.")
    
    for node_value in victims: # Checking if the values are integers, just to be sure
        if not isinstance(node_value, int):
            print(f"Invalid node value: {node_value}. Please enter integers only.")
            return
    print("Data inserted successfully")

    for victim_value in victims:
        sacrifice=find(root, victim_value)
        
        root = single_murder(root, sacrifice)
        

    return root