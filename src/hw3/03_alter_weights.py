def main() -> None:
    """Write a function to alter score weights

    Attached is a file called data/hw3/ref2015_wts which has the weights of the
    various score terms. Using argparse and file parsing methods, read
    the file and make a dictionary like:

    ```
    score_weights = {'fa_atr': 1, 'fa_rep': 0.55, ...}
    ```

    Now, write a function to change the default weights of selected
    score terms and display which terms were changes. Since you have no
    prior way of determining how many terms need to be changed, the
    function should accept the dictionary of weights and a variable
    number of keyword arguments (look up **kwargs).


    For example,
    A)
    If command line is:

    python alter_weights.py --terms fa_atr --weights 0.8

    the output should be:
    fa_atr was changed to 0.8
    {'fa_atr': 0.8, 'fa_rep': 0.55, ...}

    B)
    If command line is:

    python float_increment.py -t fa_atr fa_rep -w 0.8 0.9

    the output should be:
    fa_atr was changed to 0.8
    fa_rep was changed to 0.9
    {'fa_atr': 0.8, 'fa_rep': 0.55, ...}
    """


if __name__ == "__main__":
    main()
