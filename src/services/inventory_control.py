from csv import DictReader
from typing import Dict

from src.models.dish import Recipe
from src.models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


# Req 5
class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    # Req 5.1
    def check_ingredients(self, recipe: Recipe, consume: bool = False):
        for ingredient_name, amount_required in recipe.items():
            inventory_amount = self.inventory[ingredient_name]
            if amount_required > inventory_amount:
                if consume:
                    raise ValueError
                return False
            if consume:
                self.inventory[ingredient_name] -= amount_required
        return True

    def check_recipe_availability(self, recipe: Recipe) -> bool:
        return self.check_ingredients(recipe)

    # Req 5.2
    def consume_recipe(self, recipe: Recipe) -> None:
        self.check_ingredients(recipe, consume=True)
