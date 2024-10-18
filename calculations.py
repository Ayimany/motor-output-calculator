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

        # Determine the argument count of the lambda from its signature
        self.arg_count = len(signature(self.fun).parameters)

    def calculate(self, *kwargs) -> float | None:
        """
        Applies the given arguments to the calculation function. It is
        imperative that the arguments to this function must have the same
        length as the requirements and thus the lambda's signature parameters.

        @param kwargs: The arguments to apply
        @return: The result of the calculation
        """

        # Call the calculation lambda
        # Limit the amount of arguments passed to the lambda
        return self.fun(*kwargs[0: self.arg_count])


def binary_product(vals: list[str]) -> PropertyRelationship:
    """
    Shorthand to produce a binary property relationship. The requirement list
    must contain two elements.

    @param vals: The named requirements
    @return: A property relationship whose function is the product of the
    arguments
    """
    return PropertyRelationship(vals, lambda x, y: x * y)


def binary_quotient(vals: list[str]) -> PropertyRelationship:
    """
    Shorthand to produce a binary property relationship. The requirement list
    must contain two elements.

    @param vals: The named requirements
    @return: A property relationship whose function is the quotient of the
    arguments
    """

    # Returns None if the denominator is 0
    return PropertyRelationship(vals, lambda x, y: x / y if y != 0 else None)


def binary_sum(vals: list[str]) -> PropertyRelationship:
    """
    Shorthand to produce a binary property relationship. The requirement list
    must contain two elements.

    @param vals: The named requirements
    @return: A property relationship whose function is the sum of the
    arguments
    """
    return PropertyRelationship(vals, lambda x, y: x + y)


def binary_difference(vals: list[str]) -> PropertyRelationship:
    """
    Shorthand to produce a binary property relationship. The requirement list
    must contain two elements.

    @param vals: The named requirements
    @return: A property relationship whose function is the difference of the
    arguments
    """
    return PropertyRelationship(vals, lambda x, y: x - y)


# Defines how each property is related to one another.
# There are ways to perform algebraic manipulation automatically. As of now,
# these will not be implemented
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
    # If the target has already been calculated, return it
    if target in data.properties:
        return data.properties[target]

    # Obtain the relationships with which the target can be calculated
    relationships = PROPERTY_RELATIONSHIPS[target]
    keys = list(data.properties.keys())

    for relationship in relationships:
        # If the relationship is a valid subset of the keys, then we
        # have enough data to calculate the relationship
        if set(relationship.requirements) <= set(keys):
            req_list = []
            for requirement in relationship.requirements:
                req_list.append(data.properties[requirement])

            # Call the calculation function of the relationship
            return relationship.calculate(*req_list)

    # If the property doesn't exist or can't be calculated, return nothing
    return None


def calculate_possible_targets(data: MotorStruct) -> dict[str, float]:
    """
    Calculates the possible targets for the given motor data.

    @param data: The existing motor data
    @return: A dictionary of the calculated targets. May be empty if no new
    properties could be calculated
    """
    results = {}

    # Attempt to calculate all properties from existing data by name
    for relationship in PROPERTY_RELATIONSHIPS:

        # If the data already exists, skip
        if relationship in data.properties:
            continue

        # Attempt to calculate the relationship by name
        res = attempt_to_calculate(relationship, data)

        # Empty results are not considered
        if res is None:
            continue

        # Populate results
        results[relationship] = res

    return results
