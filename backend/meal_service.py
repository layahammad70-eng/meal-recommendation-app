
# FUNCTIONAL PROGRAMMING
# Pure function: same inputs always give the same result.
def calculate_match(user_ingredients, recipe_ingredients):
    user_items = {
        item.strip().lower()
        for item in user_ingredients
    }

    needed = {
        item.strip().lower()
        for item in recipe_ingredients
    }

    if not needed:
        return 0

    matching = len(user_items.intersection(needed))
    return round(matching / len(needed) * 100)


# OBJECT-ORIENTED PROGRAMMING
# This class contains the recommendation behavior.
class MealRecommendationService:

    def __init__(self, minimum_match=1):
        self.minimum_match = minimum_match

    def recommend(self, meals, ingredients):
        results = []

        for meal in meals:
            percentage = calculate_match(
                ingredients,
                meal.ingredients
            )

            if percentage >= self.minimum_match:
                results.append({
                    "meal": meal.name,
                    "match": percentage
                })

        return sorted(
            results,
            key=lambda item: item["match"],
            reverse=True
        )
