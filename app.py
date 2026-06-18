import gradio as gr
import numpy as np
from PIL import Image

from utils.food_detector import detect_food
from utils.nutrition import get_nutrition
from utils.bmi import calculate_bmi
from utils.diet import recommend_diet
from utils.workout import recommend_workout


def predict(age, gender, weight, height, goal, health_issue, food_pref, image):

    image_path = "temp.jpg"
    image.save(image_path)

    # Food detection
    food_name, confidence = detect_food(image_path)

    nutrition = get_nutrition(food_name)
    if nutrition is None:
        nutrition = {"Calories": "N/A", "Protein": "N/A", "Carbs": "N/A", "Fat": "N/A"}

    # BMI
    bmi = calculate_bmi(weight, height)

    if bmi < 18.5:
        bmi_status = "🟡 Underweight"
    elif bmi < 25:
        bmi_status = "🟢 Normal"
    elif bmi < 30:
        bmi_status = "🟠 Overweight"
    else:
        bmi_status = "🔴 Obese"

    diet_plan = recommend_diet(goal)
    workout_plan = recommend_workout(goal)

    return f"""
🍽️ **FOOD RESULT**

Food: **{food_name}**
Confidence: **{round(confidence*100,2)}%**

---

🥗 **NUTRITION**
Calories: {nutrition['Calories']}
Protein: {nutrition['Protein']}
Carbs: {nutrition['Carbs']}
Fat: {nutrition['Fat']}

---

⚖️ **BMI REPORT**
BMI: {round(bmi,2)}
Status: {bmi_status}

---

🥗 **DIET**
{diet_plan}

---

🏋️ **WORKOUT**
{workout_plan}
"""


demo = gr.Interface(
    fn=predict,

    # ================= INPUT UI =================
    inputs=[
        gr.Number(label="Age"),

        gr.Radio(
            choices=["Male", "Female", "Other"],
            label="Gender"
        ),

        gr.Number(label="Weight (kg)"),
        gr.Number(label="Height (cm)"),

        gr.Dropdown(
            choices=["Weight Loss", "Muscle Gain", "Maintenance"],
            label="Fitness Goal"
        ),

        gr.Radio(
            choices=[
                "None",
                "Diabetes",
                "BP",
                "Heart Problem",
                "Thyroid",
                "Other"
            ],
            label="Health Issues"
        ),

        gr.Textbox(
            label="Food Preference (Optional)",
            placeholder="e.g. Vegetarian / Vegan / High Protein / Low Carb"
        ),

        gr.Image(type="pil", label="Upload Food Image")
    ],

    # ================= OUTPUT =================
    outputs=gr.Markdown(label="📊 Your Personalized Report"),

    title="🍎 AI Workout & Diet Planner",
    description="Get Food Prediction + BMI + Diet + Workout Plan in seconds!"
)

demo.launch()