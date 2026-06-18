import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("models/food_classifier.keras")

model = load_model()

# ----------------------------
# UI CONFIG
# ----------------------------
st.set_page_config(page_title="AI Workout & Diet Planner", layout="wide")

st.title("🍎 AI-Powered Workout & Diet Planner")

# ----------------------------
# SIDEBAR NAVIGATION
# ----------------------------
menu = st.sidebar.selectbox(
    "Choose Feature",
    ["Food Detection", "BMI Calculator", "Diet Plan", "Workout Plan"]
)

# ----------------------------
# FOOD DETECTION
# ----------------------------
if menu == "Food Detection":
    st.header("📸 Food Image Classification")

    uploaded_file = st.file_uploader("Upload food image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        st.write("Predicting...")

        img = image.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        result = np.argmax(prediction)

        st.success(f"Predicted Class ID: {result}")

# ----------------------------
# BMI CALCULATOR
# ----------------------------
elif menu == "BMI Calculator":
    st.header("⚖️ BMI Calculator")

    weight = st.number_input("Enter Weight (kg)")
    height = st.number_input("Enter Height (cm)")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / ((height/100) ** 2)

            st.write(f"Your BMI: {bmi:.2f}")

            if bmi < 18.5:
                st.warning("Underweight")
            elif bmi < 24.9:
                st.success("Normal Weight")
            elif bmi < 29.9:
                st.warning("Overweight")
            else:
                st.error("Obese")

# ----------------------------
# DIET PLAN
# ----------------------------
elif menu == "Diet Plan":
    st.header("🥗 Diet Recommendation")

    goal = st.selectbox("Your Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])

    if goal == "Weight Loss":
        st.info("Eat: Vegetables, Fruits, Oats, Protein-rich foods")
    elif goal == "Muscle Gain":
        st.info("Eat: Eggs, Chicken, Paneer, Protein shakes")
    else:
        st.info("Eat balanced diet: Carbs + Protein + Fats")

# ----------------------------
# WORKOUT PLAN
# ----------------------------
elif menu == "Workout Plan":
    st.header("🏋️ Workout Recommendation")

    level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])

    if level == "Beginner":
        st.write("• Walking\n• Pushups\n• Squats")
    elif level == "Intermediate":
        st.write("• Running\n• Dumbbells\n• Planks")
    else:
        st.write("• HIIT\n• Heavy weights\n• Advanced cardio")