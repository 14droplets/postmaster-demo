import logging
from logging.config import dictConfig as logging_dict_config
import argparse

from sqlalchemy import create_engine

from postmaker.common.config import load_config
from postmaker.common.database import Base


_log = logging.getLogger(__name__)


def init_database(config):
    """ Инициализация базы данных """

    # Пользователь хочет создать таблицы в БД, окей, это мы можем
    # Напишем в лог о том, где будем создавать эту БД
    db_uri = config["SQLALCHEMY_DATABASE_URI"]
    _log.debug("Создаю базу данных по пути '%s'", db_uri)

    # Создаем объекты для работы с БД
    engine = create_engine(db_uri)

    # Создаем все таблицы
    Base.metadata.create_all(bind=engine)
    _log.info("Готово!")


def admin_main(argv):
    """ Функция - точка входа для админских команд """

    parser = argparse.ArgumentParser("Админские команды для postmaker-a", add_help=True)
    # Регистрируем аргумент - путь до конфиг файла
    parser.add_argument(
        "--config",
        metavar="путь до конфига", dest="config", nargs="?", type=str
    )

    # Регистриуем команды
    subparsers = parser.add_subparsers(dest="command_name", help="команда")
    subparsers.add_parser("init-db", help="инициализация БД")

    # разбираем аргументы
    args = parser.parse_args(argv)
    config_path = args.config
    command_name = args.command_name

    # Грузим конфиг
    config = load_config(config_path)

    # Опять настраиваем лог
    logging_dict_config(config["LOG_CONFIG"])

    _log.debug("Загружен конфиг из '%s'" % config_path)

    if command_name == "init-db":
        _log.info("Оператор хочет создать БД")
        init_database(config)

