welcomeText = """Welcome in WFRP 2ed character generator
This app helps you generate all playable characters. 
You can do it step by step, or make it totally random,
according to WFRP base handbook. 

Default language is english, you can set up polish in menu
Domyślnym językiem jest angielski, możesz zmienić na polski w menu
"""


mainMenu = ["1. Create humanoid - step by step",
            "2. Create humanoid - random",
            "3. Create busted humanoid - step by step",
            "4. Create double-busted humanoid - step by step",
            "5. Create triple-busted humanoid - step by step",
            "6. Zmień język na polski [in progress]",
            "7. Save to file",
            "8. Exit"]

simpleIdRules = {
                "lenName" : 3,
                "lenRace" : 2
                }
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








racesTuple = "Human", "Elf", "Dwarf", "Halfing"

mainStatsTuple = "ws", "bs", "s", "t", "ag", "int", "wp", "fel"
secondaryStatsTuple = "a", "w", "sb", "tb", "m", "mag", "ip", "fp"




