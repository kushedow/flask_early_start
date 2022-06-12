# В этом файле демонстрируется создание фикстуры
# При этом используется перенастройка приложения
# Подмена файла настроек позволяет юзать тестовые настройки

import pytest

# Обрати внимание на эту функцию
from run_app import get_app


class TestApp:

    @pytest.fixture
    def app_instance(self):
        # Вызываем функцию пересодания приложения
        instance = get_app(config_path="config/config_test.py")
        return instance

    def test_one(self, app_instance):
        assert app_instance.config.get("MODE") == "Режим тестирования работает"

    def test_two(self, app_instance):

        def read_data(path):
            with open(path) as file:
                return file.read().strip()

        path = app_instance.config.get("DATA_SOURCE")

        assert read_data(path) == "Данные для тестов"
