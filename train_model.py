from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.applications import MobileNetV2

from tensorflow.keras.layers import (
    Dense,
    GlobalAveragePooling2D,
    Dropout
)

from tensorflow.keras.models import Model


IMG_SIZE = (224, 224)

BATCH_SIZE = 32

EPOCHS = 10


datagen = ImageDataGenerator(
    rescale=1.0/255,
    validation_split=0.2
)


train_generator = datagen.flow_from_directory(
    "dataset/train",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)


validation_generator = datagen.flow_from_directory(
    "dataset/train",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)


base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)


base_model.trainable = False


x = base_model.output

x = GlobalAveragePooling2D()(x)

x = Dropout(0.3)(x)

predictions = Dense(
    train_generator.num_classes,
    activation="softmax"
)(x)


model = Model(
    inputs=base_model.input,
    outputs=predictions
)


model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS
)


model.save(
    "models/food_classifier.keras"
)

print("\nModel Saved Successfully!")