from loguru import logger
import yaml


class ConfigProvider:
    def __init__(self):
        self.config: dict = {}

    def load(self, file_path: str = None):
        if not file_path:
            logger.exception("A valid config file path should be specified.")
        self.config = self._from_yaml_file(file_path)
        logger.trace(f"Config dict: {self.config}")

    @staticmethod
    def _from_yaml_file(config_file) -> dict:
        with open(config_file, "r", encoding="utf-8") as f:
            try:
                return yaml.safe_load(f) or {}
            except yaml.YAMLError:
                logger.exception(f"FileConfigLoader filed to load config from {config_file}")
                raise


config_provider = ConfigProvider()
