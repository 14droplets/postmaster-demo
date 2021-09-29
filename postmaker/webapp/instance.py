from logging import getLogger
from logging.config import dictConfig as logging_dict_config

from postmaker.common.config import load_config
from postmaker.webapp.app_factory import create_app

_log = getLogger(__name__)

# грузим конфиг
config = load_config()

# Настроим логи, чтобы видеть не только WARNING и ERROR сообщения
logging_dict_config(config["LOG_CONFIG"])

# Создаем объект приложения
app = create_app(config)


