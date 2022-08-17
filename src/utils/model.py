import tensorflow as tf
import time
import os
import pandas as pd
import matplotlib.pyplot as plt


def create_model(LOSS_FUNCTION, OPTIMIZER, METRICS, EPOCHS, no_classes, input_shape):
    Layers = [
        tf.keras.layers.Flatten(input_shape=input_shape, name="inputLayer"),
        tf.keras.layers.Dense(300, activation="relu", name="hiddenLayer1"),
        tf.keras.layers.Dense(100, activation="relu", name="hiddenLayer2"),
        tf.keras.layers.Dense(no_classes, activation="softmax", name="outputLayer")
    ]

    model_clf = tf.keras.models.Sequential(Layers)

    model_clf.summary()

    model_clf.compile(loss=LOSS_FUNCTION, optimizer=OPTIMIZER, metrics=METRICS)

    return model_clf  # Untrained model


def get_unique_filename(filename):
    unique_filename = time.strftime(f"%Y%m%d_%H%M%S_{filename}")
    return unique_filename


def save_model(model, model_name, model_dir):
    unique_filename = get_unique_filename(model_name)
    path_to_model = os.path.join(model_dir, unique_filename)
    model.save(path_to_model)


def save_plots(history, plots_name, plots_dir):
    unique_plots_filename = get_unique_filename(plots_name)
    path_to_plot = os.path.join(plots_dir, unique_plots_filename)
    img = pd.DataFrame(history.history).plot(figsize=(10, 7))#.get_figure().savefig(path_to_plot)
    img.get_figure().savefig(path_to_plot)
    # img.savefig(path_to_plot)

