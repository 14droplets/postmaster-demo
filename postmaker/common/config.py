import yaml
import os


def load_config(cfg_path=None) -> dict:
    """ Загрузка конфига приложения"""

    # Если путь до конфига не задан явно, используем переменную окружения
    if not cfg_path:
        cfg_path = os.environ["POSTMASTER_CONFIG"]

    # Открываем файл как поток и парсим его как ямль
    with open(cfg_path, mode="r") as stream:
        cfg = yaml.load(stream, Loader=yaml.FullLoader)

    return cfg
