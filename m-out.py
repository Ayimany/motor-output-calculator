from sys import argv, stderr
from argparse import ArgumentParser

# THIS REQUIRES SERIOUS REFACTORING
# IT IS IN A WORKING STATE, BUT IS UGLY AF
# Try a correct input such as Target:Eff Pin:15 Pout:14
# Try an incorrect input such as Target:Eff Pout:14


EXIT_FAILURE = 1


CALCULATION_MAP = {
    # There is likely a better way to do this.
    # I will think about it later.:w

    'Pout': ['Eff', 'Pin'],
    'Pin': ['Eff', 'Pout'],
    'Eff': ['Pout', 'Pin'],
}

g_display_help_message = False


# TODO: Move to module 'argument_parsing.py'

def obtain_error_list_from_input(arguments: list[str]) -> list[str]:
    errors = []

    for arg in arguments:
        if arg.startswith('-'):
            continue

        if ':' not in arg or arg == ':':
            errors.append(f'Non-flag argument in invalid format ({arg})')

    return errors


def arguments_to_mapping(arguments: list[str]) -> dict[str, str]:
    mapping = {}

    for arg in arguments:
        if arg.startswith('-'):
            continue

        split_arg = arg.split(':')
        mapping[split_arg[0]] = split_arg[1]

    return mapping


# TODO: Move to module 'electric_motor.py'

def calculate_mechanical_output_watts_ot_av(
        output_torque_newton_metres: float,
        angular_velocity_radians_per_second: float) -> float:
    return output_torque_newton_metres * angular_velocity_radians_per_second


def calculate_mechanical_output_watts_ef_ei(
        efficiency: float,
        electrical_input_watts: float) -> float:
    return efficiency * electrical_input_watts


def calculate_electrical_input_watts_ef_mo(
        efficiency: float,
        mechanical_output_watts: float) -> float:
    return mechanical_output_watts / efficiency


def calculate_electrical_input_watts_v_c(
        voltage: float,
        current: float) -> float:
    return voltage * current


def calculate_efficiency_mo_ei(mechanical_output_watts: float,
                               electrical_input_watts: float) -> float:
    return mechanical_output_watts / electrical_input_watts


def main():
    # Likely to be handled by argparse later.
    if len(argv) <= 1:
        print('No arguments. Aborting.', file=stderr)
        quit(EXIT_FAILURE)

        # TODO: refactor into own module
        parser = ArgumentParser(
            prog='m-out',
            description='Calculates characteristics of electrical motors',
            epilog='This is a Uni project'
        )

        parser.parse_args(argv)

    # Ensure correct format. This will be refactored.
    errors = obtain_error_list_from_input(argv[1:])
    if (len(errors) > 0):
        print(f'There are errors in your input. ({len(errors)})', file=stderr)
        for error in errors:
            print(f'\t- {error}')
        quit(EXIT_FAILURE)

    input_data = arguments_to_mapping(argv[1:])

    if 'Target' not in input_data:
        print('No calculation target provided. Aborting.')
        quit(EXIT_FAILURE)

    target = input_data['Target']

    if target not in CALCULATION_MAP:
        print(f'Target not supported ({target}). Aborting.')
        quit(EXIT_FAILURE)

    requirements = CALCULATION_MAP[target]

    for req in requirements:
        if req not in input_data:
            print('Failed to locate requirement' +
                  f'`{req}` for target `{target}`.')
            quit(EXIT_FAILURE)

        if not input_data[req].isnumeric():
            print(
                'Numeric requirement is non-numeric ' +
                f'({req} = {input_data[req]}). ' +
                'Aborting.'
            )
            quit(EXIT_FAILURE)

    match (target):
        case 'Pout':
            efficiency = float(input_data['Eff'])
            p_in = float(input_data['Pin'])
            print(f'{target} = {
                  calculate_mechanical_output_watts_ef_ei(efficiency, p_in)}')
        case 'Pin':
            efficiency = float(input_data['Eff'])
            p_out = float(input_data['Pout'])
            print(f'{target} = {
                  calculate_electrical_input_watts_ef_mo(efficiency, p_out)}')
        case 'Eff':
            p_out = float(input_data['Pout'])
            p_in = float(input_data['Pin'])
            print(f'{target} = {
                  calculate_efficiency_mo_ei(p_out, p_in)}')


if __name__ == '__main__':
    main()
