import time
import classes
import parameters


def wait_a_moment(times=2):
    for _ in range(times):
        time.sleep(0.25)

def repeat():
    repeat = input("Repeat?").strip().lower()
    return repeat in ("tak", "t", "yes", "y")


def random_humanoid():
    while True:
        howmany = int(input("How many characters do you need?"))
        language = str(input("Should we use ENG or Pl name of parameters?"))
        for _ in range(howmany):
            randomHumanoid = classes.RandomHumanoid(language)
            print(randomHumanoid)
        if not repeat():
            wait_a_moment()
            break


def step_humanoid_race():
    chosenRace = int(input(f"""Chose race
    1. {parameters.humanoidRacesStats["Human"]["race"]}
    2. {parameters.humanoidRacesStats["Elf"]["race"]}
    3. {parameters.humanoidRacesStats["Dwarf"]["race"]}
    4. {parameters.humanoidRacesStats["Halfing"]["race"]}
    5. Random
            """))
    if chosenRace == 1:
        race = parameters.humanoidRacesStats["Human"]["race"]
    elif chosenRace == 2:
        race = parameters.humanoidRacesStats["Elf"]["race"]
    elif chosenRace == 3:
        race = parameters.humanoidRacesStats["Dwarf"]["race"]
    elif chosenRace == 4:
        race = parameters.humanoidRacesStats["Halfing"]["race"]
    elif chosenRace == 5:
        race = None
    else:
        race = None
    return race


def step_humanoid_name():
    chosenName = int(input(f"""
How would you like name your character? 
1. Random
2. Myself
"""))
    if (chosenName == 1) or (chosenName in ["random", "Random", "r", "R"]):
        name = None
    else:
        name = str(input("Please type name of your character"))
    return name


def step_humanoid_class():
    chosenCharacterClass = int(input(f"""Firstly choose one of three classes of your future character.

Three chosen attributes will be higher than other ones.

    1. {parameters.humanoidCharacterClasses["Warrior"]["class"]}
            {parameters.humanoidCharacterClasses["Warrior"]["description"]}
            {parameters.humanoidCharacterClasses["Warrior"]["classMainStats"]}
    2. {parameters.humanoidCharacterClasses["Swordsman"]["class"]}
            {parameters.humanoidCharacterClasses["Swordsman"]["description"]}
            {parameters.humanoidCharacterClasses["Swordsman"]["classMainStats"]}
    3. {parameters.humanoidCharacterClasses["Marksman"]["class"]}
            {parameters.humanoidCharacterClasses["Marksman"]["description"]}
            {parameters.humanoidCharacterClasses["Marksman"]["classMainStats"]}
    4. {parameters.humanoidCharacterClasses["Thief"]["class"]}
            {parameters.humanoidCharacterClasses["Thief"]["description"]}
            {parameters.humanoidCharacterClasses["Thief"]["classMainStats"]}
    5. {parameters.humanoidCharacterClasses["Intellectual"]["class"]}
            {parameters.humanoidCharacterClasses["Intellectual"]["description"]}
            {parameters.humanoidCharacterClasses["Intellectual"]["classMainStats"]}
    6. {parameters.humanoidCharacterClasses["Magician"]["class"]}
            {parameters.humanoidCharacterClasses["Magician"]["description"]}
            {parameters.humanoidCharacterClasses["Magician"]["classMainStats"]}
    7. Make it random.
     """))

    if chosenCharacterClass == 1:
        characterClass = parameters.humanoidCharacterClasses["Warrior"]["class"]
    elif chosenCharacterClass == 2:
        characterClass = parameters.humanoidCharacterClasses["Swordsman"]["class"]
    elif chosenCharacterClass == 3:
        characterClass = parameters.humanoidCharacterClasses["Marksman"]["class"]
    elif chosenCharacterClass == 4:
        characterClass = parameters.humanoidCharacterClasses["Thief"]["class"]
    elif chosenCharacterClass == 5:
        characterClass = parameters.humanoidCharacterClasses["Intellectual"]["class"]
    elif chosenCharacterClass == 6:
        characterClass = parameters.humanoidCharacterClasses["Magician"]["class"]
    elif chosenCharacterClass == 7:
        characterClass = None
    else:
        characterClass = None

    return characterClass


def step_humanoid_classMainStats(characterClass):
    if characterClass == parameters.humanoidCharacterClasses["Warrior"]["class"]:
        classMainStats = parameters.humanoidCharacterClasses["Warrior"]["classMainStats"]
    elif characterClass == parameters.humanoidCharacterClasses["Swordsman"]["class"]:
        classMainStats = parameters.humanoidCharacterClasses["Swordsman"]["classMainStats"]
    elif characterClass == parameters.humanoidCharacterClasses["Marksman"]["class"]:
        classMainStats = parameters.humanoidCharacterClasses["Marksman"]["classMainStats"]
    elif characterClass == parameters.humanoidCharacterClasses["Thief"]["class"]:
        classMainStats = parameters.humanoidCharacterClasses["Thief"]["classMainStats"]
    elif characterClass == parameters.humanoidCharacterClasses["Intellectual"]["class"]:
        classMainStats = parameters.humanoidCharacterClasses["Intellectual"]["classMainStats"]
    elif characterClass == parameters.humanoidCharacterClasses["Magician"]["class"]:
        classMainStats = parameters.humanoidCharacterClasses["Magician"]["classMainStats"]
    elif characterClass == None:
        classMainStats = None
    else:
        classMainStats = None

    return classMainStats


def step_humanoid(bust="False"):
    while True:
        race = step_humanoid_race()
        name = step_humanoid_name()
        characterClass = step_humanoid_class()
        classMainStats = step_humanoid_classMainStats(characterClass)
        language = str(input("Should we use ENG or Pl name of parameters?"))
        howmany = int(input("How many characters do you need?"))
        for _ in range(howmany):
            stepHumanoid = classes.StepHumanoid(race, name, characterClass,
                                                classMainStats, language, bust)
            print(stepHumanoid)
        if not repeat():
            wait_a_moment()
            break


def main_menu():
    while True:
        choiceMainMenu = int(input(f"""What would you do?:
        1. {parameters.mainMenu[0]} 
        2. {parameters.mainMenu[1]}
        3. {parameters.mainMenu[2]}
        4. {parameters.mainMenu[3]}
        5. {parameters.mainMenu[4]}
        6. {parameters.mainMenu[5]}
        """))

        if (choiceMainMenu == 1):
            step_humanoid()
        elif (choiceMainMenu == 2):
            random_humanoid()
        elif (choiceMainMenu == 3):
            step_humanoid(bust=1)
        elif (choiceMainMenu == 4):
            step_humanoid(bust=2)
        elif (choiceMainMenu == 5):
            step_humanoid(bust=3)
        elif (choiceMainMenu == 6):
            break
        else:
            print("Please choose 1-6 option")
            wait_a_moment()
            continue


print(parameters.welcomeText)

main_menu()
