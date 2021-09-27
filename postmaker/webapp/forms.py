from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    """ Форма для ввода нового поста """

    title = StringField(
        "Заголовок",
        [
            DataRequired(),
        ]
    )

    content = TextAreaField(
        "Контент-с",
        [
            DataRequired()
        ]
    )
