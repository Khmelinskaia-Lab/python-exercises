def parse_file(input_filename: str) -> list[str]:
    """This function reads from an input file and returns all the
    words in a list. This is a helper function; treat as black box.
    """
    word_list = []

    # save each line as a string in a list
    input_file = open(input_filename).readlines()

    for line in input_file:
        line = line.strip()  # strip whitespace
        if not line or line.startswith("#"):
            continue  # skip empty lines and comments

        for word in line.split():  # splits the string by spaces
            word_list.append(word.lower())  # to eliminate case inconsistency

    return word_list


def main() -> None:
    word_list = parse_file("../data/hw1/Macbeth")  # can change Macbeth to any word file

    """Insert code here to read word frequencies

    In the `data/hw1/` directory is a text file where we have the entire Macbeth
    copied from http://shakespeare.mit.edu/macbeth/full.html.

    The file is read by a pre-defined helper function that returns all
    the words as a list. Use dictionaries to find out how frequently
    every word occurs, then sort the dictionary by the word frequency.
    One way would be using:

    ```
    sorted_word_count = sorted(
        word_count.items(),
        key=lambda kv: kv[1],
        reverse=True
    )
    ```

    where word_count is the name of the dictionary and sorted_word_count is a
    list of tuples sorted by word frequency.
    
    You could also check out defaultdict for a better dictionary using:    
    from collections import defaultdict.

    Print the 10 most commonly used 4+ letter words as follows:

    <word 1> occurs <n1> times.
    <word 2> occurs <n2> times.

    and so on.

    You could also just sort the list and count the frequencies, but
    where's the fun in that?!
    """


if __name__ == "__main__":
    main()
