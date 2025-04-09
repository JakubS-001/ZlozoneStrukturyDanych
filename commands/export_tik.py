def export(node):
    if not node.left and not node.right:
        return f"node {{ {node.value} }}"
    
    # Recursively build the left and right child parts
    l_str = "child{"+export(node.left)+"}" if node.left else "child[missing]"
    r_str = "child{"+export(node.right)+"}" if node.right else "child[missing]"
    
    # Construct the TikZ tree part
    return f"node {{ {node.value} }}  {l_str}  {r_str} "

def export_tree(root):
    tikz_code = "\\begin{tikzpicture}[level distance=10mm,"
    tikz_code += "\nevery node/.style={fill=red!60,circle,inner sep=1pt},"
    tikz_code += "\nlevel 1/.style={sibling distance=80mm,nodes={fill=red!25}},"
    tikz_code += "\nlevel 2/.style={sibling distance=40mm,nodes={fill=red!45}},"
    tikz_code += "\nlevel 3/.style={sibling distance=20mm,nodes={fill=red!30}},"
    tikz_code += "\nlevel 4/.style={sibling distance=10mm,nodes={fill=red!25}},"
    tikz_code += "\nlevel 5/.style={sibling distance=5mm,nodes={fill=red!25}},"
    tikz_code += "\nlevel 6/.style={sibling distance=2.5mm,nodes={fill=red!25}},]"
    tikz_code += "\n\\"
    tikz_code += export(root)
    tikz_code += "\n;\n\\end{tikzpicture}"
    return tikz_code

def export_print_tree_tikz(root):
    print(export_tree(root))