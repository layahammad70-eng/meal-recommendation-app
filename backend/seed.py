
from backend.database import Base, engine, SessionLocal
from backend.models import Recipe
from meal_logic import recipes


def seed_database():
    # Create the recipes table
    Base.metadata.create_all(bind=engine)

    # Open a database session
    db = SessionLocal()

    try:
        for name, details in recipes.items():

            # Check if the recipe already exists
            existing = db.query(Recipe).filter(
                Recipe.name == name
            ).first()

            if existing is None:
                new_recipe = Recipe(
                    name=name,
                    ingredients=details["ingredients"],
                    cooking_time=details["time"],
                    steps=details["steps"]
                )

                db.add(new_recipe)

        # Save all new recipes
        db.commit()

        total = db.query(Recipe).count()
        print(f"Success! {total} recipes in the database.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
