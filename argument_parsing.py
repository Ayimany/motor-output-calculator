import argparse as ap

PROGRAM_NAME = "motor-output-calculator (m-out)"
PROGRAM_DESC = """
Calculates properties of electric motors based on known properties
"""

PROGRAM_EPILOGUE = "University project. Immature for most real work."


def setup():
    """
    Initializes the program's CLI argument parser.

    @return: The parse results.
    """

    # create an argument parser object
    parser = ap.ArgumentParser(
        prog=PROGRAM_NAME, description=PROGRAM_DESC, epilog=PROGRAM_EPILOGUE
    )

    # add the option to print the output ina terse format
    parser.add_argument("--terse", "-t", action="store_true")

    # add the option to show program properties
    parser.add_argument(
        "--show-props", help="Show available properties", action="store_true"
    )

    # parse the listed arguments and leave the other alone for program parsing
    return parser.parse_known_args()
