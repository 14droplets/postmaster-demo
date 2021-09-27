import yaml


def load_config(cfg_path) -> dict:
    """ Загрузка конфига приложения"""

    # Открываем файл как поток и парсим его как ямль
    with open(cfg_path, mode="r") as stream:
        cfg = yaml.load(stream, Loader=yaml.FullLoader)

    return cfg
