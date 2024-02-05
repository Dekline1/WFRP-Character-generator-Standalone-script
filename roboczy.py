# Zamiast tego

def random_humanoid():
    howmany = int(input("How many characters do you need?"))
    language = str(input("Should we use ENG or Pl name of parameters?"))
    for _ in range(howmany):
        randomHumanoid = classes.RandomHumanoid(language)
        print(randomHumanoid)
    repeat = str(input("Repeat?"))
    if repeat in ("Tak", "tak", "t", "Yes", "yes", "y"):
        random_humanoid()
    else:
        wait_a_moment()
        main_menu()

# dać coś w ten deseń - chodzi o eliminopwanie zapetlania do samego siebie.

def random_humanoid():
    while True:
        howmany = int(input("How many characters do you need?"))
        language = str(input("Should we use ENG or Pl name of parameters?"))
        for _ in range(howmany):
            randomHumanoid = classes.RandomHumanoid(language)
            print(randomHumanoid)
        repeat = str(input("Repeat?"))
        if repeat in ("Tak", "tak", "t", "Yes", "yes", "y"):
            continue    # w sensie składnia moze nie być ok, ale chodzi o to żę jak klilnie coś z tak to leci
            # random_humanoid jeszcze raz
        else:
            wait_a_moment()
            break   # a tu podobnie, tylko wywala petle, wiec i funkcje random_humanoid i wraca do menu.

# a tu przykład tego żę funkcja powinna sie w wyraźny sposob konczyć

def random_humanoid():
    howmany = int(input("How many characters do you need?"))
    language = str(input("Should we use ENG or Pl name of parameters?"))
    for _ in range(howmany):
        randomHumanoid = classes.RandomHumanoid(language)
        print(randomHumanoid) # widac to zakonczenie bo wydrukuje tyle postaci ile trzeba i finito, funkcja zakończona
