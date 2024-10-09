import m_out_argparser as ma
import m_out_dataex as mdex
import m_out_fmt as mfmt
from m_out_calc import calculate_possible_targets

EXIT_FAILURE = 1


def main():
    flags, properties = ma.setup()
    motor_data = mdex.convert_to_motor_data(properties, mfmt.logger)

    dataset = calculate_possible_targets(motor_data)

    print(dataset)


if __name__ == "__main__":
    main()
