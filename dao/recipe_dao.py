import boto3

class RecipeDao:

    def __init__(self, table_name, access_key, secret_key):
        self.table_name = table_name
        self.ddb = boto3.client('dynamodb', aws_access_key=access_key, aws_secret_key_id=secret_key)

    def put(self, recipe):
        self.ddb.put_item(TableName=self.table_name,
                          Item=recipe.get_item())