from src.utils.common import read_config
from src.utils.data_mgmt import get_data

import argparse

def training(config_path):
    config = read_config(config_path)

    validation_data_size = config["params"]["validation_data_size"]

    (X_train_full, y_train_full), (X_valid, y_valid ), (X_test, y_test) = get_data(validation_data_size)
    
    print(config)


if __name__ == '__main__':
    args = argparse.parse_args()

    args.add_argument("--config","-c", default="config.yaml")

    parsed_args = args.parse_args()

    training(config_path = parsed_args.config)

