import json
from flask import Flask, request, jsonify
import requests
import operator
from pymongo import MongoClient

uri = "mongodb+srv://LetThemCook:dxTjvlN93vMeJ5tE@letthemcookdb.uok4zr6.mongodb.net/?retryWrites=true&w=majority"
url = "https://us-east-1.aws.data.mongodb-api.com/app/data-kfpab/endpoint/data/v1/action/find"
client = MongoClient(uri) # your connection string
db = client["LetThemCook"]
collection = db["Recipe"]

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'saCaksb32gw7usslDUb8C4dAnlCQC9Z21hsMRNCJBy9RG4kNvTFcE0DCI3sDcdvI',
}

app = Flask(__name__)

@app.route('/recommendation', methods=['GET'])
def recommend():
    user_ingredients = request.get_json()

    payload = json.dumps({
    "collection": "Recipes",
    "database": "LetThemCook",
    "dataSource": "LetThemCookDB",
    "limit": 50000
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)

    recipes = response.json()['documents']

    count_list = {}
    counter = 0
    for i, recipe in enumerate(recipes):
        for ingredient in user_ingredients:
            if (ingredient in recipe['IngredientTags']):
                counter += 1
        
        count_list[recipe['RecipeId']] = counter
        counter = 0

    sorted_dict = dict(sorted(count_list.items(), key=operator.itemgetter(1),reverse=True))

    dict_keys = list(sorted_dict.keys())
    return [
        recipes[dict_keys[0]]['Source'],
        recipes[dict_keys[1]]['Source'],
        recipes[dict_keys[2]]['Source'],
        recipes[dict_keys[3]]['Source'],
        recipes[dict_keys[4]]['Source'],
    ]

if __name__ == '__main__':
	app.run(debug=True)