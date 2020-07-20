from flask import url_for, flash, redirect, render_template

from app import app, db
from app.models import Message
from app.forms import MessageFrom


@app.route('/', methods=['GET', 'POST'])
def index():
    # 加载所有数据
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = MessageFrom()
    if form.validate_on_submit():
        name = form.name.data
        body = form.name.data
        message = Message(name=name, body=body)
        db.session.add(message)  # 添加记录到数据库会话
        db.session.commit()  # 提交会话
        flash('你的留言已经发送成功！')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
