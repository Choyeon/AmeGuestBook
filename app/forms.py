from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class FlaskFromCN(FlaskForm):
    class Meta:
        locales = ['zh']


class MessageFrom(FlaskFromCN):
    name = StringField('昵称', validators=[DataRequired(), Length(0, 20)])
    body = TextAreaField('留言', validators=[DataRequired(), Length(0, 255)])
    submit = SubmitField('发送')
