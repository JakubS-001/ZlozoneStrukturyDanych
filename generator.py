import random

def generate_unique_data(n, output_file="data.txt"):
    count = 2 ** n
   
    data = random.sample(range(1, count * 10), count)

    with open(output_file, 'w') as f:
        f.write(f"{count}\n")
        for number in data:
            f.write(f"{number}\n")

if __name__ == "__main__":
    generate_unique_data(20)
