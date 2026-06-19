def recommend_diet(goal, bmi):
    if bmi < 18.5:
        return "High calorie diet: rice, nuts, milk, banana"
    
    elif bmi < 25:
        return "Balanced diet: vegetables, protein, fruits"

    else:
        return "Low calorie diet: salads, fruits, oats"

    if goal == "Weight Loss":

        return [
            "Oats",
            "Apple",
            "Salad",
            "Brown Rice",
            "Green Tea"
        ]

    elif goal == "Muscle Gain":

        return [
            "Eggs",
            "Chicken Breast",
            "Milk",
            "Paneer",
            "Banana"
        ]

    else:

        return [
            "Balanced Diet",
            "Fruits",
            "Vegetables",
            "Whole Grains"
        ]