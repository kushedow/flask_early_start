# Запустите этот файл, чтобы стартовать приложение

from create_app import app
from blueprints.bp_main import blueprint_main

# Этот код выполняется однократно
app.register_blueprint(blueprint_main)

# Этот код выполняется столько раз, сколько нам нужно приложение
def get_app(config_path="config/config_prod.py"):
    """
    Возвращает приложение с настройками и блупринтами.
    Использует уже созданное в create_app приложение.
    Чтобы разрешить
    """

    app.config.from_pyfile(config_path)
    return app


if __name__ == '__main__':
    app = get_app()
    app.run()
