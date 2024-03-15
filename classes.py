import parameters
import random
import faker
import copy


class RandomHumanoid:
    instances = {}

    def __init__(self, language="eng"):
        self.language = language
        self.race = random.choice(
            [parameters.humanoidRacesStats["Human"]["race"], parameters.humanoidRacesStats["Elf"]["race"],
             parameters.humanoidRacesStats["Dwarf"]["race"], parameters.humanoidRacesStats["Halfing"]["race"]])
        self.self_name()
        self.simpleId = self.simple_id()
        for stat in ["ws", "bs", "s", "t", "ag", "int", "wp", "fel"]:
            setattr(self, stat, parameters.humanoidRacesStats[self.race][stat] + self.generate_main_stat_random())
        self.a = parameters.humanoidRacesStats[self.race]["a"]
        self.w = random.choices(parameters.humanoidRacesStats[self.race]["wValues"],
                                parameters.humanoidRacesStats[self.race]["wWeights"])[0]
        self.sb = (self.s // 10)
        self.tb = (self.t // 10)
        self.m = parameters.humanoidRacesStats[self.race]["m"]
        self.mag = parameters.humanoidRacesStats[self.race]["mag"]
        self.ip = parameters.humanoidRacesStats[self.race]["ip"]
        self.fp = random.choices(parameters.humanoidRacesStats[self.race]["fpValues"],
                                 parameters.humanoidRacesStats[self.race]["fpWeights"])[0]

        RandomHumanoid.instances[self.simpleId] = [self.race, self.name, self.ws, self.bs,
                                              self.s, self.t, self.ag, self.int, self.wp, self.fel,
                                              self.a, self.w, self.sb, self.tb, self.m, self.mag,
                                              self.ip, self.fp]

    @staticmethod
    def generate_main_stat_random():
        MainStatRandomRandrange = 0
        while MainStatRandomRandrange <= 6:
            MainStatRandomRandrange = random.randrange(10) + random.randrange(10)
        return MainStatRandomRandrange

    def self_name(self):

        fakeName = faker.Faker(use_weighting=False)

        if self.race == "Human":
            fakeName.locale = "de_DE"
        elif self.race == "Elf":
            fakeName.locale = "fr_FR"
        elif self.race == "Dwarf":
            fakeName.locale = "no_NO"
        elif self.race == "Halfing":
            fakeName.locale = "nl_NL"

        self.firstName = fakeName.first_name()
        self.lastName = fakeName.last_name()
        self.name = self.firstName + " " + self.lastName

        return self.name

    def __str__(self):
        if self.language in ("ENG", "Eng", "eng", "en", "e"):
            return (f"""
Your random humanoid is: 
    {self.race}, {self.firstName} {self.lastName}
Main characteristics:
    ws:{self.ws}, bs:{self.bs}, s:{self.s}, t:{self.t}, ag:{self.ag}, int:{self.int}, wp:{self.wp}, fel:{self.fel}
Second characteristics:
    a:{self.a}, w:{self.w}, sb:{self.sb}, tb:{self.tb}, m:{self.m}, mag:{self.mag}, ip:{self.ip}, fp:{self.fp}
id:{self.simpleId}
""")
        else:
            return (f"""
Twój losowy humanoid to:
    {self.race}, {self.firstName} {self.lastName}
Cechy główne: 
    ww:{self.ws}, us:{self.bs}, k:{self.s}, odp:{self.t}, zr:{self.ag}, int:{self.int}, sw:{self.wp}, ogd:{self.fel}
Cechy drugorzędne: 
    a:{self.a}, zyw:{self.w}, s:{self.sb}, wt:{self.tb}, sz:{self.m}, mag:{self.mag}, po:{self.ip}, ps:{self.fp}
id:{self.simpleId}
""")

    def simple_id(self):
        simpleId = ''.join([self.firstName[:parameters.simpleIdRules["lenName"]],
                            self.race[:parameters.simpleIdRules["lenRace"]],
                            str(random.randint(111, 999))])
        while simpleId in RandomHumanoid.instances:
            simpleId += str(random.randint(1, 9))
        return simpleId


class StepHumanoid:

    instances = {}

    def __init__(self, race, name, characterClass, classMainStats, bust, language="eng"):
        self.bust = bust
        self.characterClass = self.characterClassChoice(characterClass)
        self.buster()
        self.language = language
        self.race = self.raceChoice(race)
        self.name = self.nameChoice(name, self.race)
        self.simpleId = self.simple_id()
        self.randomStats = self.generate_main_stats_random()
        self.stats = parameters.stats
        self.classStatsChoice(classMainStats)
        self.baseRandomStats = copy.copy(self.randomStats)

        for stat in self.classMainStats:
            setattr(self, stat, max(self.randomStats) + parameters.humanoidRacesStats[self.race][stat]
                    + self.bustMainStats)
            self.randomStats.pop()

        for stat in self.classOtherStats:
            setattr(self, stat, max(self.randomStats) + parameters.humanoidRacesStats[self.race][stat]
                    + self.bustOtherStats)
            self.randomStats.pop()

        self.a = parameters.humanoidRacesStats[self.race]["a"] + self.bustAtack
        self.w = random.choices(parameters.humanoidRacesStats[self.race]["wValues"],
                                parameters.humanoidRacesStats[self.race]["wWeights"])[0] + self.bustWounds
        self.sb = (self.s // 10)
        self.tb = (self.t // 10)
        self.m = parameters.humanoidRacesStats[self.race]["m"]
        self.mag = parameters.humanoidRacesStats[self.race]["mag"]
        self.ip = parameters.humanoidRacesStats[self.race]["ip"]
        self.fp = random.choices(parameters.humanoidRacesStats[self.race]["fpValues"],
                                 parameters.humanoidRacesStats[self.race]["fpWeights"])[0]

        StepHumanoid.instances[self.simpleId] = [self.race, self.name, self.ws, self.bs,
                                                 self.s, self.t, self.ag, self.int, self.wp, self.fel,
                                                 self.a, self.w, self.sb, self.tb, self.m, self.mag,
                                                 self.ip, self.fp, self.characterClass,]

    def raceChoice(self, race):
        if race is not None:
            return race
        else:
            return random.choice(
                [parameters.humanoidRacesStats["Human"]["race"],
                 parameters.humanoidRacesStats["Elf"]["race"],
                 parameters.humanoidRacesStats["Dwarf"]["race"],
                 parameters.humanoidRacesStats["Halfing"]["race"]])

    def nameChoice(self, name, race):
        if name is not None:
            return name
        else:
            fakeName = faker.Faker(use_weighting=False)
            if race == "Human":
                fakeName.locale = "de_DE"
            elif race == "Elf":
                fakeName.locale = "fr_FR"
            elif race == "Dwarf":
                fakeName.locale = "no_NO"
            elif race == "Halfing":
                fakeName.locale = "nl_NL"

            name = f"{fakeName.first_name()} {fakeName.last_name()}"

        return name

    def characterClassChoice(self, characterClass):
        if characterClass is not None:
            return characterClass
        else:
            return random.choice(
                [parameters.humanoidCharacterClasses["Warrior"]["class"],
                 parameters.humanoidCharacterClasses["Swordsman"]["class"],
                 parameters.humanoidCharacterClasses["Marksman"]["class"],
                 parameters.humanoidCharacterClasses["Thief"]["class"],
                 parameters.humanoidCharacterClasses["Intellectual"]["class"],
                 parameters.humanoidCharacterClasses["Magician"]["class"]])

    def classStatsChoice(self, classMainStats):
        if classMainStats is not None:
            self.classMainStats = classMainStats
            self.classOtherStats = [stat for stat in parameters.stats if stat not in self.classMainStats]
        else:
            self.classMainStats = parameters.humanoidCharacterClasses[self.characterClass]["classMainStats"]
            self.classOtherStats = [stat for stat in parameters.stats if stat not in self.classMainStats]


    def buster(self):
        self.bustMainStats = 0
        self.bustOtherStats = 0
        self.bustAtack = 0
        self.bustWounds = 0
        if self.bust == 1:
            self.bustMainStats = parameters.busters["bustersMainStats"][0]
            self.bustOtherStats = parameters.busters["bustersOtherStats"][0]
            if self.characterClass in [parameters.humanoidCharacterClasses["Warrior"]["class"],
                                  parameters.humanoidCharacterClasses["Swordsman"]["class"],
                                  parameters.humanoidCharacterClasses["Marksman"]["class"]]:
                self.bustAtack = parameters.busters["busterAtack"][0]
                self.bustWounds = parameters.busters["busterWounds"][0]
            else:
                self.bustAtack = 0
                self.bustWounds = 0
        elif self.bust == 2:
            self.bustMainStats = parameters.busters["bustersMainStats"][1]
            self.bustOtherStats = parameters.busters["bustersOtherStats"][1]
            if self.characterClass in [parameters.humanoidCharacterClasses["Warrior"]["class"],
                                  parameters.humanoidCharacterClasses["Swordsman"]["class"],
                                  parameters.humanoidCharacterClasses["Marksman"]["class"]]:
                self.bustAtack = parameters.busters["busterAtack"][1]
                self.bustWounds = parameters.busters["busterWounds"][1]
            else:
                self.bustAtack = 0
                self.bustWounds = parameters.busters["busterWounds"][0]
        elif self.bust == 3:
            self.bustMainStats = parameters.busters["bustersMainStats"][2]
            self.bustOtherStats = parameters.busters["bustersOtherStats"][2]
            if self.characterClass in [parameters.humanoidCharacterClasses["Warrior"]["class"],
                                  parameters.humanoidCharacterClasses["Swordsman"]["class"],
                                  parameters.humanoidCharacterClasses["Marksman"]["class"]]:
                self.bustAtack = parameters.busters["busterAtack"][2]
                self.bustWounds = parameters.busters["busterWounds"][2]
            else:
                self.bustAtack = 0
                self.bustWounds = parameters.busters["busterWounds"][1]

    def __str__(self):
        if self.language in ("ENG", "Eng", "eng", "en", "e"):
            return (f"""
Your humanoid is: 
    {self.race}, {self.characterClass}, {self.name} 
Your 8 x 2k10 rolls(after under 6 result rejected):
    {self.baseRandomStats}
Main characteristics:
    ws:{self.ws}, bs:{self.bs}, s:{self.s}, t:{self.t}, ag:{self.ag}, int:{self.int}, wp:{self.wp}, fel:{self.fel}
Second characteristics: 
    a:{self.a}, w:{self.w}, sb:{self.sb}, tb:{self.tb}, m:{self.m}, mag:{self.mag}, ip:{self.ip}, fp:{self.fp}
id:{self.simpleId}
""")
        else:
            return (f"""
Twój humanoid to:
    {self.race}, {self.characterClass}, {self.name} 
Twoje rzuty 8 x 2k10 ( po odrzuceniu wyników poniżej 6)
    {self.baseRandomStats}
Cechy główne: 
    ww:{self.ws}, us:{self.bs}, k:{self.s}, odp:{self.t}, zr:{self.ag}, int:{self.int}, sw:{self.wp}, ogd:{self.fel}
Cechy drugorzędne: 
    a:{self.a}, zyw:{self.w}, s:{self.sb}, wt:{self.tb}, sz:{self.m}, mag:{self.mag}, po:{self.ip}, ps:{self.fp}
id:{self.simpleId}
""")

    @staticmethod
    def generate_main_stat_random():
        MainStatRandomRandrange = 0
        while MainStatRandomRandrange <= 6:
            MainStatRandomRandrange = random.randrange(10) + random.randrange(10)
        return MainStatRandomRandrange

    @staticmethod
    def generate_main_stats_random():
        randomStats = []
        for stat in range(8):
            stat = StepHumanoid.generate_main_stat_random()
            randomStats.append(stat)
        randomStats.sort()
        return randomStats

    def simple_id(self):
        simpleId = ''.join([self.name[:parameters.simpleIdRules["lenName"]],
                            self.race[:parameters.simpleIdRules["lenRace"]],
                            str(random.randint(111, 999))])
        while simpleId in StepHumanoid.instances:
            simpleId += str(random.randint(1, 9))
        return simpleId

