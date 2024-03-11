class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нужные объект веб-драйвера, адрес страницы и время ожидания элементов

    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    # получение всех атрибутов элемента
    def get_attributes(self, element) -> dict:
        return self.driver.execute_script(
            """
            let attr = arguments[0].attributes;
            let items = {}; 
            for (let i = 0; i < attr.length; i++) {
                items[attr[i].name] = attr[i].value;
            }
            return items;
            """,
            element
        )
