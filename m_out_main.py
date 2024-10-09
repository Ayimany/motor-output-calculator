import m_out_argparser as ma
import m_out_dataex as mdex
import m_out_fmt as mfmt
from m_out_calc import calculate_possible_targets
from m_out_fmt import format_as_matrix_nx2

EXIT_FAILURE = 1


def main():
    flags, properties = ma.setup()
    motor_data = mdex.convert_to_motor_data(properties, mfmt.logger)

    while True:
        dataset = calculate_possible_targets(motor_data)
        if len(dataset) == 0:
            break

        motor_data.properties = motor_data.properties | dataset

    print(format_as_matrix_nx2(motor_data))


if __name__ == "__main__":
    main()
