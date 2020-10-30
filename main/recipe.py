from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Recipe:
    """
    The hope is to be able to parse all this data from the given URL eventually
    """

    title: str
    url: str
    ingredient_1: str
    ingredient_2: str
    date_added: datetime
    screenshot_url: str
    vegetarian: bool
    vegan: bool
    all_ingredients: List[str]
    notes: str = None
    diets: List[str] = None
    tags: List[str] = None
    source: str = None
    cuisine: str = None