import requests
import json
import requests
import pymongo
from pymongo import MongoClient
from bson import ObjectId
from tqdm import tqdm

url = "https://us-east-1.aws.data.mongodb-api.com/app/data-kfpab/endpoint/data/v1/action/find"
payload = json.dumps({
    "collection": "Recipes",
    "database": "LetThemCook",
    "dataSource": "LetThemCookDB",
    "projection": {
        "_id": 1,
        "Ingredients": 1
    },
    "limit": 50000
})

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': '6XVEJSROSERSKgWgBiMhKfNg61ct916IGTKvgwdQIndP4FEKmqkoL9y2qj6DH1Wu',
}
response = requests.request("POST", url, headers=headers, data=payload)

ingredients = {}
with open("./backend/ingredients.json") as f:
    ingredients = json.load(f)
    f.close()

data = response.json()['documents']
print(len(data))
new_ingredients_list = []
for ingredient_list in tqdm(data):
    ingredient_dict = {
        "_id": ingredient_list["_id"], 
        "Ingredients": [],           
    }
    for ingredient in ingredient_list["Ingredients"]:
        for possible in ingredients:
            if (ingredient.lower().find(possible.lower()) >= 0):
                ingredient_dict["Ingredients"].append(possible)
            
    new_ingredients_list.append(ingredient_dict)


removed_ids = []
for i, ingredient in enumerate(new_ingredients_list):
    if len(data[i]["Ingredients"]) - len(ingredient["Ingredients"]) >= 3:
        new_ingredients_list.remove(ingredient)
        removed_ids.append(ingredient["_id"])

print(len(new_ingredients_list))

uri = "mongodb+srv://LetThemCook:dxTjvlN93vMeJ5tE@letthemcookdb.uok4zr6.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client["LetThemCook"]
collection = db["Recipes"]
ret = collection.find({"_id": '648df42fab6b7bf1a6803f8b'})
print(ret)

id = 0
for ingredient_list in tqdm(new_ingredients_list):
    ret = collection.update_one(
        {"_id": ObjectId(ingredient_list["_id"])},
        {"$set": {
            "RecipeId": id,
            "IngredientTags": ingredient_list["Ingredients"],
        }}
    )
    print(ret.modified_count)
    id += 1

for id in removed_ids:
    ret = collection.delete_one({"_id": ObjectId(id)})
    print(ret.deleted_count)

