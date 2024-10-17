import argparse as ap

PROGRAM_NAME = "motor-output-calculator (m-out)"
PROGRAM_DESC = "Calculates unknown properties of electric motors based other, \
known properties"

PROGRAM_EPILOGUE = "University project. Immature for most real work."


def setup():
    """
    Initializes the program's CLI argument parser.

    @return: The parse results.
    """
    parser = ap.ArgumentParser(
        prog=PROGRAM_NAME, description=PROGRAM_DESC, epilog=PROGRAM_EPILOGUE
    )

    parser.add_argument("--terse", "-t", action="store_true")
    parser.add_argument(
        "--show-props", help="Show available properties", action="store_true"
    )

    return parser.parse_known_args()
