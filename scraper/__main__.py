import json

# To generate shifts
# from shift_list import *
# with open("../data/shifts.json", "w") as file:
   # file.write(json.dumps(get_shifts(), default=Shift.to_dict, indent=4))

# To generate skills
# from skill_list import *

# with open("../data/skills.json", "w") as file:
    # file.write(json.dumps(get_skills(), default=skill.Skill.to_dict, indent=4))

# To generate monsters
from monster import *
from monster_list import *

shifts = {}
skills = {}
with open("../data/shifts.json", "r") as file:
    shifts = json.load(file)

with open("../data/skills.json", "r") as file:
    skills = json.load(file)

with open("../data/monsters.json", "w") as file:
    file.write(json.dumps(get_monsters(shifts, skills), default=Monster.to_dict, indent=4))