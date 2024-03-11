# Данные для негативного тестирования полей ввода подготовлены с использоанием следующих техник тест-дизайна:
# - разделение на классы эквивалентности;
# - анализ граничных значений.

class NameInputTesting:
    # Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы
    negative_name = ['', '        ', 'A' 'Jerry', 'Ann#$%123', 'A14jYuZsGlJjYxOYdPTJebhuJgGgWuaYd', 'ВаняТаня123',
                     'JonВаня123', '123456', 'a1234567890123456789012345678901', '1JerrySmith',
                     '<script>alert("Field input vulnerable!")</script>'
                     ]


class MailInputTesting:
    # Формат e-mail: somebody@somewhere.ru
    negative_mail = ['', 'test@test.com', 'test@test.org', 'test1@test2@test.ru', 'test@testru', 'test@тест.ru',
                     '@test.ru', 'test@.ru', '.test@test.ru', 'test@test.ru.', 'test!@test&.ru',
                     '< script > alert("Field_input_vulnerable!") < / script >'
                     ]


class PasswordInputTesting:
    # Пароль должен содержать от 8 до 64 символов английского языка, включая заглавные буквы и цифры
    negative_pass = ['', '        ', 'Jerry12', 'jerry123456', 'JERRYSMITH', '1234567890',
                     'ASDDfdgfhdfghn14ПРОВsGlJjYxOYdPTJebhuJgGgWuaYBpUbxEtxKEhGtXiuBkyC',
                     '< script > alert("Field_input_vulnerable!") < / script >'
                     ]


class ReferralInputTesting:
    # Реферальный код должен содержать от 4 до 8 символов
    negative_code = ['1', '123', '123456789', 'F', 'qwe', 'qwertyuio',
                     '< script > alert("Field_input_vulnerable!") < / script >'
                     ]


class ScriptsInFormTesting:
    data_negative = [('', 'test@test.ru', 'ABCDqwer123', '', 'true'), ('Jonjonjon', '', 'ABCDqwer123', '', 'true'),
                     ('Jonjonjon', 'test@test.ru', '', '', True),
                     ('ВаняТаня', 'test@test.ru', 'ABCDqwer123', '12345', True),
                     ('Jonjonjon', 'tt@tt.', 'ABCqwe12', '12345', True),
                     ('Jonjonjon', 'test@test.ru', 'qwery123', '12345', True),
                     ('Jonjonjon', 'tt@tt.ru', 'ABCqwe12', '12', True),
                     ('Jonjonjon', 'test@test.ru', 'ABCDqwer123', '12345', False)
                     ]
