import streamlit as st
from PIL import Image

from utils.food_detector import detect_food
from utils.nutrition import get_nutrition
from utils.bmi import calculate_bmi
from utils.diet import recommend_diet
from utils.workout import recommend_workout


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="wide"
)

# ---------------- SIMPLE UI STYLE ----------------
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #00d4ff;
    }
    .sub {
        text-align: center;
        color: gray;
        margin-bottom: 20px;
    }
    .card {
        background-color: #111827;
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown('<div class="title">💪 AI Fitness & Diet Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Upload food image → Get Nutrition + Diet + Workout Plan</div>', unsafe_allow_html=True)

st.markdown("---")


# ---------------- SIDEBAR ----------------
st.sidebar.header("👤 User Profile")

age = st.sidebar.number_input("Age", 10, 100, 20)
weight = st.sidebar.number_input("Weight (kg)", 20, 200, 60)
height = st.sidebar.number_input("Height (cm)", 100, 250, 170)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Weight Gain", "Muscle Gain"]
)

bmi = calculate_bmi(weight, height)

st.sidebar.markdown(f"### 📊 BMI: `{bmi}`")


# ---------------- MAIN ----------------
col1, col2 = st.columns(2)

# ---------- LEFT COLUMN ----------
with col1:
    st.subheader("📤 Upload Food Image")

    uploaded_file = st.file_uploader(
        "Upload JPG / PNG image",
        type=["jpg", "jpeg", "png"]
    )

    food_item = None
    confidence = None

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # FIX: tuple unpacking
        food_item, confidence = detect_food("temp.jpg")

        st.success(f"🍽 Food: {food_item}")
        st.info(f"📊 Confidence: {confidence:.2f}%")

    else:
        st.warning("Please upload an image")


# ---------- RIGHT COLUMN ----------
with col2:
    st.subheader("📊 AI Health Report")

    if uploaded_file and food_item:

        nutrition = get_nutrition(food_item)
        diet = recommend_diet(goal, bmi)
        workout = recommend_workout(goal)

        st.markdown("### 🥗 Nutrition Info")
        st.markdown(f"<div class='card'>{nutrition}</div>", unsafe_allow_html=True)

        st.markdown("### 🍱 Diet Plan")
        st.markdown(f"<div class='card'>{diet}</div>", unsafe_allow_html=True)

        st.markdown("### 🏋️ Workout Plan")
        st.markdown(f"<div class='card'>{workout}</div>", unsafe_allow_html=True)

    else:
        st.info("Upload image to generate AI report")


# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center style='color:gray;'>🚀 AI Powered Fitness System | Streamlit App</center>",
    unsafe_allow_html=True
)