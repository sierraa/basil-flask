from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
import os
import logging

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
        return render_template("home.html")

    @app.route("/recipe", methods=["POST", "GET"])
    def add_recipe():
        if request.method == "POST":
            recipe_service.add_recipe(request.form, request.files['file'])
        # TODO probably want to get this from a better source of truth
        cuisines = ["Italian", "Japanese", "Mexican", "Thai", "None"]
        diets = ["Vegetarian", "Vegan", "Low carb", "Pescetarian"]
        tags = ["Healthy", "Quick", "Salad", "Soup"]
        return render_template("new_recipe.html", cuisines=cuisines, diets=diets, tags=tags)

    @app.route("/recipes")
    def recipes_list():
        return render_template("recipes_list.html")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)