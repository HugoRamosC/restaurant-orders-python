import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish = Dish("dish_test", 10.10)
    assert dish.name == "dish_test"

    repr_dish = dish.__repr__()
    assert repr_dish == "Dish('dish_test', R$10.10)"
    assert dish.__eq__(Dish("other", 20.20)) is False
    assert dish.__eq__(dish) is True
    assert dish.__hash__() == hash(repr_dish)

    dish.add_ingredient_dependency(Ingredient("ovo"), 30)
    assert dish.get_restrictions() == {Restriction.ANIMAL_DERIVED}
    assert dish.get_ingredients() == {Ingredient("ovo")}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Invalid_price", "not_number")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Invalid_price", -1)
