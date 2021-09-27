from logging.config import dictConfig as logging_dict_config

from postmaker.common.config import load_config
from postmaker.webapp import app_factory


# грузим конфиг
config_path = "postmaker_config.yaml"
config = load_config(config_path)

# Настроим логи, чтобы видеть не только WARNING и ERROR сообщения
logging_dict_config(config["LOG_CONFIG"])

# Создаем объект приложения
app = app_factory(config)

# Напишем в лог откуда мы взяли конфиг
# Возпольуемся логгером приложения
app.logger.info("Я взял конфиг из '%s", config_path)

