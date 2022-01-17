class Shift:
    # Name of this shift
    name = ""
    # Description of this shift
    description = ""
    # All monsters with this shift
    monsters = []

    def __init__(self, name, description, monsters):
        self.name = name
        self.description = description
        self.monsters = monsters

    def to_dict(self):
        return {"name": self.name, "description": self.description, "monsters": self.monsters}