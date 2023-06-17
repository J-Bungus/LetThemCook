"""
Scrapes the New York Times Cooking website

I have no idea how this website is structured but there are random
numbers in the url for recipe pages and they range from 9 to 12973
and 1012377 to 1022498. There are randomly missing numbers within those
ranges so I have no idea whats going on, but this program scrapes
as much as possible.
"""

from bs4 import BeautifulSoup as bs
import requests as req

from class_definition import RecipeData, id

BASE_URL = 'https://cooking.nytimes.com/recipes/'

# generate_urls() returns a list of possible urls for recipes by nyt
def generate_urls():
    url_list = []

    for i in range(9, 12974):
        url_list.append(BASE_URL + str(i))

    for i in range (1012377, 1022498):
        url_list.append(BASE_URL + str(i))

    return url_list

# scrape_recipes(url_list) returns a list of RecipeData
def scrape_recipes(url_list):
    global id

    recipes_data= []

    with open('./recipes.csv', 'a') as f:
        for url in url_list:
            print(f"Attempting to Scrape: {url}")

            r = req.get(url)
            soup = bs(r.text, 'html.parser')

            instruction_element = soup.find_all('p', class_='pantry--body-long')
            try :
                time = soup.find('dd', class_='pantry--ui').get_text()
            except AttributeError:
                print(f"No recipe from: {url}")
                continue

            instructions = []

            for element in instruction_element:
                instructions.append(element.get_text())
                
            quantity_element = soup.find('span', class_='ingredient_quantity__wlL75')
            ingredients = []

            while quantity_element:
                ingredient_element = quantity_element.find_next_sibling('span')
                ingredients.append(quantity_element.get_text() + ' ' + ingredient_element.get_text())

                quantity_element = quantity_element.find_next('span', class_='ingredient_quantity__wlL75')

            recipe = RecipeData(id, "Recipe_Name_PLACEHOLDER", ingredients, instructions, url, time)
        
            recipe.write_file(f)
            recipes_data.append(recipe)
            id += 1

        f.close()

    return recipes_data

def nyt_scraper_wrapper():
    recipes = scrape_recipes(generate_urls())

    print("The New York Times scrape has completed!")
    return recipes
