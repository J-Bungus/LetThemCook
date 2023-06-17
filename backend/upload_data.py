import pymongo
from pymongo import MongoClient
import csv
from class_definition import *
from nyt_scraper import nyt_scraper_wrapper
from ethan_scraper import ec_scraper_wrapper

uri = "mongodb+srv://LetThemCook:dxTjvlN93vMeJ5tE@letthemcookdb.uok4zr6.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client["LetThemCook"]
collection = db["Recipes"]
header = ["RecipeId", "RecipeName", "Source", "TimeRequired", "Ingredients", "Steps"]

with open('./recipes.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

recipes = nyt_scraper_wrapper()
recipes = map(lambda x: x.to_dict(), recipes)
collection.insert_many(recipes)

recipes = ec_scraper_wrapper()
recipes = map(lambda x: x.to_dict(), recipes)
collection.insert_many(recipes)
