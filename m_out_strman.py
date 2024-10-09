import re

VALID_PROPERTIES = {
    "Targets": "targets",
    "Mechanical Power Output": "p_out",
    "Mechanical Power Input": "p_in",
    "Efficiency": "eff",
    "Input Voltage": "v_in",
    "Input Current": "i_in",
    "Input Resistance": "o_in",
    "Output Voltage": "v_out",
    "Output Current": "i_out",
    "Output Resistance": "o_out",
}


def represents_floating_point(what: str) -> bool:
    """Determines whether a string can be parsed as a floating point number or
    not. The usual `isnumeric()` method is not great at recognizing
    floating-point numbers. This method fixes said issue."""

    match = re.match(r"^[-+]?[0-9]*\.?[0-9]+", what)

    if match is None:
        return False

    return match.group() == what
