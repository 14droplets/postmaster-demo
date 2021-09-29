import flask

from postmaker.webapp.blueprints.posts import posts_blueprint
from postmaker.webapp.database import db


def create_app(config: dict) -> flask.Flask:
    """ Создание объекта приложения со всеми финтифлюшуками """

    app = flask.Flask("postmaker.webapp")
    # Говорим приложению где искать наши шаблоны
    app.template_folder = "templates"
    # Где искать всякие картинкосы
    app.static_folder = "static"

    # Некожно попишем в лог о том как мы запускаемся
    app.logger.info("Использую БД по пути '%s'", config.get("SQLALCHEMY_DATABASE_URI", None))

    # Проставляем конфиг приложения
    app.config.update(config)

    # Регистрируем плагины
    db.init_app(app)

    # Регистрируем наши модули
    app.register_blueprint(posts_blueprint)

    return app
