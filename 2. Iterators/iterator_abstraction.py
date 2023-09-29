from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class LineItem:
    price: int
    quantity: int

    def total_price(self) -> int:
        return self.price * self.quantity
    
def print_totals(items: Iterable[LineItem]) -> None:
    for item in items:
        print(item.total_price())

def main() -> None:
    line_items = [
        LineItem(1_000, 1),
        LineItem(3_000, 2),
        LineItem(10, 5),
    ]
    print_totals(line_items)

if __name__ == '__main__':
    main()


# The iterables introduces abstraction because we can either use a list
# like we did or we could use a tupple, or whatever, as long as is iter