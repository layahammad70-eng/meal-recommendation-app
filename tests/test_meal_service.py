
import pytest

from backend.meal_service import (
    calculate_match,
    MealRecommendationService
)


# TEST 1: Check ingredient matching
# Test several different situations
@pytest.mark.parametrize(
    "user_ingredients, recipe_ingredients, expected",
    [
        (["chicken", "rice"], ["chicken", "rice"], 100),
        (["chicken"], ["chicken", "rice"], 50),
        (["milk"], ["chicken", "rice"], 0),
        ([], ["chicken", "rice"], 0),
        (["EGGS"], ["eggs", "cheese"], 50),
    ]
)
def test_calculate_match(
    user_ingredients,
    recipe_ingredients,
    expected
):
    result = calculate_match(
        user_ingredients,
        recipe_ingredients
    )

    assert result == expected


# TEST 2: Check empty recipe ingredients
def test_empty_recipe():
    result = calculate_match(
        ["chicken"],
        []
    )

    assert result == 0


# TEST 3: Check recommendation service
def test_recommendation_service():

    class FakeMeal:
        def __init__(self, name, ingredients):
            self.name = name
            self.ingredients = ingredients

    meals = [
        FakeMeal("Chicken Rice", ["chicken", "rice"]),
        FakeMeal("Omelette", ["eggs", "cheese"]),
        FakeMeal("Tomato Pasta", ["tomato", "pasta"])
    ]

    service = MealRecommendationService()

    results = service.recommend(
        meals,
        ["chicken", "rice"]
    )

    assert results == [
        {"meal": "Chicken Rice", "match": 100}
    ]
