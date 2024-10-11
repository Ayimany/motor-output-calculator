from argument_parsing import setup
from calculations import calculate_possible_targets
from data_extraction import convert_to_motor_data
from formatting import (
    logger,
    format_as_matrix_nx2,
    format_as_matrix_nx2_terse,
    print_available_properties,
)


def main():
    flags, properties = setup()
    motor_data = convert_to_motor_data(properties, logger)

    while True:
        dataset = calculate_possible_targets(motor_data)
        if len(dataset) == 0:
            break

        motor_data.properties = motor_data.properties | dataset

    if flags.show_props:
        print_available_properties()
        return 0

    if flags.terse:
        print(format_as_matrix_nx2_terse(motor_data))
    else:
        print(format_as_matrix_nx2(motor_data))


if __name__ == "__main__":
    main()
