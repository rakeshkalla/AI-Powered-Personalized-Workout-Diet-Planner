def recommend_workout(goal):

    if goal == "Weight Loss":

        return [
            "Running - 30 mins",
            "Cycling - 20 mins",
            "Skipping - 15 mins",
            "Walking - 30 mins"
        ]

    elif goal == "Muscle Gain":

        return [
            "Pushups",
            "Pullups",
            "Squats",
            "Bench Press",
            "Deadlift"
        ]

    else:

        return [
            "Walking",
            "Stretching",
            "Yoga"
        ]