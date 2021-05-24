# choose random meals from allrecipes.com
# Add those recipes to meal plan
# Count calories for each recipe


# import dependencies
from bs4 import BeautifulSoup as bs
import requests
from recipe_scrapers import scrape_me
from random import choice

class Globals:
    final_dict = {}
    chosen_recipe = []
    days_needed = []
    names = []


# find links from delish web page
def randomRecipe():
    r = requests.get("https://www.delish.com/cooking/nutrition/g1441/healthy-packed-lunches/?slide=3")
    soup = bs(r.content, 'lxml')
    # parse link
    links = [item['href'] if item.get('href') is not None else item['src'] for item in
             soup.select('[href^="http"], [src^="http"]')]

    recipe_links = []
    ingredients = []

    # ffind valid recipes and ignore rest of links
    for x in links:
        if 'idea' in x:
            recipe_links.append(x)

    recipes = []

    # Scrape necessary data from Delish

    for recipe in recipe_links:
        new = scrape_me(recipe)
        Globals.names.append(new.title())
        recipes.append(new.ingredients())

    # make dictionary with the name of recipe as keys and the ingredients as values
    for i in range(0, len(recipes)):
        Globals.final_dict[Globals.names[i]] = recipes[i]

    # get random recipe name from recipes[]
    # then cross reference with final_dict and find ingredients
    Globals.chosen_recipe.append((choice(Globals.names)))
    # l_ingredients = Globals.final_dict.get(chosen_recipe)
    Globals.names = [x for x in Globals.names if not any(c.isdigit() for c in x)]


