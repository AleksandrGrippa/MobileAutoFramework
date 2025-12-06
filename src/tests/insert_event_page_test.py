from base_test import BaseTest
from pages.home_page import HomePage
from pages.insert_event_page import InsertEventPage
from utils.data_generator import DataGenerator
from pages.flow_page import FlowPage
from pages.dialog_permission import DialogPermission
import allure

class TestAddEvent(BaseTest):
    def test_homePageIsOpen_addEventWithCorrectData_eventAdded(self):
        flow_page = FlowPage(self.driver)
        dialog_permission = DialogPermission(self.driver)
        insert_event_page = InsertEventPage(self.driver)
        home_page = HomePage(self.driver)
        
        dialog_permission.dont_allow_permission_button.click()
        dialog_permission.dont_allow_permission_button.click()
        home_page.insert_event_button.click()
        dialog_permission.allow_permission_button.click()
        insert_event_page.cancel_import_contact_button.click()
        random_date = DataGenerator.get_random_date()
        insert_event_page.fill_event_form('Birthday', 'Sasha', 'Grippa', random_date)
        button_displayed = insert_event_page.create_event_button.is_enabled()
        print(button_displayed)
        insert_event_page.create_event_button.click()
        
        png_bytes = flow_page.capture_screenshot()
        allure.attach(png_bytes, name='screen_{}_test_end_state'.format(self.test_homePageIsOpen_addEventWithCorrectData_eventAdded.__name__), attachment_type=allure.attachment_type.PNG, extension=".png")
        
        assert home_page.event_element(1).is_displayed() == True
        
    def test_homePageIsOpen_addEventWithoutName_CreateEventButtonIsNotEnabled(self):
        home_page = HomePage(self.driver)
        insert_event_page = InsertEventPage(self.driver)
        
        home_page.insert_event_button.click()
        random_date = DataGenerator.get_random_date()
        
        insert_event_page.fill_event_form('Birthday', '', 'Grippa', random_date)
        
        button_displayed = insert_event_page.create_event_button.is_enabled()
        
        png_bytes = insert_event_page.capture_screenshot()
        allure.attach(png_bytes, name='screen_{}_test_end_state'.format(self.test_homePageIsOpen_addEventWithoutName_CreateEventButtonIsNotEnabled.__name__), attachment_type=allure.attachment_type.PNG, extension=".png")
        
        assert button_displayed == False