from dao.recipe import Recipe
from dao.recipe_dao import RecipeDao
from dao.recipe_preview import RecipePreview
from dao.screenshot_dao import ScreenshotDao
from werkzeug.utils import secure_filename


class RecipeService:

    def __init__(self, recipe_table_name, screenshot_bucket_name, access_key, secret_key):
        self.screenshot_dao = ScreenshotDao(screenshot_bucket_name, access_key, secret_key)
        self.recipe_dao = RecipeDao(recipe_table_name, access_key, secret_key)

    def add_recipe(self, form, screenshot_file):
        # TODO: add validation in here
        title = form["title"]
        screenshot_file.filename = secure_filename(screenshot_file.filename)
        screenshot_url = self.screenshot_dao.upload(screenshot_file, title)
        ingredients = self.get_ingredients_list_from_string(form["ingredients"])
        # TODO add optional fields
        recipe = Recipe(title, form["url"], form["ingredient1"], form["ingredient2"], screenshot_url,
                        form.get("Vegetarian", default=False), form.get("Vegan", default=False), ingredients)
        self.recipe_dao.put(recipe)

    def get_ingredients_list_from_string(self, ingredients):
        ingredients_list = ingredients.split(",")
        return [x.strip() for x in ingredients_list]

    def list_recipes(self):
        recipes = self.recipe_dao.get_recipes()["Items"]
        return [RecipePreview.create_preview(self.get_string_attribute("Ingredient1,Ingredient2", recipe),
                                             self.get_string_attribute("Title", recipe),
                                             self.get_string_attribute("Url", recipe)) for recipe in recipes]

    def get_string_attribute(self, attribute_name, item):
        return item[attribute_name]["S"]