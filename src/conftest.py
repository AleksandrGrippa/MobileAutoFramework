import pytest
import subprocess
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from utils.config_loader import ConfigLoader
# appium --relaxed-security --allow-insecure=adb_shell

@pytest.fixture(scope="function")
def appium_driver(request):
    # capabilities = {
    #     'deviceName': 'Pixel 9A API 36',
    #     'platformName': 'Android',
    #     'automationName': 'UiAutomator2',
    #     'platformVersion': '16.0',
    #     'appPackage': 'com.minar.birday',
    #     "appium:allowUnauthorizedExecuteShell": True,
    #     'adbExecTimeout': '20000',
    # }
    config = ConfigLoader()
    capabilities = config.get_appium_capabilities()
    driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(capabilities))
    request.cls.driver = driver
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def add_contact():
    path = r"D:\testPython\utils\addContactScript.ps1"
    subprocess.run(["powershell", "-File", path], check=True)