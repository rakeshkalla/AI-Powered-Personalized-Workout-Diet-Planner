from flask import Flask, render_template, request
import os

from utils.food_detector import detect_food
from utils.nutrition import get_nutrition
from utils.bmi import calculate_bmi
from utils.diet import recommend_diet
from utils.workout import recommend_workout

app = Flask(__name__)

# Save uploaded images inside static folder
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        age = request.form["age"]
        gender = request.form["gender"]
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        goal = request.form["goal"]
        health_issue = request.form["health_issue"]
        food_pref = request.form["food_pref"]

        image = request.files["food_image"]

        if image.filename == "":
            return "Please upload an image"

        filename = image.filename

        image_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        image.save(image_path)

        # Food Detection
        food_name, confidence = detect_food(image_path)

        # Nutrition Data
        nutrition = get_nutrition(food_name)

        if nutrition is None:
            nutrition = {
                "Calories": "N/A",
                "Protein": "N/A",
                "Carbs": "N/A",
                "Fat": "N/A"
            }

        # BMI
        bmi = calculate_bmi(weight, height)

        if bmi < 18.5:
            bmi_status = "Underweight"
        elif bmi < 25:
            bmi_status = "Normal"
        elif bmi < 30:
            bmi_status = "Overweight"
        else:
            bmi_status = "Obese"

        # Recommendations
        diet_plan = recommend_diet(goal)
        workout_plan = recommend_workout(goal)

        return render_template(
            "result.html",

            age=age,
            gender=gender,
            goal=goal,
            health_issue=health_issue,
            food_pref=food_pref,

            food_name=food_name,
            confidence=round(confidence, 2),

            calories=nutrition["Calories"],
            protein=nutrition["Protein"],
            carbs=nutrition["Carbs"],
            fat=nutrition["Fat"],

            bmi=round(bmi, 2),
            bmi_status=bmi_status,

            diet_plan=diet_plan,
            workout_plan=workout_plan,

            image_file=filename
        )

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)