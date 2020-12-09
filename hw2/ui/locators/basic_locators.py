from selenium.webdriver.common.by import By

email = 'fcdacyczb@emlpro.com'
password = 'Evelone192'


class BasePageLocators(object):
    signin = (By.XPATH, "//div[text()='Войти' and contains(@class, 'response')]")
    login = (By.XPATH, "//input[contains(@placeholder, 'или номер')]")
    password = (By.XPATH, "//input[@placeholder='Пароль']")
    auth_button = (By.XPATH, "//div[text()='Войти' and contains(@class, 'authForm')]")


class MainPageLocators(BasePageLocators):
    create_company = (By.XPATH, "//div[text()='Создать кампанию']")
    mail_product = (By.XPATH, "//div[contains(text(), 'Продукты Mail.ru')]")
    company_name = (By.XPATH, "(//input[@class='input__inp js-form-element' and @maxlength=255])[1]")
    input_url = (By.XPATH, "//input[@placeholder='Введите ссылку']")
    title = (By.XPATH, "//input[@data-gtm-id='banner_form_title']")
    text = (By.XPATH, "//textarea[@data-gtm-id='banner_form_text']")
    upload_image = (By.XPATH, "//input[@type='file' and contains(@data-gtm-id, 'load_image')]")
    upload_video = (By.XPATH, "//input[@type='file' and contains(@data-gtm-id, 'load_video')]")
    save_image = (By.XPATH, "//input[@value='Сохранить изображение']")
    preview_video = (By.XPATH, "//video[@data-preview-name='preview_video_banner_mob']")
    add_ad = (By.XPATH, "//div[text()='Добавить объявление']")
    settings_cell = (By.XPATH, "//div[contains(@class, 'icon-settings settingsCell')]")
    settings_cell_alt = (By.XPATH, "//a[text()='Реклама Корбена Далласа']")
    delete_company = (By.XPATH, "//ul[contains(@class, 'optionsList-module-optionsList')]/li[text()='Удалить']")


class SegmentsLocators(BasePageLocators):
    classes = (By.XPATH, "//a[text()='Аудитории']")
    create_class = (By.XPATH, "//a[contains(text(), 'Создайте')]")
    alternative_create = (By.XPATH, "//div[text()='Создать сегмент']")
    checkbox = (By.XPATH, "//input[@type='checkbox']")
    add_segment_button = (By.XPATH, "//div[text()='Добавить сегмент']")
    segment_name_input = (By.XPATH, "//input[@maxlength=60]")
    create_segment = (By.XPATH, "//div[text()='Создать сегмент']")
    new_segment_locator = (By.XPATH, "(//a[text()='Сепаратисты'])[1]")
    new_segment_locator_del = (By.XPATH, "(//a[text()='Лейбористы'])[1]")
    segment_menu = (By.XPATH, "(//div[contains(@class, 'select-module-arrow')])[1]")
    delete_segment = (By.XPATH, "//ul[contains(@class, 'optionsList-module-optionsList')]/li[text()='Удалить']")
    segment_checkbox = (By.XPATH, "(//a[text()='Сепаратисты']\
                /ancestor::div[contains(@class, 'main-module-Cell')]\
                /preceding-sibling::div/div/input)[1]")
    segment_checkbox_alt = (By.XPATH, "(//a[text()='Лейбористы']\
                /ancestor::div[contains(@class, 'main-module-Cell')]\
                /preceding-sibling::div/div/input)[1]")
