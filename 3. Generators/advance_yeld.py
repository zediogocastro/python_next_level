# Genertors aka lazy iterator
from typing import Generator

def echoRound() -> Generator[int, float, str]:
    res = yield
    while res:
        res = yield round(res)
    return "OK"

def main() -> None:
    echo = echoRound()
    next(echo)
    print(echo.send(3.14125))
    print(echo.send(5.14125))
    try:
        print(echo.send(0.0))
    except StopIteration as e:
        print(e.value)
    

if __name__ == "__main__":
    main()