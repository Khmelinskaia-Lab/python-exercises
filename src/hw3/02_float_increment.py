def main() -> None:
    """Write a function for float ranges

    This function should imitate the range() function for integers.
    It should accept one to three parameters in the order:
        1) start value - compulsory
        2) end value - optional, defaults to start
        3) increment - optional, defaults to 1.0

    Use argument parsing feed in these values, ensuring that they are
    of type float. While you can set default values in the argparse
    itself, try to do it in the function definition instead.

    Then print a comma separated list of range values.

    For example,
    A)
    If command line is:

    python float_increment.py --start 1.5 --end 1.9 --increment 0.1

    the output should be:
    1.5, 1.6, 1.7, 1.8

    B)
    If command line is:

    python float_increment.py -s 1.9 -e 1.5 -i -0.1

    the output should be:
    1.9, 1.8, 1.7, 1.6

    C)
    If command line is:

    python float_increment.py -s 1.5

    the output should be:
    1.5

    D)
    If command line is:

    python float_increment.py -s 1.5 -e 5.9

    the output should be:
    1.5, 2.5, 3.5, 4.5, 5.5
    """


if __name__ == "__main__":
    main()
