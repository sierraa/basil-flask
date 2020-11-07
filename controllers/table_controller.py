from flask_table import Table, Col, LinkCol


class RecipeTable(Table):
    title = Col('Title')
    ingredient1 = Col('Ingredient1')
    ingredient2 = Col('Ingredient2')
    view = LinkCol('View', 'view_recipe', url_kwargs=dict(title="title",ingredient1="ingredient1",ingredient2="ingredient2"))