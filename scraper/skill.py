class Skill:
    name = ""
    monsters = []
    image = ""
    description = ""

    def __init__(self, name, monsters, image, description):
        self.name = name
        self.monsters = monsters
        self.image = image
        self.description = description

    def to_dict(self):
        return {"name": self.name, "image": self.image, "monsters": self.monsters, "description": self.description}


class AbilitySkill(Skill):
    ultimate = False
    damage = True
    element = ""
    physical = False

    def __init__(self, damage, name, description, monsters, element, physical, image, ultimate):
        super().__init__(name, monsters, image, description)
        self.ultimate = ultimate
        self.damage = damage
        self.element = element
        self.physical = physical

    def to_dict(self):
        return {"name": self.name, "image": self.image, "monsters": self.monsters, "damage": self.damage,
                "element": self.element, "physical": self.physical, "description": self.description}


class PassiveSkill(Skill):
    description = ""

    def __init__(self, name, description, image, monsters):
        super().__init__(name, monsters, image, description)

    def to_dict(self):
        return {"name": self.name, "image": self.image, "monsters": self.monsters, "description": self.description}
