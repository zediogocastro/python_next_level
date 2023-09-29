from dataclasses import dataclass

@dataclass
class Item:
    name: str
    weight: float

def main() -> None:

    inventory = [
        Item('Mac', 1.5),
        Item('iPhone', 0.5),
        Item('book', 0.2),
        Item('racket', 0.8),
        Item('guitar', 4.5),
    ]

    inventory_iterator = iter(inventory)
    print(next(inventory_iterator))
    print(next(inventory_iterator))

    # Is the same as:
    for item in inventory:
        print(item)

if __name__ == '__main__':
    main()
