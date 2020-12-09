import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from tests.base import BaseCase

data = {'login': 'fcdacyczb@emlpro.com',
        'password': 'Evelone192'}


class Test(BaseCase):

    @pytest.fixture(scope='session')
    def auth(self):
        self.base_page.authentication(**data)
        return self.main_page

    def test_successful_auth(self):
        self.base_page.authentication(**data)
        assert 'Создать кампанию' in self.driver.page_source

    def test_unsuccessful_auth(self):
        self.base_page.authentication(
            login='fcdacyczb@emlpro.com',
            password='dzgrfdrf',
            timeout=2
        )
        assert 'Invalid login or password' in self.driver.page_source

    def test_create_company(self):
        with allure.step('Выясняем, что там происходит'):
            try:
                self.base_page.authentication(**data)
                self.main_page.create_company()
                assert 'Реклама Корбена Далласа' in self.driver.page_source
                self.main_page.delete_company()
            except Exception:
                allure.attach(name='MainPageCreateCompany',
                              body=self.driver.get_screenshot_as_png(),
                              attachment_type=AttachmentType.PNG)

    def test_create_segment(self):
        self.base_page.authentication(**data)
        self.segments_page.create_segment()
        assert 'Сепаратисты' in self.driver.page_source
        self.segments_page.delete_segment()

    def test_delete_segment(self):
        self.base_page.authentication(**data)
        self.segments_page.create_segment(self.segments_page.segment_name_del)
        assert 'Лейбористы' in self.driver.page_source
        self.segments_page.delete_segment(self.segments_page.segment_name_del)
        assert 'Лейбористы' not in self.driver.page_source

