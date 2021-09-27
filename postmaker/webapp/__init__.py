import flask

from flask import Flask

from postmaker.webapp.views import main_blueprint
from postmaker.webapp.database import init_webapp_database


def app_factory(config: dict) -> Flask:
    """ Создание объекта приложения со всеми финтифлюшуками """

    app = flask.Flask(__name__)
    # Говорим приложению где искать наши шаблоны
    app.template_folder = "templates"
    # Где искать всякие картинкосы
    app.static_folder = "static"

    # Проставляем конфиг приложения
    app.config.update(config)

    # Регистрируем плагины
    init_webapp_database(app)

    # Регистрируем наши модули
    app.register_blueprint(main_blueprint)

    return app