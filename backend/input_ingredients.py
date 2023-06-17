"""
Script for organizing inputted ingredients into a JSON file
"""

import json

ingredient = input().lstrip()
seen = []

with open('./ingredients.json', 'r') as f:
    dict = json.load(f)
    f.close()

while ingredient:
    if not(ingredient in seen):
        dict[ingredient] = ingredient
    
    ingredient = input().lstrip()

with open('./ingredients.json', 'w') as f:
    obj = json.dumps(dict, indent=4)
    f.write(obj)
    f.close()