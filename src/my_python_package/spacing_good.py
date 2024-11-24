def calculate(a, b):
    """Adds two numbers and returns the result."""
    return a + b


class MyClass:
    """A simple class that stores and displays a value."""

    def __init__(self, val):
        self.val = val

    def display(self):
        print(self.val)


def main():
    """Main function to demonstrate the functionality."""
    result = calculate(10, 5)
    print(f"Result: {result}")

    obj = MyClass("Hello")
    obj.display()


if __name__ == "__main__":
    main()

