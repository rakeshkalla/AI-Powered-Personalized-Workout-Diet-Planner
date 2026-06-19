import pandas as pd

food_data = pd.read_csv("nutrition_data.csv")


def get_nutrition(food_name):

    food_name = food_name.lower()

    # Example dataset (you can expand this)
    nutrition_db = {
        "biryani": {
            "Calories": 450,
            "Protein": 20,
            "Carbs": 55,
            "Fat": 18,
            "HealthScore": 5
        },
        "pizza": {
            "Calories": 300,
            "Protein": 12,
            "Carbs": 40,
            "Fat": 10,
            "HealthScore": 4
        },
        "rice": {
            "Calories": 200,
            "Protein": 4,
            "Carbs": 45,
            "Fat": 2,
            "HealthScore": 7
        }
    }

    # default fallback
    data = nutrition_db.get(food_name, {
        "Calories": 250,
        "Protein": 10,
        "Carbs": 30,
        "Fat": 8,
        "HealthScore": 6
    })

    return data

    food_name = food_name.lower()

    row = food_data[
        food_data["Food"].str.lower() == food_name
    ]

    if len(row) == 0:
        return None

    return {
        "Calories": row.iloc[0]["Calories"],
        "Protein": row.iloc[0]["Protein"],
        "Carbs": row.iloc[0]["Carbs"],
        "Fat": row.iloc[0]["Fat"],
        "HealthScore": row.iloc[0]["HealthScore"]
    }