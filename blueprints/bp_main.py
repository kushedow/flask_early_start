from create_app import app
from flask import Blueprint

# cоздаем блупринт

blueprint_main = Blueprint("blueprint_main", __name__)

# Мы можем обращатьс к приложения напрямую
# При этом мы получаем ссылку на первоначальный app
# Который был создан в create_app

info = app.config.get("INFO")

# Дальше мы используем созданные при импорте блупринта объекты
# Будь это сервисы, дао или строки.

@blueprint_main.route("/")
def index_page():
    return info

