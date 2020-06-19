# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class TableForm(FlaskForm):
    name = StringField(u'垃圾的名字', validators=[DataRequired(), Length(1, 10)])
    submit = SubmitField(u'查询')
