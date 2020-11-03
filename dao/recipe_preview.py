from dataclasses import dataclass


@dataclass
class RecipePreview:
    title: str
    url: str
    ingredient1: str
    ingredient2: str

    @staticmethod
    def create_preview(ingredient_key, title, url):
        [ingredient1, ingredient2] = ingredient_key.split(",")
        return RecipePreview(title, url, ingredient1, ingredient2)