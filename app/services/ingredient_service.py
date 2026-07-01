import json

with open ("app/database/harmful_ingredients.json") as f:
    harmful_db = json.load(f)

def analyze_ingredients(text):
    found =[]

    for ingredient in harmful_db:
        if ingredient.lower() in text.lower():

            found.append({
                "ingredient": ingredient,
                "risk": harmful_db[ingredient]["risk"],
                "description": harmful_db[ingredient]["description"]
            })

    return found