from dataclasses import dataclass
from datetime import datetime
from typing import List
import json


@dataclass
class Recipe:
    """
    The hope is to be able to parse all this data from the given URL eventually
    """
    title: str
    url: str
    ingredient_1: str
    ingredient_2: str
    screenshot_url: str
    vegetarian: bool
    vegan: bool
    all_ingredients: List[str]
    notes: str = None
    diets: List[str] = None
    tags: List[str] = None
    source: str = None
    cuisine: str = None

    def get_partition_key(self):
        return f"{self.ingredient_1},{self.ingredient_2}"

    def get_all_ingredients_json(self):
        return json.dumps({"ingredients": self.all_ingredients})

    def get_all_diets_json(self):
        if not self.diets and self.vegetarian and self.vegan:
            self.diets = ["Vegetarian", "Vegan"]
        elif not self.diets and self.vegetarian:
            self.diets = ["Vegetarian"]
        elif not self.diets and self.vegan:
            self.diets = ["Vegan"]
        if self.diets:
            return json.dumps({"diets": self.diets})
        return None

    def get_all_tags_json(self):
        if self.tags:
            return json.dumps({"tags": self.tags})
        return None

    def get_item(self):
        item = {
            "Ingredient1,Ingredient2": {
                "S": self.get_partition_key()
            },
            "Url": {
                "S": self.url
            },
            "Title": {
                "S": self.title
            },
            "DateAdded": {
                "S": datetime.now().strftime("%m-%d-%Y, %H:%M:%S")
            },
            "ScreenshotUrl": {
                "S": self.screenshot_url
            },
            "Ingredients": {
                "S": self.get_all_ingredients_json()
            }
        }
        diets = self.get_all_diets_json()
        if diets:
            item["Diets"] = {"S": diets}
        tags = self.get_all_tags_json()
        if tags:
            item["Tags"] = {"S": tags}
        if self.source:
            item["Source"] = {"S": self.source}
        if self.cuisine:
            item["Cuisine"] = {"S": self.cuisine}
        if self.notes:
            item["Notes"] = {"S": self.notes}
        return item
