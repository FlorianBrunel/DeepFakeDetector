import pathlib
import tensorflow as tf
from tensorflow import keras

data_dir_train = pathlib.Path('C:/Users/flori/Desktop/DataSet2/train')
data_dir_valid = pathlib.Path('C:/Users/flori/Desktop/DataSet2/valid')
data_dir_test = pathlib.Path('C:/Users/flori/Desktop/DataSet2/test')

batch_size = 150
img_height = 200
img_width = 200

train_data = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir_train,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)
val_data = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir_valid,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(img_height, img_width),
    batch_size=batch_size,
)
test_data = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir_test, image_size=(img_height, img_width), batch_size=batch_size
)

class_names = val_data.class_names
print(class_names)

num_classes = len(class_names)

model = tf.keras.Sequential([
    keras.layers.Rescaling(1./255),
    keras.layers.Conv2D(128, 4, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(64, 4, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(32, 4, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(16, 4, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

logdir = "logs"
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir, histogram_freq=1, write_images=True)
model.fit(train_data, validation_data=val_data, epochs=10, callbacks=[tensorboard_callback])

model.summary()
tf.saved_model.save(model, "Model/ModelNewDataSet20E200B2C")

# Évaluation du modèle (aucune modification nécessaire)
test_loss, test_acc = model.evaluate(test_data)
print('Test Loss: {}'.format(test_loss))
print('Test Accuracy: {}'.format(test_acc))
