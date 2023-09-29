# Genertors aka lazy iterator
from typing import Generator

def simpleGenerator() -> Generator[str, None, None]:
    word = "Hello World"
    yield word
    word += "!"
    yield word

def main() -> None:
    print(list(simpleGenerator()))
    

if __name__ == "__main__":
    main()