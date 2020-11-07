from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
import os
import logging

from controllers.table_controller import RecipeTable
from main.recipe_service import RecipeService


def create_app():
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    logging.basicConfig(level=logging.DEBUG)

    recipe_service = RecipeService(os.getenv("RECIPES_TABLE_NAME"), os.getenv("SCREENSHOTS_BUCKET"),
                                   os.getenv("ACCESS_KEY"), os.getenv("SECRET_KEY"))

    @app.route("/")
    def home():
        # TODO: add edit recipe, delete recipe
        return render_template("home.html")

    @app.route("/recipe", methods=["GET"])
    def view_recipe():
        if not request.args:
            return render_template("404.html")
        recipe = recipe_service.get_recipe(request.args)
        return render_template("view_recipe.html")

    @app.route("/recipe", methods=["POST"])
    def add_recipe():
        recipe_service.add_recipe(request.form, request.files['file'])
        # TODO probably want to get this from a better source of truth
        cuisines = ["Italian", "Japanese", "Mexican", "Thai", "French", "None"]
        diets = ["Vegetarian", "Vegan", "Low carb", "Pescetarian"]
        tags = ["Healthy", "Quick", "Salad", "Soup"]
        return render_template("new_recipe.html", cuisines=cuisines, diets=diets, tags=tags)

    @app.route("/recipes")
    def recipes_list():
        recipes = recipe_service.list_recipes()
        recipe_table = RecipeTable(recipes)
        return render_template("recipes_list.html", recipe_table=recipe_table)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)