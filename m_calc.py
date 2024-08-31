
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
