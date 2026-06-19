import os
import numpy as np
import numpy as np

def detect_food(img_path):
    # temporary mock prediction for deployment
    return "biryani", 92.5

# Load trained model
model = load_model("models/food_classifier.keras")

# Automatically read all class names from dataset/train
classes = sorted(
    [
        folder
        for folder in os.listdir("dataset/train")
        if os.path.isdir(os.path.join("dataset/train", folder))
    ]
)

def detect_food(img_path):

    # Load image
    img = image.load_img(
        img_path,
        target_size=(224, 224)
    )

    # Convert image to array
    img_array = image.img_to_array(img)

    # Normalize
    img_array = img_array / 255.0

    # Expand dimensions
    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # Predict
    prediction = model.predict(
        img_array,
        verbose=0
    )

    predicted_index = np.argmax(
        prediction
    )

    confidence = float(
        np.max(prediction) * 100
    )

    food_name = classes[
        predicted_index
    ]

    return food_name, round(confidence, 2)