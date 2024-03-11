from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.locators import RegisterLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# создание класса формы регистрации
class RegistrationForm(BasePage):

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout)

        url = "https://koshelek.ru/authorization/signup"
        driver.get(url)

        self.driver = driver

        # ожидаем формирование DOM и теневого участка в нем
        shadow_host = WebDriverWait(driver, 20).until(EC.presence_of_element_located(RegisterLocators.Remote_Component))

        # получаем доступ к теневому участку DOM и создаем объект с формой регистрации
        shadow_root = shadow_host.shadow_root
        self.shadow_root = shadow_root

        # создаем нужные элементы страницы
        self.title_form = shadow_root.find_element(*RegisterLocators.Title_Form)
        self.name_input = shadow_root.find_element(*RegisterLocators.Name_Input)
        self.mail_input = shadow_root.find_element(*RegisterLocators.Mail_Input)
        self.pass_input = shadow_root.find_element(*RegisterLocators.Pass_Input)
        self.pass_viewing = shadow_root.find_element(*RegisterLocators.Pass_Viewing)
        self.referral_input = shadow_root.find_element(*RegisterLocators.Referral_Input)
        self.checkbox_agreement = shadow_root.find_element(*RegisterLocators.Checkbox_Agreement)
        self.submit_btn = shadow_root.find_element(*RegisterLocators.Submit_Btn)
        self.captcha = driver.find_element(*RegisterLocators.Captcha)

    # получаем элементы страницы, откравающиеся в процессе работы
    def name_error(self):
        return self.shadow_root.find_element(*RegisterLocators.Error_Name_Input)

    def mail_error(self):
        return self.shadow_root.find_element(*RegisterLocators.Error_Mail_Input)

    def pass_error(self):
        return self.shadow_root.find_element(*RegisterLocators.Error_Pass_Input)

    def referral_error(self):
        return self.shadow_root.find_element(*RegisterLocators.Error_Referral_Input)

    #  очистка поля ввода
    def field_clear(self, elem, len_text):
        for i in range(len_text):
            elem.send_keys(Keys.BACKSPACE)

    # заполнение полей и чекбокса формы
    def filling_out_form(self, data):
        name, mail, password, code, check = data
        if name:
            self.name_input.send_keys(name)
        if mail:
            self.mail_input.send_keys(mail)
        if password:
            self.pass_input.send_keys(password)
        if code:
            self.referral_input.send_keys(code)
        # выбор включения или нет чекбокса формы
        if check and self.checkbox_agreement.get_attribute('aria-checked') == 'false':
            self.checkbox_agreement.click()
        else:
            if self.checkbox_agreement.get_attribute('aria-checked') == 'true':
                self.checkbox_agreement.click()

    # очистка полей и чекбокса формы
    def clear_form(self, data):
        name, mail, password, code, check = data
        if name:
            self.field_clear(self.name_input, len(name))
        if mail:
            self.field_clear(self.mail_input, len(mail))
        if password:
            self.field_clear(self.pass_input, len(password))
        if code:
            self.field_clear(self.referral_input, len(code))
        if self.checkbox_agreement.get_attribute('aria-checked') == 'true':
            self.checkbox_agreement.click()
