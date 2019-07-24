import random
from colorama import Fore, Back, Style

TYPES = [
    "Pistol",
    "Assault Rifle",
    "Submachine Gun",
    "Sniper Rifle",
    "Light Machine Gun",
    "Rocket Launcher",
    "Special"
    ]

RANGES = [
    [9, 21],    # pistol
    [19, 31],   # AR
    [15, 28],   # SMG
    [60, 100],  # Sniper
    [27, 35],   # LMG
    [65, 100],  # Launcher
    [0, 100]   # Special
]

ACCURACIES = [
    [1.9, 2.4],    # pistol
    [1.2, 1.7],   # AR
    [2.5, 3.5],   # SMG
    [0, 1],  # Sniper
    [2.4, 2.8],   # LMG
    [3.8, 4.1],  # Launcher
    [0, 5]   # Special
]

RARITIES = [                #name, color, dmg mod
    { "value": "Common", "color":    [255,255,255],  "mod": [-4,-2] }, # white
    { "value": "Uncommon", "color":  [174,255,0],    "mod": [-2,0] }, # green
    { "value": "Unusual", "color":   [183,0,197],    "mod": [0,2] }, # pink
    { "value": "Different", "color": [30,144,245],   "mod": [1,3] }, # blue
    { "value": "Rare", "color":      [238,0,0],      "mod": [3, 5] }, # red
    { "value": "Spectacular", "color":[255, 102, 0], "mod": [5,7]  }, # orange
    { "value": "Inter-Galactic Trans-Dimensional Turing Complete Relic", "color": [100, 100, 100] } # gray
]

MANUFACTURER = [
    "Alien",
    "Imperial",
    "Rebellion",
    "One Percent",
    "Native",
    "Arch-Tech",
    "THE 7"
]

class Weapon:
    def __init__(self):
        i = random.randint(0,len(TYPES)-2) # index used for associated values
        r = random.randint(0,10000) # rarity

        self.type = TYPES[i]
        self.range = random.randint(RANGES[i][0], RANGES[i][1])
        self.damage = None
        self.accuracy = random.uniform(ACCURACIES[i][0], ACCURACIES[i][1])
        self.manufacturer = random.choice(MANUFACTURER[:6])
        self.rarity = None

        if r <= 3500:
            self.rarity = RARITIES[0]    # 35%
        elif r <= 6000:
            self.rarity = RARITIES[1]    # 25%
        elif r <= 8000:
            self.rarity = RARITIES[2]    # 20%
        elif r <= 9000:
            self.rarity = RARITIES[3]    # 10%
        elif r <= 9750:
            self.rarity = RARITIES[4]    # 7.5%
        elif r <= 10000:
            self.rarity = RARITIES[5]    # 5 %

        if r == 7777:
            self.rarity = RARITIES[6]    # 0.01%
            self.type = TYPES[6]         # special
            self.manufacturer = MANUFACTURER[6]  # 7
            self.damage = 77
        else: # add rarity modifier if not a 7
            self.damage = self.range + random.randint(self.rarity["mod"][0], self.rarity["mod"][1])

    def get():
        return {"type": self.type, "range": self.range, "damage":self.damage, "rarity":self.rarity, "manufacturer":self.manufacturer }

    def __str__(self):
        return "{ " + self.type + " | r: " + str(self.range) + " | d: " + str(self.damage) + " | " + self.rarity["value"] + " | " + self.manufacturer + " }"
