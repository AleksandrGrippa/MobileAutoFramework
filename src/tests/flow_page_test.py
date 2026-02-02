from pages.flow_page import FlowPage
from pages.dialog_permission import DialogPermission
from base_test import BaseTest
from pages.home_page import HomePage
import allure
import pytest

@allure.title("Welcome FLow Page Test")
@allure.tag("Welcome flow")
@pytest.mark.smoke
@pytest.mark.regression
class TestWelcomeFLowPage(BaseTest):
    def test_theFirstStepOfFlowIsOpen_clickNextButton_theSecondStepOpens(self):
        flow_page = FlowPage(self.driver)
        print(self.driver.current_activity)
        flow_page.next_flow_button.click()

        title_text_expected = 'Free, simple, customizable'
        title_text_actual = flow_page.title_flow.text()
        png_bytes = flow_page.capture_screenshot()
        allure.attach(png_bytes, name='screen_{}_test_end_state'.format(self.test_theFirstStepOfFlowIsOpen_clickNextButton_theSecondStepOpens.__name__), attachment_type=allure.attachment_type.PNG, extension=".png")
        
        assert title_text_expected == title_text_actual
        
    
    def test_theSecondStepOfFlowIsOpen_clickNextButton_theThirtyStepOpens(self):

        flow_page = FlowPage(self.driver)
        flow_page.next_flow_button.click()
        flow_page.next_flow_button.click()
        
        title_text_expected = 'Import from contacts'
        title_text_actual = flow_page.title_flow.text()
        
        png_bytes = flow_page.capture_screenshot()
        allure.attach(png_bytes, name='screen_{}_test_end_state'.format(self.test_theSecondStepOfFlowIsOpen_clickNextButton_theThirtyStepOpens.__name__), attachment_type=allure.attachment_type.PNG, extension=".png")
        assert title_text_expected == title_text_actual
    
    # @pytest.mark.welcome_reset(2)
    def test_theThirtyStepOfFlowIsOpen_clickDoneButton_theHomePageOpens(self):
        flow_page = FlowPage(self.driver)
        flow_page.next_flow_button.click()
        flow_page.next_flow_button.click()
        flow_page.done_flow_button.click()
        
        dialog_permission = DialogPermission(self.driver)
        dialog_permission_message_expected = 'Allow Birday to send you notifications?'
        # dialog_permission_message_actual = dialog_permission.dialog_permission_message.text()

        home_page = HomePage(self.driver)
        no_events_text_view_expected = 'No events yet'
        no_events_text_view_actual = home_page.no_events_text_view.text()
        
        png_bytes = flow_page.capture_screenshot()
        allure.attach(png_bytes, name='screen_{}_end_state'.format(self.test_theThirtyStepOfFlowIsOpen_clickDoneButton_theHomePageOpens.__name__), attachment_type=allure.attachment_type.PNG, extension=".png")
        
        assert home_page.no_events_text_view.is_displayed()