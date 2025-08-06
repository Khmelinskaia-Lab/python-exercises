def within_bounds(
    value: float,
    low: float,
    high: float,
) -> bool:
    """This function returns True if value is less than high and more
    than low. Replace this function with a lambda function.
    """

    return high > value > low


def main() -> None:
    """Insert code here to input a series of numbers and of bounds and
    print out a series of True/False if the numbers are within the
    bounds.

    Use argument parsing to accept the three arguments. To input a
    number series you may use the nargs parameter. Then substitute the
    function written above with a lambda function, which does the
    exact same thing. Finally print out True or False in the same order.
    """


if __name__ == "__main__":
    main()
