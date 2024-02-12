import pathlib
import tensorflow as tf
from tensorflow.keras import layers


#Définition des 
data_dir_train= pathlib.Path('DataSet/Train')
data_dir_valid= pathlib.Path('DataSet/Validation')
data_dir_test = pathlib.Path('DataSet/Test')


batch_size = 30
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
  batch_size=batch_size)


test_data = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir_test,
  image_size=(img_height, img_width),
  batch_size=batch_size,
)


class_names = val_data.class_names
print(class_names)
num_classes = 2



model = tf.keras.Sequential([
                             #Cette couche permet de rendre les valeurs RGB (0-255) en valeur comprise entre 0 et 1
                             layers.experimental.preprocessing.Rescaling(1./255), 
                             
                             
                             # On enchaine ensuite des couche de convolution et de pooling qui permettent de réduire
                             # la taille et condenser les informations pour être facilement interpretable
                             
                             # On a ici 4 couches en réduisant de 2 la résolution de l'image à chaque fois
                             layers.Conv2D(128, 4, activation = 'relu'),
                             layers.MaxPooling2D(),
                             layers.Conv2D(64, 4, activation = 'relu'),
                             layers.MaxPooling2D(),
                             layers.Conv2D(32, 4, activation = 'relu'),
                             layers.MaxPooling2D(),
                             layers.Conv2D(16, 4, activation = 'relu'),
                             layers.MaxPooling2D(),
                             
                             # Permet d'applatir l'image sur une seule dimension interpretable par la suite
                             layers.Flatten(),
                             
                             # Ici se trouve la couche dense constituée de 64 neurones
                             layers.Dense(64, activation = 'relu'),
                             
                             # Enfin c'est ici que seront interprété les données en finalité afin de déterminer l'issu du programme
                             layers.Dense(num_classes, activation = 'softmax')
    ])




model.compile(optimizer='adam', loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
logdir="logs"

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=logdir, histogram_freq=1, write_images=logdir, embeddings_data=train_data)





model.fit(
    train_data,
    validation_data=val_data,
    epochs=10,
    callbacks=[tensorboard_callback
    ])

model.summary()


model.save("Model10Epochs30batch.h5")



test_loss, test_acc = model.evaluate(test_data)
print('Test Loss: {}'.format(test_loss))
print('Test Accuracy: {}'.format(test_acc))



