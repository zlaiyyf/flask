#-*- encoding: utf-8 -*_

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import TableForm
from pa import spider
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


class Config():
    SECRET_KEY = 'My Secret Key'

    @staticmethod
    def init_app(app):
        pass


bootstrap = Bootstrap()

app = Flask(__name__)
app.config.from_object(Config)
Config.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TableForm()
    if form.validate_on_submit():
        return render_template('index.html', form=form,result=spider(form.name.data))
    return render_template('index.html', form=form,result="请输入要查询的物品")


if __name__ == '__main__':
    bootstrap.init_app(app)
    app.run()
