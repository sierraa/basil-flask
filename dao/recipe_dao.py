import boto3
import logging


class RecipeDao:

    def __init__(self, table_name, access_key, secret_key):
        self.table_name = table_name
        self.ddb = boto3.client('dynamodb')

    def put(self, recipe):
        self.ddb.put_item(TableName=self.table_name,
                          Item=recipe.get_item())
        logging.debug(f"Sucessfully put recipe {recipe.title} in table {self.table_name}")

    def get_recipes(self):
        response = self.ddb.scan(TableName=self.table_name, Limit=100,
                                 AttributesToGet=['Ingredient1,Ingredient2', 'Url', 'Title'],
                                 Select='SPECIFIC_ATTRIBUTES')
        logging.debug(f"Successfully retrieved from table {self.table_name}")
        return response

    def get_recipe(self, title, ingredient1, ingredient2):
        item = self.ddb.get_item(TableName=self.table_name, Key={'Title':  {'S': title},
                                                          'Ingredient1,Ingredient2': {'S': f'{ingredient1},{ingredient2}'}})
        return item