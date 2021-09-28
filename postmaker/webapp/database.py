from flask import Flask
from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy

from postmaker.common.database import Base

db = FlaskSQLAlchemy(metadata=Base.metadata)


def init_webapp_database(app: Flask):
    db.init_app(app)
