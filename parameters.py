humanoidRacesStats = {
    "Human": {
        "race": "Human",
        "ws": 20,
        "bs": 20,
        "s": 20,
        "t": 20,
        "ag": 20,
        "int": 20,
        "wp": 20,
        "fel": 20,

        "a": 1,
        "wValues": [10, 11, 12, 13],
        "wWeights": [3, 3, 3, 1],
        "m": 4,
        "mag": 0,
        "ip": 0,
        "fpValues": [2, 3],
        "fpWeights": [4, 6],
    },

    "Elf": {
        "race": "Elf",
        "ws": 20,
        "bs": 30,
        "s": 20,
        "t": 20,
        "ag": 30,
        "int": 20,
        "wp": 20,
        "fel": 20,

        "a": 1,
        "wValues": [10, 11, 12, 13],
        "wWeights": [3, 3, 3, 1],
        "m": 5,
        "mag": 0,
        "ip": 0,
        "fpValues": [1, 2],
        "fpWeights": [4, 6],
    },

    "Dwarf": {
        "race": "Dwarf",
        "ws": 30,
        "bs": 20,
        "s": 20,
        "t": 30,
        "ag": 10,
        "int": 20,
        "wp": 20,
        "fel": 10,

        "a": 1,
        "wValues": [10, 11, 12, 13],
        "wWeights": [3, 3, 3, 1],
        "m": 3,
        "mag": 0,
        "ip": 0,
        "fpValues": [1, 2, 3],
        "fpWeights": [4, 3, 3],
    },

    "Halfing": {
        "race": "Halfing",
        "ws": 10,
        "bs": 30,
        "s": 10,
        "t": 10,
        "ag": 30,
        "int": 20,
        "wp": 20,
        "fel": 30,

        "a": 1,
        "wValues": [10, 11, 12, 13],
        "wWeights": [3, 3, 3, 1],

        "m": 4,
        "mag": 0,
        "ip": 0,
        "fpValues": [2, 3],
        "fpWeights": [7, 3],
    }
}

stats = ["ws", "bs", "s", "t", "ag", "int", "wp", "fel"]

humanoidCharacterClasses = {
    "Warrior": {
        "class": "Warrior",
        "description": "Good in close combat, strong and and durable",
        "classMainStats": ["ws", "s", "t"]
    },
    "Swordsman": {
        "class": "Swordsman",
        "description": "Good in close combat, high agility, durable",
        "classMainStats": ["ws", "ag", "t"]
    },
    "Marksman": {
        "class": "Marksman",
        "description": "Good ballistic skills, high agility and intelligence",
        "classMainStats": ["bs", "ag", "int"]
    },
    "Thief": {
        "class": "Thief",
        "description": "High agility and intelligence, good in close combat",
        "classMainStats": ["ag", "int", "ws"]
    },
    "Intellectual": {
        "class": "Intellectual",
        "description": "High intelligence, fellowship and willpower",
        "classMainStats": ["int", "fel", "wp"]
    },
    "Magician": {
        "class": "Magician",
        "description": "High willpower, intelligence and fellowship",
        "classMainStats": ["wp", "int", "fel"]
    }
}
busters = {
    "bustersMainStats": [10, 25, 40],
    "bustersOtherStats": [5, 10, 15],
    "busterAtack": [0, 1, 2],
    "busterWounds": [2, 4, 8]
}

bustersMainStats = [15, 30, 40]
bustersOtherStats = [5, 10, 15]

"""

racesTuple = "Human", "Elf", "Dwarf", "Halfing"

mainStatsTuple = "ws", "bs", "s", "t", "ag", "int", "wp", "fel"
secondaryStatsTuple = "a", "w", "sb", "tb", "m", "mag", "ip", "fp"



"""
