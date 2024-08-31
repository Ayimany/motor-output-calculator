from sys import stderr
import re

PROP_REQUIREMENTS = {
    'Pout': ['Eff', 'Pin'],
    'Pin': ['Eff', 'Pout'],
    'Eff': ['Pout', 'Pin'],
}


class motor_struct:

    def __init__(self, targets: list[str], properties: dict[str, float]):
        self.targets = targets
        self.properties = properties


def print_mprop_err(index: int, arg: str, reason: str):
    print(f'At argument #{index} (\'{arg}\'):',
          reason, 'Skipping.', file=stderr)


def represents_floating_point(what: str) -> bool:
    """Determines whether a string can be parsed as a floating point number or not.
    The usual `isnumeric()` method is not great at recognizing floating-point numbers.
    This method fixes said issue."""

    # Maybe begins with a sign, followed by n-or-zero numbers,
    # maybe a dot, and at least one number
    match = re.match(r'^[-+]?[0-9]*\.?[0-9]+', what)

    if match is None:
        return False

    return match.group() == what


def extract_motor_data(args: list[str]) -> motor_struct:
    targets = []
    properties = {}

    for i, arg in enumerate(args):
        if ':' not in arg:
            print_mprop_err(i, arg, 'Missing property delimiter (\':\')')
            continue

        segments = [s.strip() for s in arg.split(sep=':')]

        if (len(segments) > 2):
            print_mprop_err(i, arg,
                            'Can only have one separator per entry (\':\').')
            continue

        property = segments[0]
        value = segments[1]

        if not value or value.isspace():
            print_mprop_err(i, arg, 'Property with no value.')
            continue

        if property == 'Targets':
            requested_targets = [s.strip() for s in value.split(sep=',')]

            for request in requested_targets:
                if request not in PROP_REQUIREMENTS:
                    print_mprop_err(
                        i, arg, f'Invalid property \'{property}\'.')
                    continue

                targets += [request]
            continue

        if property not in PROP_REQUIREMENTS:
            print_mprop_err(i, arg, f'Invalid property \'{property}\'.')
            continue

        if not represents_floating_point(value):
            print_mprop_err(
                i, arg,
                f'Right-hand side of argument, \'{value}\', is non-numeric.')
            continue

        properties[property] = float(value)

    return motor_struct(targets, properties)
