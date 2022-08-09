from utils.common import read_config
from utils.data_mgmt import get_data
from utils.model import create_model

import argparse

def training(config_path):
    config = read_config(config_path)

    validation_data_size = config["params"]["validation_data_size"]

    (X_train, y_train), (X_valid, y_valid ), (X_test, y_test) = get_data(validation_data_size)

    LOSS_FUNCTION=config["params"]["loss_function"]
    OPTIMIZER=config["params"]["optimizer"]
    METRICS=config["params"]["metrics"]
    EPOCHS=config["params"]["epochs"]
    no_classes=config["params"]["no_classes"]
    input_shape=config["params"]["input_shape"]
  
    model = create_model(LOSS_FUNCTION, OPTIMIZER, METRICS, EPOCHS, no_classes, input_shape)

    VALIDATION_SET = (X_valid, y_valid)

    history = model.fit(X_train, y_train, epochs = EPOCHS, validation_data=VALIDATION_SET)

if __name__ == '__main__':

    args = argparse.ArgumentParser()

    args.add_argument("--config","-c", default="config.yaml")

    parsed_args = args.parse_args()

    training(config_path = parsed_args.config)

