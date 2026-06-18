def calculate_bmi(weight, height):
    """
    weight -> kg
    height -> cm
    """

    height = height / 100

    bmi = weight / (height ** 2)

    return round(bmi, 2)