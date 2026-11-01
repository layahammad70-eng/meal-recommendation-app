
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from backend.database import get_db, Base, engine
from backend.models import Recipe
from backend.meal_service import MealRecommendationService
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Meal Kitchen API",
    description="Meal Recommendation Backend",
    version="2.0"
)


# Validate new recipe information
class RecipeCreate(BaseModel):
    name: str = Field(min_length=1)
    ingredients: list[str] = Field(min_length=1)
    cooking_time: str = Field(min_length=1)
    steps: list[str] = Field(min_length=1)


# Validate ingredient searches
class IngredientRequest(BaseModel):
    ingredients: list[str] = Field(min_length=1)


# Convert a database recipe to JSON
def recipe_to_dict(recipe):
    return {
        "id": recipe.id,
        "name": recipe.name,
        "ingredients": recipe.ingredients,
        "cooking_time": recipe.cooking_time,
        "steps": recipe.steps
    }


# Endpoint 1: List all recipes
@app.get("/meals")
def get_meals(db: Session = Depends(get_db)):
    meals = db.query(Recipe).all()

    return {
        "meals": [recipe_to_dict(meal) for meal in meals],
        "total": len(meals)
    }


# Endpoint 2: Recommend meals

@app.post("/recommend")
def recommend(
    request: IngredientRequest,
    db: Session = Depends(get_db)
):
    ingredients = [
        item.strip().lower()
        for item in request.ingredients
        if item.strip()
    ]

    if not ingredients:
        raise HTTPException(
            status_code=400,
            detail="Please enter valid ingredients"
        )

    # PROCEDURAL PROGRAMMING
    # 1. Read recipes from the database
    meals = db.query(Recipe).all()

    # 2. Create the recommendation service
    service = MealRecommendationService()

    # 3. Calculate recommendations
    results = service.recommend(meals, ingredients)

    # 4. Return results to Streamlit
    return {"recommendations": results}


# Endpoint 3: Add a new recipe
@app.post("/meals", status_code=201)
def add_meal(
    recipe: RecipeCreate,
    db: Session = Depends(get_db)
):
    name = recipe.name.strip()

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Recipe name cannot be empty"
        )

    existing = db.query(Recipe).filter(
        Recipe.name == name
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="This recipe already exists"
        )

    new_recipe = Recipe(
        name=name,
        ingredients=recipe.ingredients,
        cooking_time=recipe.cooking_time,
        steps=recipe.steps
    )

    try:
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Could not save recipe"
        )

    return recipe_to_dict(new_recipe)


# Endpoint 4: Get one recipe
@app.get("/meals/{meal_name}")
def get_recipe(
    meal_name: str,
    db: Session = Depends(get_db)
):
    meal = db.query(Recipe).filter(
        Recipe.name == meal_name
    ).first()

    if not meal:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )

    return recipe_to_dict(meal)

# Endpoint 5: Delete Creamy Chicken Pasta
@app.delete("/meals/creamy-chicken-pasta")
def delete_creamy_pasta(db: Session = Depends(get_db)):
    meal = db.query(Recipe).filter(
        Recipe.name == "Creamy Chicken Pasta"
    ).first()

    if not meal:
        raise HTTPException(
            status_code=404,
            detail="Creamy Chicken Pasta not found"
        )

    db.delete(meal)
    db.commit()

    return {"message": "Creamy Chicken Pasta deleted successfully"}

