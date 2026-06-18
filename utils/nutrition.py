import pandas as pd

food_data = pd.read_csv("nutrition_data.csv")


def get_nutrition(food_name):

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