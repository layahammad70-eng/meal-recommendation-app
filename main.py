
import os
import requests
import streamlit as st

# FastAPI backend address
API_URL = os.getenv(
    "API_URL",
    "https://meal-recommendation-app.onrender.com"
)
st.set_page_config(
    page_title="My Meal Kitchen",
    page_icon="🍽️"
)

# Website design
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

# Pictures for all 17 dishes
pictures = {
    "Chicken Rice": "images/chicken.jpg",
    "Omelette": "images/Omelette.jpg",
    "Tomato Pasta": "images/tomato-pasta.jpg",
    "Fried Rice": "images/fried-rice.jpg",
    "Fluffy Pancakes": "images/pancakes.jpg",
    "Cheese Sandwich": "images/sandwich.jpg",
    "Chicken Pasta": "images/chicken-pasta.jpg",
    "Pizza": "images/pizza.jpg",
    "Cheeseburger": "images/burger.jpg.jpg",
    "Chicken Tacos": "images/tacos.jpg",
    "Chicken Salad": "images/salad.jpg",
    "Spaghetti Bolognese": "images/bolognese.jpg",
    "Mashed Potatoes": "images/mashed_potatoes.jpg",
    "Tuna Sandwich": "images/tuna_sandwich.jpg",
    "Vegetable Soup": "images/vegetable_soup.jpg",
    "French Toast": "images/french_toast.jpg",
    "Chicken Wrap": "images/chicken_wrap.jpg"
}

# Remember search results
if "meals" not in st.session_state:
    st.session_state.meals = []

st.title("🍽️ My Meal Kitchen")
st.write("Find delicious recipes with ingredients you have!")

user_input = st.text_input(
    "🥕 Enter ingredients separated by commas:",
    placeholder="chicken, rice, cheese"
)

# Search using FastAPI
if st.button("🔍 Find Recipes"):

    ingredients = [
        item.strip().lower()
        for item in user_input.split(",")
        if item.strip()
    ]

    if not ingredients:
        st.warning("Please enter at least one ingredient.")

    else:
        try:
            response = requests.post(
                f"{API_URL}/recommend",
                json={"ingredients": ingredients},
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            st.session_state.meals = data["recommendations"]

        except requests.exceptions.RequestException:
            st.error(
                "Cannot connect to the FastAPI backend. "
                "Make sure the API server is running."
            )

# Show recommendations
if st.session_state.meals:

    st.success("We found recipes for you!")
    st.subheader("🍽️ Choose what you want to cook")

    for result in st.session_state.meals:

        meal = result["meal"]
        percentage = result["match"]

        st.subheader("🍴 " + meal)
        st.write(f"✅ {percentage}% ingredient match")

        picture = pictures.get(meal)

        if picture and os.path.isfile(picture):
            st.image(picture, width=350)
        else:
            st.caption("Picture not found for " + meal)

        if st.button(
            "👩‍🍳 See How to Prepare " + meal,
            key="choose_" + meal
        ):
            st.session_state.selected_meal = meal
            st.switch_page("pages/recipe.py")

        st.divider()

elif user_input:
    st.info("Click Find Recipes to see your options.")
# Recipe match statistics
if st.session_state.meals:
    st.header("📊 Recipe Match Statistics")

    chart_data = {
        result["meal"]: result["match"]
        for result in st.session_state.meals
    }

    st.bar_chart(chart_data, y_label="Ingredient Match (%)")