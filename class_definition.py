import csv

id = 0

class RecipeData():
    def __init__(self, recipeID: int, recipe_name: str, ingredients: list[str], instructions: list[str], source_url: str, time: str = ""):
        self.id = recipeID
        self.source = source_url
        self.name = recipe_name
        self.ingredients = ingredients
        self.steps = instructions
        self.time = time

    def get_row(self):
        return [self.id, self.name, self.source, self.time, self.ingredients, self.steps]
    
    def print_data(self):
        print(self.name)
        print(f"RecipeID: {self.id:05}  Time Required: {self.time}")
        print(f"Source: {self.source}")
        print("Ingredients:")
        print("------------")
        ingredients = self.ingredients
        for ingredient in ingredients:
            print(f" - {ingredient}")

        print("Instructions:")
        print("--------------")
        instructions = self.steps
        for i, instruction in enumerate(instructions):
            print(f"{i+1}. {instruction}")
        
        print("----------------------------------------------------------------------------------------------------------------------------")
    
    def write_file(self, f):
        writer = csv.writer(f)

        writer.writerow(self.get_row())
    
    def to_dict(self):
        return {
            "RecipeId": self.id,
            "RecipeName": self.name,
            "Source": self.source,
            "TimeRequired": self.time,
            "Ingredients": self.ingredients,
            "Instructions": self.steps
        }

# Declare constants
SCRAPE_FAIL = RecipeData(-1, "", [], [], "")