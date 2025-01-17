import random

from dcs.vehicles import AirDefence, Unarmed

from gen.sam.airdefensegroupgenerator import (
    AirDefenseRange,
    AirDefenseGroupGenerator,
)


class GepardGenerator(AirDefenseGroupGenerator):
    """
    This generate a Gepard group
    """

    name = "Gepard Group"
    price = 50

    def generate(self):
        self.add_unit(
            AirDefence.Gepard,
            "SPAAA",
            self.position.x,
            self.position.y,
            self.heading,
        )
        if random.randint(0, 1) == 1:
            self.add_unit(
                AirDefence.Gepard,
                "SPAAA2",
                self.position.x,
                self.position.y,
                self.heading,
            )
        self.add_unit(
            Unarmed.M_818,
            "TRUCK",
            self.position.x + 80,
            self.position.y,
            self.heading,
        )

    @classmethod
    def range(cls) -> AirDefenseRange:
        return AirDefenseRange.Short
