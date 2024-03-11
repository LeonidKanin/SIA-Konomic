Тестовое задание.

Тестовый стенд:  https://exchange.konomik.com/

Область тестирования: форма Регистрация. 

Код написан на Python в PyCharm, с использованием фреймворков Pytest и Selenium.

Проводится негативное тестирование всех полей ввода области тестирования, как постоянных, так и открывающихся по ходу тестирования (сообщения об ошибках). Дополнительно, тестируются негативные сценарии заполнения формы.

Тесты написаны с использованием техники серого ящика, подразумевающей частичное знание внутреннего устройства объекта (HTML-код).

Параметризация тестов осуществляется с помощью циклов, для сокращения времени прохождения тестов. Использование @pytest.mark.parametrize приводит к большим потерям времени из-за постоянного открытия браузера.

Наборы предварительно подготовленных данных для параметризации тестов созданы с использованием таких техник тест-дизайна, как разбиение на классы эквивалентности и граничные значения.

Код подразумевает запуск тестов в различных браузерах, поддерживаемых Selenium. Для примера, используются Chrome и Firefox.

Структура проекта:

в директории pages находится объект области тестирования в виде класса с формой Регистрация, наследующий от базового класса страницы BasePage, а так же локаторы всех элементов;
в директории prepare находятся предварительно подготовленные данные;
в директории tests находятся тесты;
в корне проекта: chromedriver.exe (Chrome 122), geckodriver.exe (Firefox 123) и requirement.txt.

Команды для запуска в виде комментариев, в начале тестового файла.
