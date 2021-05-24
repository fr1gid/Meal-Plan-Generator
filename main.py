# Nick Hansel

# Web scraper to create a shopping list given recipes

from random_recipe import *

days = {
    "Monday": None,
    "Tuesday": None,
    "Wednesday": None,
    "Thursday": None,
    "Friday": None,
    "Saturday": None,
    "Sunday": None
}

while True:

    answer = input("Would you like to choose a random meal or would you like to schedule your meal plan? ("
                   "schedule/random): ")
    answer = answer.lower()

    if answer == "random":
        randomRecipe()
        print("\n" + "Recipe chosen: " + '\n' + Globals.chosen_recipe[0] + "\n")
        print("Ingredients needed:")
        for x in Globals.final_dict.get(Globals.chosen_recipe[0]):
            print(x)

    elif answer == 'schedule':
        how_many_days = input("How many days would you like to schedule (up to 7 days, starting on Monday): " + '\n')
        how_many_days = int(how_many_days)
        shopping = input('Would you like a shopping list as well? (y/n): ' + '\n')

        if how_many_days <= 7:

            randomRecipe()
            new = (list(days.items()))

            new = ([list(x) for x in new])

            for x in range(how_many_days):
                used = (choice(Globals.names))
                new[x][1] = used
                Globals.names.remove(used)

            del new[how_many_days:]
            new = ([tuple(x) for x in new])
            new = dict(new)

            file1 = open("lunch.txt", 'w')

            for k, v in new.items():
                print(k + ':' + ' ', v + "\n")

        if shopping == 'y':
            file1 = open('Shopping List.txt', 'w')
            for x in new.values():
                for j in Globals.final_dict.get(x):
                    file1.write(j + '\n')
            file1.close()
        break




