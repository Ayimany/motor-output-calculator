import m_arg as ma
import m_prop as mp
import m_calc as mc
import m_fmt
import sys

EXIT_FAILURE = 1


def main():
    (flags, properties) = ma.setup()
    motor_data = mp.extract_motor_data(properties, m_fmt.logger)

    for target in motor_data.targets:
        target_value = mc.calculate_target(target, motor_data.properties)

        if target_value is None:
            print(
                f"Could not calculate {target}. Please check for any errors.",
                file=sys.stderr,
            )

        print(target, ": ", target_value)


if __name__ == "__main__":
    main()
