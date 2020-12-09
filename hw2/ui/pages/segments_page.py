from selenium.common.exceptions import ElementNotInteractableException

from ui.locators.basic_locators import SegmentsLocators
from ui.pages.base_page import BasePage
import time


class SegmentsPage(BasePage):
    locators = SegmentsLocators()
    segment_name = 'Сепаратисты'
    segment_name_del = 'Лейбористы'

    def create_segment(self, name=segment_name):
        time.sleep(2)
        self.find(self.locators.classes).click()
        try:
            class_create_button = self.find(self.locators.create_class)
            class_create_button.click()
        except (ElementNotInteractableException, TimeoutError):
            class_create_button = self.find(self.locators.alternative_create)
            class_create_button.click()

        checkbox_in_creating_class = self.find(self.locators.checkbox)
        checkbox_in_creating_class.click()
        add_segment_button = self.find(self.locators.add_segment_button)
        add_segment_button.click()
        segment_name_input = self.find(self.locators.segment_name_input)
        segment_name_input.clear()
        segment_name_input.send_keys(name)
        create_segment = self.find(self.locators.create_segment)
        create_segment.click()
        segment_locator = self.locators.new_segment_locator \
            if name == 'Сепаратисты' else self.locators.new_segment_locator_del
        new_segment = self.find(segment_locator)

    def delete_segment(self, name=segment_name):
        segment_checkbox = self.locators.segment_checkbox \
            if name == 'Сепаратисты' else self.locators.segment_checkbox_alt
        segment_checkbox = self.find(segment_checkbox)
        segment_checkbox.click()
        segment_menu = self.find(self.locators.segment_menu)
        segment_menu.click()
        delete_segment = self.find(self.locators.delete_segment)
        delete_segment.click()
        time.sleep(1)
