def main() -> None:
    """Insert code here to fix a score file

    You can find a real score file (data/hw2/docking_score.sc) which was
    generated using a buggy job distribution system. Your job is to write a
    fixed score file called fixed_docking_score.sc which takes care of the
    following problems:

    1)  docking_score.sc has multiple occurrences of the same decoy.
        For example, the decoy name 3v4f_b_INPUT_0049 appears multiple
        times. In the fixed file, write only the LAST instance of each
        decoy and discard all duplicate lines,
        e.g. only retain line 66 for 3v4f_b_INPUT_0049.

    2)  The lines are, at times, truncated.
        Delete all such lines in the fixed score file.

    3)  The decoy names may need to be changed to make them descriptive.
        In the fixed file, change the decoy names from 3v4f_b_INPUT_0049
        to file_handling_string_manipulation_test_0049 and so on.
        (Let's assume we also did this for the corresponding decoy pdb
        files.)

    No other detail in the lines should change. The two header lines
    should be printed as is. The order of the lines that are not
    discarded should be the same. At the end of your script, print out
    the number of lines in your decoy file and the number of lines you
    discarded.
    """


if __name__ == "__main__":
    main()
