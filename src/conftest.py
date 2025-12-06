import pytest
import subprocess
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
# appium --relaxed-security --allow-insecure=adb_shell

@pytest.fixture(scope="class")
def appium_driver(request):
    capabilities = {
        'deviceName': 'Pixel 9A API 36',
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'platformVersion': '16.0',
        'appPackage': 'com.minar.birday',
        "appium:allowUnauthorizedExecuteShell": True,
        'adbExecTimeout': '20000',
        'appium:noReset': True
    }
    driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(capabilities))
    request.cls.driver = driver
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

@allure.title("Prepare for the test when need to reset apps storage/cache and starts certain welcome's flow step")
@pytest.fixture()
def prepare_welcome_step(request):
    marker = request.node.get_closest_marker("welcome_reset")
    if not marker:
        yield
        return

    driver = request.cls.driver

    driver.execute_script("mobile: shell", {
        "command": "pm",
        "args": ["clear", "com.minar.birday"]
    })
    driver.activate_app("com.minar.birday")

    step = marker.args[0]
    for _ in range(step):
        driver.find_element(AppiumBy.ID, "com.minar.birday:id/next").click()
    yield

    
@pytest.fixture(scope="session")
def add_contact():
    path = r"D:\testPython\utils\addContactScript.ps1"
    subprocess.run(["powershell", "-File", path], check=True)