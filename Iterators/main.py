from dataclasses import dataclass

@dataclass
class Item:
    name: str
    weight: float

def main() -> None:

    inventory = [
        Item("laptop", 1.5),
        Item("phone", 0.5),
        Item("book", 1.0),
        Item("camera", 1.0),
    ]

    #inventory_iterator = inventory.__iter__()
    # Simpler version:
    inventory_iterator = iter(inventory)

    print(next(inventory_iterator))
    print(next(inventory_iterator))

    with open("Iterators/countries.txt") as file:
        for line in iter(file.readline, "Italy\n"):
            print(line, end="a")

if __name__ == "__main__":
    main()