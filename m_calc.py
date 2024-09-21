from inspect import signature
import m_prop as mp


class PropertyRelationship:

    def __init__(self, requirements: list[str], fun):
        self.requirements = requirements
        self.fun = fun
        self.argcount = len(signature(self.fun).parameters)

    def calculate(self, *kwargs) -> float:
        return self.fun(*kwargs[0 : self.argcount])


def proprel_bin_product(values: list[str]) -> PropertyRelationship:
    return PropertyRelationship(values, lambda x, y: x * y)


def proprel_bin_quotient(values: list[str]) -> PropertyRelationship:
    return PropertyRelationship(values, lambda x, y: x / y)


def proprel_bin_sum(values: list[str]) -> PropertyRelationship:
    return PropertyRelationship(values, lambda x, y: x + y)


def proprel_bin_difference(values: list[str]) -> PropertyRelationship:
    return PropertyRelationship(values, lambda x, y: x - y)


PROPERTY_RELATIONSHIPS = {
    "p_out": [
        proprel_bin_product(["t_out", "w_out"]),
        proprel_bin_product(["eff", "p_in"]),
    ],
    "p_in": [proprel_bin_quotient(["p_out", "eff"])],
    "eff": [proprel_bin_quotient(["p_out", "p_in"])],
}


def calculate_target(target: str, properties: dict[str, float]) -> float | None:
    relationships = PROPERTY_RELATIONSHIPS[target]

    if relationships is None:
        print("Null relationship")
        return None

    for relationship in relationships:
        p_exists = True
        props = []

        for property in relationship.requirements:
            p_exists = p_exists and (property in properties)
            props.append(property)

        if p_exists:
            data = []

            for prop in props:
                data.append(properties[prop])

            print(data)

            return relationship.calculate(*data)

    print("Just dumb")
    return None
