import yaml
from pathlib import Path


class Config:
    def __init__(self):
        self.config_path = Path(__file__).parent.parent / "config.yaml"
        self.config = self._load_config()

    def _load_config(self):
        """Load configuration from YAML file"""
        try:
            with open(self.config_path, "r") as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found at {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML file: {e}")

    @property
    def amazon_url(self):
        return self.config["base_urls"]["amazon"]

    @property
    def api_base_url(self):
        return self.config["base_urls"]["api"]

    @property
    def browser_name(self):
        return self.config["browser"]["name"]

    @property
    def browser_headless(self):
        return self.config["browser"]["headless"]

    @property
    def browser_timeout(self):
        return self.config["browser"]["timeout"]

    @property
    def browser_implicit_wait(self):
        return self.config["browser"]["browser_implicit_wait"]

    @property
    def excel_path(self):
        return self.config["test_data"]["excel_path"]

    @property
    def logging_level(self):
        return self.config["logging"]["level"]

    @property
    def logging_format(self):
        return self.config["logging"]["format"]

    @property
    def reports_path(self):
        return self.config["reports"]["path"]

    @property
    def allure_results_path(self):
        return self.config["reports"]["allure_results"]


# Global config instance
config = Config()
