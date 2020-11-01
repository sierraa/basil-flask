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