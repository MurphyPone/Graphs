from weapon import Weapon, TYPES
import numpy as np
import matplotlib.pyplot as plt
import time
import pprint as pp



stats = {
    "rarity":   {"Common":0, "Uncommon":0, "Unusual":0, "Different": 0, "Rare":0, "Spectacular":0, "Inter-Galactic Trans-Dimensional Turing Complete Relic":0},
    "type":     {"Pistol": 0, "Assault Rifle": 0, "Submachine Gun": 0, "Sniper Rifle": 0, "Light Machine Gun": 0, "Rocket Launcher": 0, "Special": 0},
    "manufacturer": {"Alien": 0, "Imperial": 0, "Rebellion": 0, "One Percent": 0, "Native": 0, "Arch-Tech": 0, "THE 7": 0}
}

# accepts a weapon as input
def update_stats(w):
    stats["rarity"][w.rarity["value"]] += 1
    stats["type"][w.type] += 1
    stats["manufacturer"][w.manufacturer] += 1

def display_stats():
    ind = np.arange(7)    # the x locations for the groups

    p1 = plt.bar(ind*1.5, stats["rarity"].values())

    plt.ylabel('Scores')
    plt.title('Rarity breakdown')
    plt.xticks(ind*1.5, stats["rarity"].keys())

    plt.show()

for i in range(1000):
    w = Weapon()
    print(w)
    update_stats(w)
    time.sleep(0.005)

pp.pprint(stats)
display_stats()
