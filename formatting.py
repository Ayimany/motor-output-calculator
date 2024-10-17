import logging

from data_extraction import MotorStruct
from data_formats import VALID_PROPERTIES

RESET = "\x1b[0m"
COLOR_ERROR = "\x1b[31;20m"
COLOR_CRITICAL = "\x1b[31;1m"
COLOR_WARNING = "\x1b[33;20m"
COLOR_DEBUG = "\x1b[34;20m"
COLOR_INFO = "\x1b[35;20m"

FORMAT = "%(levelname)s: %(message)s"

FORMAT_STYLES = {
    logging.DEBUG: f"{COLOR_INFO}{FORMAT}{RESET}",
    logging.INFO: f"{COLOR_DEBUG}{FORMAT}{RESET}",
    logging.WARNING: f"{COLOR_WARNING}{FORMAT}{RESET}",
    logging.ERROR: f"{COLOR_ERROR}{FORMAT}{RESET}",
    logging.CRITICAL: f"{COLOR_CRITICAL}{FORMAT}{RESET}",
}


def applyfmt(log):
    """
    Generates a formatter for a logger

    @param log: The log to apply the formatting to
    @return: The formatter object
    """
    formatter = logging.Formatter(FORMAT_STYLES.get(log.levelno))

    return formatter.format(log)


class FormatWrapper:
    """
    Aids in the generation of custom log formatting
    """

    def format(self, log):
        """
        Applues a format to a given log entry

        @param log: The log to apply the formatting to
        @return: The formatted log entry
        """
        return applyfmt(log)


logger = logging.getLogger("m-out")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(FormatWrapper())

logger.addHandler(handler)


def print_available_properties():
    """
    Prints the properties which a user can use to calculate motor data

    @return: Nothing.
    """
    print("Available Properties")

    for prop in VALID_PROPERTIES:
        print(f"{VALID_PROPERTIES[prop]} : {prop}")


def format_as_matrix_nx2(data: MotorStruct, decimals=4, padding=1):
    """
    Receives motor data and formats it as a table through the use of a data
    matrix. Pretty version

    @param data: The data to format
    @param decimals: The amount of decimal places to round to
    @param padding: The padding to apply to each entry in the table
    @return: The formatted data
    """
    longest_key_length = 0
    longest_value_length = 0
    matrix = []

    if len(data.properties) < 1:
        return "Please provide at least one property."

    for prop in data.properties:
        key = VALID_PROPERTIES[prop]
        value = str(round(data.properties[prop], decimals))

        if len(key) > longest_key_length:
            longest_key_length = len(key)

        if len(value) > longest_value_length:
            longest_value_length = len(value)

        matrix.append([key, value])

    key_hline_count = longest_key_length + padding * 2
    value_hline_count = longest_value_length + padding * 2

    fmt = "┌" + "─" * key_hline_count + "┬" + "─" * value_hline_count + "┐"

    for i, row in enumerate(matrix):
        key = row[0]
        key_length = len(key)
        key_filler = " " * (longest_key_length - key_length)
        value = row[1]
        value_length = len(value)
        value_filler = " " * (longest_value_length - value_length)
        padding_string = " " * padding

        fmt += "\n"
        fmt += "│" + padding_string
        fmt += key + key_filler + padding_string
        fmt += "│" + padding_string
        fmt += value + value_filler + padding_string
        fmt += "│"

        if i < len(matrix) - 1:
            fmt += "\n"
            fmt += "├"
            fmt += "─" * key_hline_count
            fmt += "┼"
            fmt += "─" * value_hline_count
            fmt += "┤"

    fmt += "\n└" + "─" * key_hline_count + "┴" + "─" * value_hline_count + "┘"

    return fmt


def format_as_matrix_nx2_terse(data: MotorStruct, decimals=4, padding=1):
    """
    Receives motor data and formats it as a table through the use of a data
    matrix. Terse version

    @param data: The data to format
    @param decimals: The amount of decimal places to round to
    @param padding: The padding to apply to each entry in the table
    @return: The formatted data
    """
    longest_key_length = 0
    longest_value_length = 0
    matrix = []

    if len(data.properties) < 1:
        return "Please provide at least one property."

    for prop in data.properties:
        key = VALID_PROPERTIES[prop]
        value = str(round(data.properties[prop], decimals))

        if len(key) > longest_key_length:
            longest_key_length = len(key)

        if len(value) > longest_value_length:
            longest_value_length = len(value)

        matrix.append([key, value])

    fmt = ""

    for i, row in enumerate(matrix):
        key = row[0]
        key_length = len(key)
        key_filler = " " * (longest_key_length - key_length)
        value = row[1]
        value_length = len(value)
        value_filler = " " * (longest_value_length - value_length)
        padding_string = " " * padding

        fmt += key + key_filler + padding_string
        fmt += "=" + padding_string
        fmt += value + value_filler + padding_string

        if i != len(matrix) - 1:
            fmt += "\n"

    return fmt
