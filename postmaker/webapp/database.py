from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy
from postmaker.common.database import Base

db = FlaskSQLAlchemy(model_class=Base)

