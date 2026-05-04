import os

def print_hello(name):
    print(f"Hello, {name}!")
    print("This is a simple exemple of EDITO Generic process. You can field the form before launching with your own code.")
if __name__ == "__main__":
    name = os.getenv("NAME", "World")
    print_hello(name)