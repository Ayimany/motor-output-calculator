import m_arg as ma
import m_prop as mp
import m_calc as mc

# Try a correct input such as Target:Eff Pin:15 Pout:14
# Try an incorrect input such as Target:Eff Pout:14

EXIT_FAILURE = 1


def contains_required_properties(available: list[str], reqs: list[str]):
    stat = True

    for element in reqs:
        stat = stat and element in available

    return stat


def main():
    (flags, properties) = ma.setup()
    motor_data = mp.extract_motor_data(properties)

    # TODO: Recursive algorithm to check for composite property calculations
    # TODO: Dynamic property association

    if len(motor_data.targets) > 1:
        print("Heya, I'm gonna stop you right there.",
              "I have made some very poor time management choices and,",
              "for now, I will only let you have one target at a time.")

        print("Sorry for the inconvenience")
        quit(1)

    if motor_data.targets[0] == 'Pout':
        if not contains_required_properties(motor_data.properties,
                                            mp.PROP_REQUIREMENTS['Pout']):
            print('Insufficient data to calculate power output')
            quit(1)

        eff = motor_data.properties['Eff']
        p_in = motor_data.properties['Pin']

        print(f'{mc.calculate_mechanical_output_watts_ef_ei(eff, p_in):.3f}',
              'W')

    if motor_data.targets[0] == 'Eff':
        if not contains_required_properties(motor_data.properties,
                                            mp.PROP_REQUIREMENTS['Eff']):
            print('Insufficient data to calculate efficiency')
            quit(1)

        p_out = motor_data.properties['Pout']
        p_in = motor_data.properties['Pin']

        print(f'{(mc.calculate_efficiency_mo_ei(p_out, p_in)):.3f}', '%')

    if motor_data.targets[0] == 'Pin':
        if not contains_required_properties(motor_data.properties,
                                            mp.PROP_REQUIREMENTS['Pin']):
            print('Insufficient data to calculate power input')
            quit(1)

        eff = motor_data.properties['Eff']
        p_out = motor_data.properties['Pout']

        print(f'{mc.calculate_electrical_input_watts_ef_mo(eff, p_out):.3f}',
              'W')


if __name__ == '__main__':
    main()
