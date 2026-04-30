import os

def print_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    name = os.getenv("NAME", "World")
    print_hello(name)