from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('ovo')
    assert ingredient.name == 'ovo'
    assert ingredient.__hash__() == hash('ovo')
    assert ingredient.restrictions == {Restriction.ANIMAL_DERIVED}
    assert ingredient.__eq__(Ingredient('carne')) is False
    assert ingredient.__eq__(ingredient) is True
    assert ingredient.__repr__() == "Ingredient('ovo')"
