import csv
from models.ingredient import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, encoding="utf-8") as file:
            menu_reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = menu_reader
            self.header = header

            dishes_dict = dict()
            for dish_line in data:
                dish, price, ingredient, recipe_ammount = dish_line
                if dish in dishes_dict:
                    dishes_dict[dish].add_ingredient_dependency(
                        Ingredient(ingredient),
                        int(recipe_ammount)
                    )
                else:
                    dishes_dict[dish] = (Dish(dish, float(price)))
                    dishes_dict[dish].add_ingredient_dependency(
                        Ingredient(ingredient),
                        int(recipe_ammount)
                    )

            self.dishes = set(dishes_dict.values())
