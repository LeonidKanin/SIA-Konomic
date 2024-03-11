# pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_registration_page.py
# pytest -v --driver Firefox --driver-path geckodriver.exe tests/test_registration_page.py

import time

from selenium.common import NoSuchElementException
from pages.registration_form import RegistrationForm
from prepare.for_registration_form import *


def test_name_input_negative(driver):
    # открытие страницы с формой Регистрация в браузере
    page = RegistrationForm(driver)

    # проверка доступности формы регистрации
    assert page.title_form.text == 'Регистрация'

    # параметризация поля ввода имени
    for name in NameInputTesting.negative_name:
        page.name_input.send_keys(name)
        # клик вне поля ввода для формирования сообщения об ошибке
        page.title_form.click()
        error_name = page.name_error().text

        # проверка наличия и текста сообщения об ошибке
        assert error_name == 'Поле не заполнено' or \
               'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',\
               f'Отсутствует или неверное сообщение об ошибке: "{error_name}", при вводе: "{name}".'

        # очистка поля ввода
        page.field_clear(page.name_input, len(name))


def test_mail_input_negative(driver):
    # открытие страницы с формой Регистрация в браузере
    page = RegistrationForm(driver)

    # проверка доступности формы регистрации
    assert page.title_form.text == 'Регистрация'

    # параметризация поля ввода адреса электронной почты
    for mail in MailInputTesting.negative_mail:
        page.mail_input.send_keys(mail)
        # клик вне поля ввода для формирования сообщения об ошибке
        page.title_form.click()
        error_mail = page.mail_error().text

        # проверка наличия и текста сообщения об ошибке
        assert error_mail == 'Поле не заполнено' or 'Формат e-mail: somebody@somewhere.ru', \
            f'Отсутствует или неверное сообщение об ошибке: "{error_mail}", при вводе: "{mail}".'

        # очистка поля ввода
        page.field_clear(page.mail_input, len(mail))


def test_pass_input_negative(driver):
    # открытие страницы с формой Регистрация в браузере
    page = RegistrationForm(driver)

    # проверка доступности формы регистрации
    assert page.title_form.text == 'Регистрация'

    # включение видимости пароля в поле ввода (необязательный код)
    page.pass_viewing.click()

    # параметризация поля ввода пароля
    for password in PasswordInputTesting.negative_pass:
        page.pass_input.send_keys(password)
        # клик вне поля ввода для формирования сообщения об ошибке
        page.title_form.click()

        # При пропуске программой некорректного пароля, элемент сообщения об ошибке не появится в DOM
        try:
            error_pass = page.pass_error().text
        except NoSuchElementException:
            raise AssertionError(f'Отсутствует сообщение об ошибке, при вводе: "{password}".')

        # Проверка текстов сообщений об ошибке
        # Сложная конструкция из-за того, что в сообщениях 1 и 2 много общих слов
        # При использовании: assert 'текст 1' or 'текст 2' можно пропустить отсутствие общих слов или ошибки в них
        try:
            assert error_pass == 'Пароль должен содержать минимум 8 символов'
        except AssertionError:
            try:
                assert error_pass == 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры'
            except AssertionError:
                try:
                    assert error_pass == 'Поле не заполнено'
                except AssertionError:
                    raise AssertionError(f'Неверное сообщение об ошибке: "{error_pass}", при вводе: "{password}".')

        # очистка поля ввода
        page.field_clear(page.pass_input, len(password))


def test_referral_input_negative(driver):
    # открытие страницы с формой Регистрация в браузере
    page = RegistrationForm(driver)

    # проверка доступности формы регистрации
    assert page.title_form.text == 'Регистрация'

    # параметризация поля ввода реферального кода
    for referral in ReferralInputTesting.negative_code:
        page.referral_input.send_keys(referral)
        error_referral = page.referral_error().text

        # проверка наличия и текста сообщения об ошибке
        assert error_referral == 'Неверный формат ссылки', \
            f'Отсутствует или неверное сообщение об ошибке: "{error_referral}", при вводе: "{referral}".'

        # очистка поля ввода
        page.field_clear(page.referral_input, len(referral))


def test_scripts_in_form_negative(driver):
    # открытие страницы с формой Регистрация в браузере
    page = RegistrationForm(driver)

    # проверка доступности формы регистрации
    assert page.title_form.text == 'Регистрация'

    # параметризация заполнения полей ввода формы
    for data_form in ScriptsInFormTesting.data_negative:
        # заполнение полей формы набором данных
        page.filling_out_form(data_form)

        # не доступна кнопка Далее при некорректном реферальном коде
        if 'disabled' in page.get_attributes(page.submit_btn):
            # очистка полей формы
            page.clear_form(data_form)
            # переход к началу цикла с новыми данными
            continue

        page.submit_btn.click()
        # задержка выполнения для возможного появления капчи (на слабом оборудовании возможно понадобится удлинить)
        time.sleep(1)

        # проверка, что при некорректном заполнении формы, не происходит перехода к капче
        assert 'visibility: hidden' in page.get_attributes(page.captcha)['style'],\
            f'Непредвиденное прохождение формы, при некорректном вводе: name="{data_form[0]}"; mail="{data_form[1]}";' \
            f' password="{data_form[2]}"; referral code="{data_form[3]}".'

        # очистка полей формы
        page.clear_form(data_form)
