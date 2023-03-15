import yaml
import logging

from credit_card_validator.exceptions import ConfigFileNotFoundException

LOGGER = logging.getLogger(__name__)


def load_config_from_local_filesystem(config_file_path: str) -> dict:
    try:
        with open(config_file_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        LOGGER.exception("Failed to load config file from YAML file at path: {}".format(config_file_path))
        raise ConfigFileNotFoundException
    except ValueError:
        LOGGER.exception("Unable to parse YAML file contents at path: {}".format(config_file_path))
    except Exception:
        LOGGER.exception("Unable to load contents of config file at path: {}".format(config_file_path))
