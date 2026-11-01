
import os
import streamlit as st
from meal_logic import recipes

# Page settings
st.set_page_config(
    page_title="How to Prepare",
    page_icon="👩‍🍳"
)

# Website colors
st.markdown("""
<style>
.stApp {
    background-color: #FFF4E8;
}

.stApp p,
.stApp li,
.stApp span {
    color: #222222 !important;
}

.stApp h1,
.stApp h2,
.stApp h3 {
    color: #A94723 !important;
}

.stButton > button {
    background-color: #E8753D;
    border-radius: 12px;
}

.stButton > button p {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# Pictures for all dishes
pictures = {
    "Chicken Rice": "images/chicken.jpg",
    "Omelette": "images/Omelette.jpg",
    "Tomato Pasta": "images/tomato-pasta.jpg",
    "Fried Rice": "images/fried-rice.jpg",
    "Pancakes": "images/pancakes.jpg",
    "Cheese Sandwich": "images/sandwich.jpg",
    "Chicken Pasta": "images/chicken-pasta.jpg",
    "Pizza": "images/pizza.jpg",
    "Cheeseburger": "images/burger.jpg",
    "Chicken Tacos": "images/tacos.jpg",
    "Chicken Salad": "images/salad.jpg",
    "Spaghetti Bolognese": "images/bolognese.jpg",
    "Mashed Potatoes": "images/mashed_potatoes.jpg",
    "Tuna Sandwich": "images/tuna_sandwich.jpg",
    "Vegetable Soup": "images/vegetable_soup.jpg",
    "French Toast": "images/french_toast.jpg",
    "Chicken Wrap": "images/chicken_wrap.jpg"
}

# Get selected meal
meal = st.session_state.get("selected_meal")

# Back button
if st.button("⬅ Back to Recipes"):
    st.switch_page("main.py")

# Show recipe
if not meal or meal not in recipes:

    st.warning("Please choose a meal first.")

else:

    details = recipes[meal]

    st.title("👩‍🍳 How to Prepare " + meal)

    # Show picture
    picture = pictures.get(meal)

    if picture and os.path.isfile(picture):
        st.image(picture, width=350)

    # Cooking time
    st.header("⏱️ Cooking Time")
    st.write(details["time"])

    # Ingredients
    st.header("🥕 Ingredients")

    for ingredient in details["ingredients"]:
        st.write("• " + ingredient)

    # Cooking instructions
    st.header("🍳 Preparation Steps")

    for number, step in enumerate(details["steps"], 1):
        st.write(f"{number}. {step}")

    st.success("Enjoy your meal! 🍽️")
