import sys
import argparse
from commands.brain import commandcenter
from commands.tree_creation import create_tree
from commands.printing import print_brain
from commands.searching import find_min_max
from commands.dsw import dsw_balance
import time

def main(filename):
    with open("random_array_00524288.txt", 'r') as f:
        lines = f.readlines()

    total_rows = int(lines[0].strip())
    data_lines = [line.strip() for line in lines[1:total_rows+1]]

    for power in range(6, 10):
        size = 2 ** power
        if size > total_rows:
            break
        batch = data_lines[:size]
        
        for i in range(4):
            process_batch(list(map(int,batch)), size)

    for amount, types in czasy.items():
        print(f"\n{amount} danych:")
        for tree_type, operations in types.items():
            print(f"  {tree_type.upper()}:")
            for op, times in operations.items():
                avg = sum(times) / len(times)
                print(f"    {op}: {avg:.2f}ms")
   
czasy = dict()

def process_batch(batch, amount):
    if amount not in czasy:
        czasy[amount] = {
            "avl": {
                "tree_creation": [],
                "min_max": [],
                "in_order": []
            },
            "bst": {
                "tree_creation": [],
                "min_max": [],
                "in_order": [],
                "dsw_balance": []
            }
        }


    start = time.perf_counter()
    root = create_tree("avl", data=batch)
    delay = (time.perf_counter() - start) * 1000
    print(f"Utworzenie AVL {amount} danych: {delay} ms")
    czasy[amount]["avl"]["tree_creation"].append(delay)

    start = time.perf_counter()
    find_min_max(root)
    delay = (time.perf_counter() - start) * 1000
    print(f"Min/max AVL {amount} danych: {delay} ms")
    czasy[amount]["avl"]["min_max"].append(delay)

    start = time.perf_counter()
    print_brain("in-order", root)
    delay = (time.perf_counter() - start) * 1000
    print(f"In-order AVL {amount} danych: {delay} ms")
    czasy[amount]["avl"]["in_order"].append(delay)

    # BST processing
    start = time.perf_counter()
    root = create_tree("bst", data=batch)
    delay = (time.perf_counter() - start) * 1000
    print(f"Utworzenie BST {amount} danych: {delay} ms")
    czasy[amount]["bst"]["tree_creation"].append(delay)

    start = time.perf_counter()
    find_min_max(root)
    delay = (time.perf_counter() - start) * 1000
    print(f"Min/max BST {amount} danych: {delay} ms")
    czasy[amount]["bst"]["min_max"].append(delay)

    start = time.perf_counter()
    print_brain("in-order", root)
    delay = (time.perf_counter() - start) * 1000
    print(f"In-order BST {amount} danych: {delay} ms")
    czasy[amount]["bst"]["in_order"].append(delay)

    start = time.perf_counter()
    dsw_balance(root)
    delay = (time.perf_counter() - start) * 1000
    print(f"DSW Balancing BST {amount} danych: {delay} ms")
    czasy[amount]["bst"]["dsw_balance"].append(delay)




if __name__ == "__main__":
    main('data.txt')