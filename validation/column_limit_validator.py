import os

COLUMN_LIMIT = 80


def get_python_filenames():
    """
    Returns the list of python filenames in the current working directory
    @return: The list of python filenames
    """

    # grab all files ending in .py
    return [f for f in os.listdir() if f.endswith(".py")]


def check_file(filename: str, char_limit: int) -> list[str]:
    """
    Checks each line in the given filename to see if it contains at least
    `char_limit` characters. If it doesn't, it appends an error message
    to a list which is returned by this function.

    @param filename: The filename to check
    @param char_limit: The character limit
    @return: The list of error messages
    """
    errlist = []

    # open file
    with open(filename) as f:
        lines = f.readlines()

        # go through each line
        for ln, line in enumerate(lines):
            ll = len(line)

            # append an error message if limit is surpassed
            if ll >= char_limit:
                errlist.append(f"{filename}: {ll} chars @ line" f" {ln + 1}")

    return errlist


def main():
    # get all python files
    py_files = get_python_filenames()

    # check all files for column limits
    for filename in py_files:
        errlist = check_file(filename, COLUMN_LIMIT)

        # no errors ? ok
        if len(errlist) == 0:
            continue

        # else, print them
        for err in errlist:
            print(err)


if __name__ == "__main__":
    main()
