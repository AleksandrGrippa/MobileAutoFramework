import pytest


@pytest.mark.flaky(reruns=2)
@pytest.mark.usefixtures("appium_driver")
class BaseTest:
    pass