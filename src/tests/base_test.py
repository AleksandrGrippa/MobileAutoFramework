import pytest


@pytest.mark.flaky(reruns=0)
@pytest.mark.usefixtures("appium_driver")
class BaseTest:
    pass