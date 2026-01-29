import os
import configparser
from pathlib import Path
from typing import Dict, Any

class ConfigLoader():

    def __init__(self, config_path: str = None):
        if config_path is None:
            project_root = Path(__file__).parent.parent
            config_path = project_root / "utils" / "config" / "config.ini"
        self.config_path = Path(config_path)
        self.config = configparser.ConfigParser()
        
        if self.config_path.exists():
            self.config.read(self.config_path)

    def __get(self, section: str, key: str) -> str:
        if self.config.has_section(section):
            return self.config.get(section, key)
        else:
            raise ValueError(f"Section {section} not found in config file")

    def __get_bool(self, section: str, key: str) -> bool:
        if self.config.has_section(section):
            return self.config.get(section, key).lower() == "true" 
        else:
            raise ValueError(f"Section {section} not found in config file")
    
    def __get_int(self, section: str, key: str) -> int:
        if self.config.has_section(section):
            return int(self.config.get(section, key))
        else:
            raise ValueError(f"Section {section} not found in config file")

    def get_appium_capabilities(self) -> dict:
        capabilities = {
            "deviceName": self.__get("appium", "device_name"),
            "platformName": self.__get("appium", "platform_name"),
            "automationName": self.__get("appium", "automation_name"),
            "platformVersion": self.__get("appium", "platform_version"),
            "appPackage": self.__get("appium", "app_package"),
            # "appActivity": self.__get("appium", "appActivity"),
        } 

        app_path = self.__get('appium', 'app_path')
        if app_path:
            capabilities['app'] = app_path
        
        no_reset = self.__get_bool('appium', 'no_reset')
        if no_reset:
            capabilities['appium:noReset'] = True

        return capabilities