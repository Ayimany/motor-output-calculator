import argparse as ap


PROGRAM_NAME = 'motor-output-calculator (m-out)'
PROGRAM_DESC = 'Calculates unkmown properties of electric motors based other, \
known properties'
PROGRAM_EPILOGUE = 'University project. Immature for most real work.'


def setup():
    parser = ap.ArgumentParser(
        prog=PROGRAM_NAME,
        description=PROGRAM_DESC,
        epilog=PROGRAM_EPILOGUE
    )

    return parser.parse_known_args()
