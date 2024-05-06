def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disks {source} to {target}: 1")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {source} to {target}: {n}")
    hanoi(n - 1, auxiliary, target, source)


def main():
    n = int(input("Enter number of disks: "))
    source = "A"
    target = "C"
    auxiliary = "B"
    print(f"Initial state: {{'A': {list(range(n, 0, -1))}, 'B': [], 'C': []}}")
    hanoi(n, source, target, auxiliary)
    print(f"Final state: {{'A': [], 'B': [], 'C': {list(range(n, 0, -1))}}}")


if __name__ == "__main__":
    main()
