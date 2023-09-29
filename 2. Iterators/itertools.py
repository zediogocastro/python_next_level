from dataclasses import dataclass
import itertools

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

    for i in itertools.count(10, 10):
        print(i)
        if i >= 30:
            break
    
    print("------Repeat------")
    for i in itertools.repeat(10, 4):
        print(i)

    print("------Accumulators------")
    subtotals = [1, 2, 3, 4]
    for i in itertools.accumulate(subtotals):
        print(i)

    print("------Permutations------")
    teams: list[str] = ['benfica', 'porto', 'sporting']

    perms = itertools.permutations(teams, 2)
    for draws in perms:
        print(draws)

    print("------Combinations------")
    perms = itertools.combinations(teams, 2)
    #for draws in perms:
    #    print(draws)
    print(list(perms))

    print("------Chain------")
    perms = itertools.chain(teams, "Home", "Away")
    print(list(perms))

    print("------Filter False------")
    print(list(itertools.filterfalse(lambda x: x.weight < 1, inventory)))

    print("------StarMap------")
    print(list(itertools.starmap(lambda x, y: x+y , [(2,6), (4,4)])))

if __name__ == '__main__':
    main()
