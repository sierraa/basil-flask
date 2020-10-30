from dao.screenshot_dao import ScreenshotDao


class RecipeService:

    def __init__(self, recipe_table_name, screenshot_bucket_name, access_key, secret_key):
        self.screenshot_dao = ScreenshotDao(screenshot_bucket_name, access_key, secret_key)