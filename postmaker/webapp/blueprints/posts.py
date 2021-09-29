from flask import Blueprint
from flask import render_template, redirect, url_for
from flask import current_app

from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

from postmaker.common.database import Post as PostModel
from postmaker.webapp.database import db


posts_blueprint = Blueprint(
    "posts", __name__,
    url_prefix="/posts",
    template_folder="templates"
)


class PostForm(FlaskForm):
    """ Форма для ввода нового поста """

    title = StringField("Заголовок", [DataRequired()])
    tags = StringField("Тэги", [DataRequired()])
    description = TextAreaField("Описание", [DataRequired()])


@posts_blueprint.route("/")
def index():
    return render_template("base.html")


@posts_blueprint.route("/list-posts")
def list_posts():
    return render_template("base.html")


@posts_blueprint.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        current_app.logger.info("Получил форму!")

        post = PostModel(
            title=form.title.data,
            description=form.description.data,
            tags=form.tags.data
        )
        current_app.logger.info("Создал запись БД!")

        db.session.add(post)
        db.session.commit()

        redirect(url_for("posts.list_posts"))

    return render_template("new-post.html", new_post_form=form)
