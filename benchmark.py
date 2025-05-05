import sys
import argparse
import csv
import time
import tracemalloc
from itertools import islice
from commands.brain import commandcenter
from commands.tree_creation import create_tree
from commands.printing import print_brain
from commands.searching import find_min_max
from commands.dsw import dsw_balance

import time
from itertools import islice

def main(filename):
    for power in range(1, 21):
        size = 2 ** power

        for i in range(4):
            with open(filename, 'r') as f:
                total_rows = int(f.readline().strip())
                if size > total_rows:
                    break

                current_data = [int(line.strip()) for line in islice(f, size)]

            process_batch(current_data, size)

    # for amount, types in czasy.items():
    #     print(f"\n{amount} danych:")
    #     for tree_type, operations in types.items():
    #         print(f"  {tree_type.upper()}:")
    #         for op, times in operations.items():
    #             avg = sum(times) / len(times)
    #             print(f"    {op}: {avg:.2f}ms")

    write_csv_files()
   
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


    #start = time.perf_counter() # assuming we don't meassure the data preparation to more accurately compare BST vs AVL
    (root, start) = create_tree("avl", data=batch, benchmark=True)
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

    #start = time.perf_counter()
    (root, start) = create_tree("bst", data=batch, benchmark=True)
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


def write_csv_files():
    for tree_type in ["avl", "bst"]:
        for operation in czasy[next(iter(czasy))][tree_type]:
            filename = f"{tree_type}_{operation}.csv"
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["name", "data", "time"])

                for amount, results in czasy.items():
                    times = results[tree_type][operation]
                    if times:
                        avg_time = sum(times) / len(times)
                        writer.writerow([tree_type, amount, f"{avg_time:.4f}"])


if __name__ == "__main__":
    main('data.txt')