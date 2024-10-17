from inspect import signature
from math import pi

from data_extraction import MotorStruct


class PropertyRelationship:
    """
    Defines a relationship between two or more properties.

    This is done through the use of a generic lambda which acts as a
    calculation function and must have as many arguments as the requirement
    list.
    """

    def __init__(self, requirements: list[str], fun):
        """
        Constructs a PropertyRelationship object.

        @param requirements: The named requirements of the relationship
        @param fun: The function to apply on the arguments
        """
        self.requirements = requirements
        self.fun = fun
        self.arg_count = len(signature(self.fun).parameters)

    def calculate(self, *kwargs) -> float:
        """
        Applies the given arguments to the calculation function. It is
        imperative that the arguments to this function must have the same
        length as the requirements and thus the lambda's signature parameters.

        @param kwargs: The arguments to apply
        @return: The result of the calculation
        """
        return self.fun(*kwargs[0: self.arg_count])


def binary_product(values: list[str]) -> PropertyRelationship:
    """
    Shorthand to produce a binary property relationship. The requirement list
    must contain two elements.

    @param values: The named requirements
    @return: A property relationship whose function is the product of the
    arguments
    """
    return PropertyRelationship(values, lambda x, y: x * y)


def binary_quotient(values: list[str]) -> PropertyRelationship:
    """
    Shorthand to produce a binary property relationship. The requirement list
    must contain two elements.

    @param values: The named requirements
    @return: A property relationship whose function is the quotient of the
    arguments
    """
    return PropertyRelationship(values, lambda x, y: x / y)


def binary_sum(values: list[str]) -> PropertyRelationship:
    """
    Shorthand to produce a binary property relationship. The requirement list
    must contain two elements.

    @param values: The named requirements
    @return: A property relationship whose function is the sum of the
    arguments
    """
    return PropertyRelationship(values, lambda x, y: x + y)


def binary_difference(values: list[str]) -> PropertyRelationship:
    """
    Shorthand to produce a binary property relationship. The requirement list
    must contain two elements.

    @param values: The named requirements
    @return: A property relationship whose function is the difference of the
    arguments
    """
    return PropertyRelationship(values, lambda x, y: x - y)


PROPERTY_RELATIONSHIPS = {
    "p_out": [
        binary_product(["t", "w"]),
        binary_product(["eff", "p_in"]),
    ],
    "p_in": [
        binary_quotient(["p_out", "eff"]),
        binary_product(["i", "v"]),
    ],
    "eff": [
        binary_quotient(["p_out", "p_in"]),
    ],
    "t": [binary_quotient(["p_out", "w"])],
    "rpm": [
        PropertyRelationship(["w"], lambda x: (x * 60) / (2 * pi)),
    ],
    "w": [
        binary_quotient(["p_out", "t"]),
        PropertyRelationship(["rpm"], lambda x: (x * 2 * pi) / 60),
    ],
    "v": [binary_product(["i", "r"]), binary_quotient(["p_in", "i"])],
    "i": [binary_quotient(["v", "r"]), binary_quotient(["p_in", "v"])],
    "r": [
        binary_quotient(["v", "i"]),
    ],
}


def attempt_to_calculate(target: str, data: MotorStruct) -> float | None:
    """
    Attempts to calculate the given target from existing motor data

    @param target: The named target to calculate
    @param data: The existing data of the motor
    @return: The value, calculated as a floating point number or None if the
    value is not calculable.
    """
    if target in data.properties:
        return data.properties[target]

    relationships = PROPERTY_RELATIONSHIPS[target]
    keys = list(data.properties.keys())

    for relationship in relationships:
        # If the relationship is a valid subset of the keys, then we
        # have enough data to calculate the relationship
        if set(relationship.requirements) <= set(keys):
            req_list = []
            for requirement in relationship.requirements:
                req_list.append(data.properties[requirement])

            return relationship.calculate(*req_list)

    return None


def calculate_possible_targets(data: MotorStruct) -> dict[str, float]:
    """
    Calculates the possible targets for the given motor data.

    @param data: The existing motor data
    @return: A dictionary of the calculated targets. May be empty if no new
    properties could be calculated
    """
    results = {}

    for relationship in PROPERTY_RELATIONSHIPS:
        if relationship in data.properties:
            continue

        res = attempt_to_calculate(relationship, data)

        if res is None:
            continue

        results[relationship] = res

    return results
