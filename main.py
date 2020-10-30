from flask import Flask, render_template, request, flash


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(SECRET_KEY="dev")

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/recipe", methods=["POST", "GET"])
    def add_recipe():
        if request.method == "POST":
            title = request.form["title"]
            recipe_url = request.form["url"]
            error = None
            if not title:
                error = "Title is required."
            if error is not None:
                flash(error)
            else:
                # Write to the DB
                pass
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