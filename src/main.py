import time
import random
import argparse
from configuration import configuration as cfg
from sensor import GPIOSensor
import logging
from datetime import datetime
import os

logger = logging.getLogger(__name__)


def setup_logging(config: cfg.Config):
    root = logging.getLogger()
    if config.debug:
        root.setLevel(logging.DEBUG)
    else:
        root.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(config.log_format)
    file_handler = logging.FileHandler(f"{config.log_dir}/{datetime.now().strftime('%m-%d-%Y-%H-%M')}.csv")
    handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    root.addHandler(handler)
    root.addHandler(file_handler)


def ensure_directories(config: cfg.Config):
    """
    Makes sure that the directories specified in environment exist.
    """
    for directory in [config.log_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config',
        nargs='?',
        default="/opt/pikachu/src/configuration/config.cfg",
        type=str,
        required=False,
        help='Path to the configuration file',
        dest='config'
    )
    args = parser.parse_args()
    config = cfg.get_config(args.config)
    ensure_directories(config)
    setup_logging(config)
    device = GPIOSensor(name="device", pin=config.pin, out_mode=True)
    choices = [0, 1]
    while True:
        command = random.choice(choices)
        logger.info(f"Sending command {command}")
        device.update_value(command)
        time.sleep(config.interval)
