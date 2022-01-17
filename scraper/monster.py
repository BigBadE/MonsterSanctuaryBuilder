class Monster:
    # Name
    name = None
    # Image
    image = None
    # Light Image
    image_light = None
    # Dark Image
    image_dark = None
    # String locations
    location = []
    # Monster base stats
    stats = None
    # Monster light form base stats
    stats_light = None
    # Monster dark form base stats
    stats_dark = None
    # ID of light ability
    ability_light = -1
    # ID of dark ability
    ability_dark = -1
    # Monster skills, a list containing 4 dictionaries with their tree
    # and one list with ultimates.
    # The tree contains the level required and a list of skill lists
    skills = {}
    # Weaknesses
    weaknesses = []
    # Resistances
    resistances = []
    # Elements
    elements = []

    def __init__(self, name, image, image_light, image_dark, location, stats, stats_light, stats_dark,
                 ability_light, ability_dark, skills, weaknesses, resistances, elements):
        self.name = name
        self.image = image
        self.image_light = image_light
        self.image_dark = image_dark
        self.location = location
        self.stats = stats
        self.stats_light = stats_light
        self.stats_dark = stats_dark
        self.ability_light = ability_light
        self.ability_dark = ability_dark
        self.skills = skills
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.elements = elements

    def to_dict(self):
        return {"image": self.image, "image_light": self.image_light, "image_dark": self.image_dark,
                "location": self.location, "name": self.name,
                "stats": self.stats, "stats_light": self.stats_light, "stats_dark": self.stats_dark,
                "ability_light": self.ability_light, "ability_dark": self.ability_dark, "skills": self.skills,
                "weaknesses": self.weaknesses, "resistances": self.resistances, "elements": self.elements}


divider = "▐"


class Stats:
    stats = [0, 0, 0, 0, 0]

    def __init__(self, bars):
        i = 0
        for stat in bars:
            self.stats[i] = len(stat)
            i += 1

    def to_dict(self):
        return {"attack": self.stats[0], "magic": self.stats[1], "defense": self.stats[2],
                "health": self.stats[3], "mana": self.stats[4]}
