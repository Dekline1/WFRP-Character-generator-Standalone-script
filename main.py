import time
import classes
import parameters
from Levenshtein import distance as levenshtein
import json


def wait_a_moment(times=2):
    for _ in range(times):
        time.sleep(0.25)


def repeat():
    repeat = input("Repeat?").strip().lower()
    return repeat in ("tak", "t", "yes", "y")


def show_results():
    try:
        if not classes.RandomHumanoid.instances:
            print("No data in Random Humanoid instances")
        else:
            for key, value in classes.RandomHumanoid.instances.items():
                print(key + ": " + ", ".join(map(str, value)))
    except AttributeError:
        print("No definition in Random Humanoid instances")

    try:
        if not classes.StepHumanoid.instances:
            print("No data in Step Humanoid instances")
        else:
            for key, value in classes.StepHumanoid.instances.items():
                print(key + ": " + ", ".join(map(str, value)))
    except AttributeError:
        print("No definition in Step Humanoid instances")


def save_to_file():
    globalInstances = classes.RandomHumanoid.instances.copy()
    globalInstances.update(classes.StepHumanoid.instances)


    print("Chosen character will be save in *.txt file")
    show_results()
    wait_a_moment()
    choice = str(input("Type [id] or save [a]: "))
    if choice.lower() != "a":
        bestMatch = check_id(choice, globalInstances)
        value = globalInstances[bestMatch]
        print("You wrote: " + bestMatch + ": " + ", ".join(map(str, value)))

        with open("Characters.txt", 'a+') as file:
            json.dump((bestMatch + ": " + ", ".join(map(str, value))), file)
            file.write("\n")

    else:
        with open("Characters.txt", 'a+') as file:
            for key, value in globalInstances.items():
                json.dump((key + ": " + ", ".join(map(str, value))), file)
                file.write('\n')


def check_id(choice, globalInstances):
    levenshteinDict = {}
    for key, value in globalInstances.items():
        levenshteinDict[key] = (levenshtein(key.lower(), choice.lower()))
    bestMatch = min(levenshteinDict, key=levenshteinDict.get)
    return bestMatch


def random_humanoid():
    while True:
        howmany = int(input("How many characters do you need?"))
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
        {parameters.mainMenu[0]} 
        {parameters.mainMenu[1]}
        {parameters.mainMenu[2]}
        {parameters.mainMenu[3]}
        {parameters.mainMenu[4]}
        {parameters.mainMenu[5]}
        {parameters.mainMenu[6]}
        {parameters.mainMenu[7]}
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
            global language
            language = "pl"
            continue
        elif (choiceMainMenu == 7):
            save_to_file()
        elif (choiceMainMenu == 8):
            break
        else:
            print("Please choose 1-6 option")
            wait_a_moment()
            continue


print(parameters.welcomeText)
global language
language = "eng"
main_menu()
