from weapon import Weapon
import numpy as np
import matplotlib.pyplot as plt
import time
import keyboard  # using module keyboard

run = true

stats = {\
    "rarity":   {"Common":0, "Uncommon":0, "Unusual":0, "Different": 0, "Rare":0, "Spectacular":0, "Inter-Galactic Trans-Dimensional Turing Complete Relic":0},
    "type":     {"Pistol": 0, "Assault Rifle": 0, "Submachine Gun", "Sniper Rifle": 0, "Light Machine Gun": 0, "Rocket Launcher": 0, "Special": 0},
    "manufacturer": {"Alien": 0, "Imperial": 0, "Rebellion": 0, "One Percent": 0, "Native": 0, "Arch-Tech": 0, "THE 7": 0}
}

while run:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            run = False
            w = Weapon()


            break  # finishing the loop
        elif keyboard.is_pressed('r'):
            run = True;
            break
