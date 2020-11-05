from flask_table import Table, Col


class RecipeTable(Table):
    title = Col('Title')
    url = Col('Url')
    ingredient1 = Col('Ingredient1')
    ingredient2 = Col('Ingredient2')
