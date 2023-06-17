"""
Scrapes the recipes from Ethan Chlebowski's website

He is the GOAT so his website isn't cringe and weird like
the NYT's website.
"""

from bs4 import BeautifulSoup as bs
import time
import requests as req
import unicodedata
import csv

from class_definition import RecipeData, id, SCRAPE_FAIL

BASE_URL = 'https://www.ethanchlebowski.com'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
}

# scrape_page(url) takes in the request object of one page of the 
#    website and returns a list of urls to each recipe and 
#    the names listed on that page (there should be 20 per page)
def scrape_page(r):
    soup = bs(r.text, 'html.parser')

    anchor_elements = soup.find_all('a', class_='BlogList-item-title')
    recipe_urls = []
    recipe_names = []
    for element in anchor_elements:
        recipe_urls.append(BASE_URL + element['href'])
        recipe_names.append(element.get_text())

    return recipe_urls, recipe_names

# scrape_recipe(url) takes in the url of recipe page and
#    returns a RecipeData object
def scrape_recipe(url, recipe_name):
    global id
    print(f"Attempting to Scrape: {url}")
    r = req.get(url, headers=HEADER)
    soup = bs(r.text, 'html.parser')
    
    unordered_elements = soup.find_all('ul')
    ordered_elements = soup.find_all('ol')

    instruction_elements = []
    if not(ordered_elements):
        try: 
            div = soup.find('div', class_='sqs-html-content')
            instruction_section = div.find('h1', string='Instructions')
            instruction_elements = instruction_section.find_next_siblings('p')
        except AttributeError:

            print(f"Could not retrieve recipe information for the recipe at: \n {url}")

            return SCRAPE_FAIL
    else:
        for element in ordered_elements:
            try:
                instruction_elements.extend(element.find_all('li'))
            except AttributeError:

                print(f"Could not retrieve recipe information for the recipe at: \n {url}")

                return SCRAPE_FAIL
    
    instruction_list = []
    for element in instruction_elements:
        instruction_list.append(unicodedata.normalize("NFKD", element.get_text()))

    ingredient_elements = []
    for element in unordered_elements:
        ingredient_elements.extend(element.find_all('li'))
    
    ingredient_list = []
    for element in ingredient_elements:
        ingredient_list.append(unicodedata.normalize("NFKD", element.get_text()))

    recipe = RecipeData(id, recipe_name, ingredient_list, instruction_list, url)
    id += 1

    return recipe

# next_page() takes in the request object of a page and returns the
#    url to go to the next page 
def next_page(r):
    soup = bs(r.text, 'html.parser')

    prev_page_url = soup.find('a', class_='BlogList-pagination-link')

    try:
        next_page_url = prev_page_url.find_next_sibling('a', class_='BlogList-pagination-link')['href']
    except TypeError:
        if (prev_page_url.get_text().strip() == "Older"):
            return BASE_URL + prev_page_url['href']
        else:
            return None

    return BASE_URL + next_page_url

def ec_scraper_wrapper():
    root = 'https://www.ethanchlebowski.com/cooking-techniques-recipes'

    recipes = []

    while(root):
        print(f"Scraping page with URL: {root}")
        r = req.get(root)
        url_list, recipe_names = scrape_page(r)

        with open('./recipes.csv', 'a') as f:
            for i, url in enumerate(url_list):
                recipe = scrape_recipe(url, recipe_names[i])
                recipe.write_file(f)
                recipes.append(recipe)

            f.close
            
        print("Complete.")

        root = next_page(r)

    print("The Ethan Chlebowski personal website scrape as completed!")

    return recipes