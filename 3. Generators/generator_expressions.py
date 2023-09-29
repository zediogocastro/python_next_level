# A bit like lambda functions, but then are anomonous generators


def main() -> None:
    powers = (2**i for i in range(10))
    for power in powers:
        print(power)

    # you can also use generators expressions as function arguments
    print(sum(2**i for i in range(10)))

if __name__ == "__main__":
    main()
