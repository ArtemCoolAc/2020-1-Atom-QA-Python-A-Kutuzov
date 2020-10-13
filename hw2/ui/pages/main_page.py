from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    some_url = 'https://mail.ru'
    video_path = '/home/artemcoolac/Загрузки/ББ_КОРБЕН.mp4'
    image_path = '/home/artemcoolac/Изображения/Korben_Team_less1.jpg'
    title = 'КОРБЕН БИТВА БЛОГЕРОВ'
    company_name = 'Реклама Корбена Далласа'
    text = 'Вступайте за армию Корбена Далласа!'
    locators = MainPageLocators()

    def create_company(self):
        create_button = self.find(self.locators.create_company)
        create_button.click()
        mail_products = self.find(self.locators.mail_product)
        mail_products.click()
        input_url = self.find(self.locators.input_url)
        input_url.send_keys(self.some_url)
        upload_video = self.find(self.locators.upload_video)
        upload_video.send_keys(self.video_path)
        upload_image = self.find(self.locators.upload_image)
        upload_image.send_keys(self.image_path)
        save_image = self.find(self.locators.save_image)
        save_image.click()
        title = self.find(self.locators.title)
        title.send_keys(self.title)
        company_name = self.find(self.locators.company_name)
        company_name.clear()
        company_name.send_keys(self.company_name)
        text = self.find(self.locators.text)
        text.send_keys(self.text)
        add_ad = self.find(self.locators.add_ad)
        add_ad.click()
        preview_video = self.find(self.locators.preview_video)
        create_company_b = self.find(self.locators.create_company)
        create_company_b.click()
        # settings_cell = self.find(self.locators.settings_cell)
        settings_cell = self.find(self.locators.settings_cell_alt)

    def delete_company(self):
        settings_cell = self.find(self.locators.settings_cell)
        settings_cell.click()
        assert self.company_name in self.driver.page_source
        deleting = self.find(self.locators.delete_company)
        deleting.click()
        self.driver.refresh()
        assert self.company_name not in self.driver.page_source
