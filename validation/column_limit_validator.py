import os

COLUMN_LIMIT = 80


def get_python_filenames():
    return ["../" + f for f in os.listdir("..") if f.endswith(".py")]


def check_file(filename: str, char_limit: int) -> list[str]:
    errlist = []

    with open(filename) as f:
        lines = f.readlines()

        for ln, line in enumerate(lines):
            ll = len(line)
            if ll >= char_limit:
                errlist.append(f"{filename}: {ll} chars @ line" f" {ln + 1}")

    return errlist


def main():
    py_files = get_python_filenames()

    for filename in py_files:
        errlist = check_file(filename, COLUMN_LIMIT)

        if len(errlist) == 0:
            continue

        for err in errlist:
            print(err)


if __name__ == "__main__":
    main()
