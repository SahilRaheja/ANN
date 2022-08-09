import tensorflow as tf


def create_model(LOSS_FUNCTION, OPTIMIZER, METRICS, EPOCHS, no_classes, input_shape):
    Layers = [
    tf.keras.layers.Flatten(input_shape = input_shape, name = "inputLayer"),
    tf.keras.layers.Dense(300, activation = "relu", name = "hiddenLayer1"),
    tf.keras.layers.Dense(100, activation = "relu", name = "hiddenLayer2"),
    tf.keras.layers.Dense(no_classes, activation = "softmax", name = "outputLayer")
    ]

    model_clf = tf.keras.models.Sequential(Layers)

    model_clf.summary()

    model_clf.compile(loss = LOSS_FUNCTION, optimizer = OPTIMIZER, metrics = METRICS)

    return model_clf   # <<< Untrained model 