import pytest
import subprocess
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from utils.config_loader import ConfigLoader
# appium --relaxed-security --allow-insecure=adb_shell

@pytest.fixture(scope="session")
def ensure_app_installed():
    """
    A fixture for installing the application once per session.
    Checks through ADB, if the application is installed, and installs it only if it is not.
    """
    config = ConfigLoader()
    app_package = config.config.get('appium', 'app_package')
    app_path = config.config.get('appium', 'app_path')
    
    if not app_path:
        yield
        return
    
    # Check if the application is installed
    try:
        result = subprocess.run(
            ['adb', 'shell', 'pm', 'list', 'packages', app_package],
            capture_output=True,
            text=True,
            check=False
        )
        
        # if app is not installed, install it
        if app_package not in result.stdout:
            print(f"App {app_package} not found. Installing...")
            install_result = subprocess.run(
                ['adb', 'install', '-r', app_path],
                capture_output=True,
                text=True,
                check=False
            )
            
            if install_result.returncode != 0:
                print(f"Erorr of installing app: {install_result.stderr}")
                raise Exception(f"Failed to install application: {install_result.stderr}")
            else:
                print(f"App {app_package} has been installed succes.")
        else:
            print(f"App {app_package} has been installed already. Skipping instalation.")
    except Exception as e:
        print(f"Eror while /установке приложения: {e}")
        # Let's continue execution, perhaps Appium will install the application itself

    
    yield

@pytest.fixture(scope="function")
def appium_driver(request, ensure_app_installed):
    """
    A fixture for creating an Appium driver.
    Depends on ensure_app_installed to ensure the app is installed before creating the driver.
    """
    config = ConfigLoader()
    capabilities = config.get_appium_capabilities(include_app=False)
    driver = webdriver.Remote('http://localhost:4723', options=UiAutomator2Options().load_capabilities(capabilities))
    request.cls.driver = driver
    # driver.implicitly_wait(15)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def add_contact():
    path = r"D:\testPython\utils\addContactScript.ps1"
    subprocess.run(["powershell", "-File", path], check=True)