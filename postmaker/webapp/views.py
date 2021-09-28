from flask import Blueprint
from flask import render_template, redirect, url_for
from flask import current_app

from postmaker.webapp.forms import PostForm

main_blueprint = Blueprint("main", "/")


@main_blueprint.route("/")
def index():
    return render_template("base.html")


@main_blueprint.route("/posts", methods=["GET", "POST"])
def posts():
    form = PostForm()
    if form.validate_on_submit():
        current_app.logger.info("Получил форму!")
        redirect(url_for("main.posts"))

    return render_template("posts.html", new_post_form=form)
