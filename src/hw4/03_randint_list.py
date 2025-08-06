from random import randint


def generate_random_list() -> list[int]:
    """This function generates and returns a randomly large list of
    random integers between 1 and 1,000,000. Treat as black box.
    """

    random_list = []
    list_size = randint(1, 1000000)

    for _ in range(list_size):
        random_list.append(randint(1, 1000000))

    return random_list


def main() -> None:
    """In this exercise we will try to return the nth element from a
    randomly generated list. The user enters the index n. The code to
    check for a positive integer input is given. You need to fill in
    code to ensure that the index is present in the list and print the
    nth number. Otherwise, you have to interactively ask the user for
    another input.
    """

    # Generate a randomly large random list
    random_list = generate_random_list()
    attempt_count = 0

    # This while loop will continue to ask for an index until a valid
    # index is found and you break it.
    while True:
        try:
            index_input = input(
                "What is the index of the element that youwould like to find out? "
            )
            # if index_input is not a positive integer,
            # assertion will return False
            assert index_input.isnumeric()

        except AssertionError:
            print("Please enter a non-negative integer.")

        else:
            index = int(index_input)
            """Insert code here to find element
            
            Within this else clause, insert a try/except/else block to
            first try printing out the element at the given index in 
            random_list. If the index is out of bounds, print an
            appropriate message, else print the element and break the
            infinite loop.
            """

        finally:
            attempt_count += 1
            print("This is attempt number {}.".format(attempt_count))


if __name__ == "__main__":
    main()
