
# Meal database
recipes = {
    "Chicken Rice": {
        "ingredients": ["chicken", "rice"],
        "time": "30 minutes",
        "steps": [
            "Boil the rice until cooked.",
            "Cut chicken into small pieces.",
            "Heat oil in a pan.",
            "Cook chicken until fully cooked.",
            "Serve chicken with rice."
        ]
    },

    "Omelette": {
        "ingredients": ["eggs", "cheese"],
        "time": "10 minutes",
        "steps": [
            "Crack eggs into a bowl.",
            "Beat the eggs with a fork.",
            "Heat oil in a frying pan.",
            "Pour eggs into the pan.",
            "Add cheese and cook until set."
        ]
    },

    "Tomato Pasta": {
        "ingredients": ["tomato", "pasta"],
        "time": "20 minutes",
        "steps": [
            "Boil water in a pot.",
            "Cook pasta until tender.",
            "Chop the tomatoes.",
            "Cook tomatoes in a pan with oil.",
            "Mix the pasta with the tomato sauce."
        ]
    },

    "Fried Rice": {
        "ingredients": ["rice", "eggs"],
        "time": "15 minutes",
        "steps": [
            "Heat oil in a frying pan.",
            "Scramble the eggs.",
            "Add cooked rice.",
            "Stir everything together.",
            "Season and serve."
        ]
    },

    "Pancakes": {
        "ingredients": ["flour", "milk", "eggs"],
        "time": "20 minutes",
        "steps": [
            "Mix flour, milk and eggs in a bowl.",
            "Whisk until smooth.",
            "Heat a lightly oiled pan.",
            "Pour some batter into the pan.",
            "Cook both sides until golden."
        ]
    },

    "Cheese Sandwich": {
        "ingredients": ["bread", "cheese"],
        "time": "5 minutes",
        "steps": [
            "Take two slices of bread.",
            "Place cheese between them.",
            "Heat a frying pan.",
            "Toast the sandwich on both sides.",
            "Serve warm."
        ]
    },

    "Chicken Pasta": {
        "ingredients": ["chicken", "pasta", "cheese"],
        "time": "30 minutes",
        "steps": [
            "Boil pasta until cooked.",
            "Cut chicken into small pieces.",
            "Cook chicken thoroughly in a pan.",
            "Add the cooked pasta.",
            "Mix with cheese and serve."
        ]
    },

    "Pizza": {
        "ingredients": ["dough", "cheese", "tomato"],
        "time": "25 minutes",
        "steps": [
            "Preheat the oven to 220°C.",
            "Spread the dough on a baking tray.",
            "Add tomato sauce and cheese.",
            "Bake until the crust is golden and cooked.",
            "Slice and serve."
        ]
    },

    "Cheeseburger": {
        "ingredients": ["bread", "beef", "cheese"],
        "time": "20 minutes",
        "steps": [
            "Shape the beef into a burger patty.",
            "Cook the beef thoroughly in a pan.",
            "Add cheese on top.",
            "Place the patty inside a burger bun.",
            "Serve warm."
        ]
    },

    "Chicken Tacos": {
        "ingredients": ["chicken", "tortilla", "tomato"],
        "time": "25 minutes",
        "steps": [
            "Cut chicken into small pieces.",
            "Cook the chicken completely.",
            "Chop the tomatoes.",
            "Warm the tortillas.",
            "Fill tortillas with chicken and tomato."
        ]
    },

    "Chicken Salad": {
        "ingredients": ["chicken", "lettuce", "tomato"],
        "time": "20 minutes",
        "steps": [
            "Cook the chicken thoroughly.",
            "Wash and chop the lettuce.",
            "Slice the tomatoes.",
            "Cut the cooked chicken into pieces.",
            "Mix everything together and serve."
        ]
    },

    "Spaghetti Bolognese": {
        "ingredients": ["pasta", "beef", "tomato"],
        "time": "35 minutes",
        "steps": [
            "Boil the spaghetti until cooked.",
            "Cook ground beef thoroughly in a pan.",
            "Add chopped tomatoes.",
            "Simmer the sauce.",
            "Serve the sauce over spaghetti."
        ]
    },

    "Mashed Potatoes": {
        "ingredients": ["potato", "milk", "butter"],
        "time": "25 minutes",
        "steps": [
            "Peel and cut the potatoes.",
            "Boil until soft.",
            "Drain the water.",
            "Add milk and butter.",
            "Mash until smooth."
        ]
    },

    "Tuna Sandwich": {
        "ingredients": ["bread", "tuna", "mayonnaise"],
        "time": "10 minutes",
        "steps": [
            "Drain the tuna.",
            "Mix tuna with mayonnaise.",
            "Take two slices of bread.",
            "Spread the tuna mixture on the bread.",
            "Close the sandwich and serve."
        ]
    },

    "Vegetable Soup": {
        "ingredients": ["carrot", "potato", "onion"],
        "time": "30 minutes",
        "steps": [
            "Wash and chop the vegetables.",
            "Place them in a pot.",
            "Add water and seasoning.",
            "Boil until the vegetables are soft.",
            "Serve warm."
        ]
    },

    "French Toast": {
        "ingredients": ["bread", "eggs", "milk"],
        "time": "15 minutes",
        "steps": [
            "Beat eggs and milk in a bowl.",
            "Dip bread into the mixture.",
            "Heat a lightly oiled pan.",
            "Cook both sides until golden and set.",
            "Serve warm."
        ]
    },

    "Chicken Wrap": {
        "ingredients": ["chicken", "tortilla", "lettuce"],
        "time": "20 minutes",
        "steps": [
            "Cut chicken into small pieces.",
            "Cook chicken completely.",
            "Wash and chop the lettuce.",
            "Place chicken and lettuce on a tortilla.",
            "Roll the tortilla and serve."
        ]
    }
}


# Reusable recommendation function
def recommend_meals(ingredients):
    results = []

    for meal, details in recipes.items():
        needed = details["ingredients"]
        matching = 0

        for item in needed:
            if item in ingredients:
                matching += 1

        percentage = matching / len(needed) * 100

        if matching > 0:
            results.append((meal, round(percentage)))

    return sorted(
        results,
        key=lambda x: x[1],
        reverse=True
    )
