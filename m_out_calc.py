from inspect import signature

from m_out_dataex import MotorStruct


class PropertyRelationship:

    def __init__(self, requirements: list[str], fun):
        self.requirements = requirements
        self.fun = fun
        self.arg_count = len(signature(self.fun).parameters)

    def calculate(self, *kwargs) -> float:
        return self.fun(*kwargs[0: self.arg_count])


def binary_product(values: list[str]) -> PropertyRelationship:
    return PropertyRelationship(values, lambda x, y: x * y)


def binary_quotient(values: list[str]) -> PropertyRelationship:
    return PropertyRelationship(values, lambda x, y: x / y)


def binary_sum(values: list[str]) -> PropertyRelationship:
    return PropertyRelationship(values, lambda x, y: x + y)


def binary_difference(values: list[str]) -> PropertyRelationship:
    return PropertyRelationship(values, lambda x, y: x - y)


PROPERTY_RELATIONSHIPS = {
    "p_out": [
        binary_product(["t_out", "w_out"]),
        binary_product(["eff", "p_in"]),
    ],
    "p_in": [binary_quotient(["p_out", "eff"])],
    "eff": [binary_quotient(["p_out", "p_in"])],
}


def attempt_to_calculate(target: str, data: MotorStruct) -> float | None:
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
    results = {}
    for relationship in PROPERTY_RELATIONSHIPS:
        res = attempt_to_calculate(relationship, data)

        if res is None:
            continue

        results[relationship] = res

    return results
