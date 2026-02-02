from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BaseElement():
    def __init__(self, driver, locator, timeout = 10, cache_ttl = 2):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.cache_ttl = cache_ttl  # Cache time-to-live in seconds
        self._cached_element = None
        self._cache_timestamp = None
    

    def find(self, use_cache=True):
        """
        Find the element, with optional caching to avoid repeated find() calls.
        
        Args:
            use_cache: If True, use cached element if still valid (within cache_ttl)
        
        Returns:
            WebElement: The found element
        """
        # Check if we have a valid cached element
        if use_cache and self._cached_element is not None and self._cache_timestamp is not None:
            elapsed = time.time() - self._cache_timestamp
            if elapsed < self.cache_ttl:
                try:
                    # Verify element is still attached to DOM
                    _ = self._cached_element.is_displayed()
                    return self._cached_element
                except:
                    # Element is stale, clear cache and find again
                    self._cached_element = None
                    self._cache_timestamp = None
        
        # Find element and cache it
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((self.locator)))

        
        if use_cache:
            self._cached_element = element
            self._cache_timestamp = time.time()
        
        return element
    
    def _clear_cache(self):
        """Clear the cached element (useful when element might be recreated)."""
        self._cached_element = None
        self._cache_timestamp = None
    
    def click(self):
        el = self.find()
        el.click()

    def text(self):
        el = self.find()
        return el.text
    
    def is_displayed(self):
        el = self.find()
        return el.is_displayed()
    
    def is_enabled(self):
        el = self.find()
        return el.is_enabled()