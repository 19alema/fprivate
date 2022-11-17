from flask import Blueprint, render_template,request, url_for, redirect,jsonify
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy
from models import Users, Messages

# from models import db, Task, Users

main = Blueprint('main', __name__)

@main.route("/")
# @login_required
def index():
    messages = Messages.query.all()
    messages_data =[]
    for msg in messages:
        author =Users.query.filter(Users.id ==msg.user).one_or_none();
        messages_data.append({
            'title':msg.message_title,
            'text':msg.message_body,
            'author':author.username,
            'id':msg.id
        })
    
    return render_template('base.html', data=messages_data)


@main.route('/message', methods=['GET','POST'])
def profile():
    if request.method=='GET':
        return render_template("create_message.html")
    else:
        title = request.form.get('title')
        message = request.form.get('message')
        title = request.form.get('title')
        user_id = current_user.id
        new_message = Messages(message_title=title,message_body=message,user=user_id)
        new_message.insert()
        return redirect(url_for("main.index"))

        # 
@main.route("/messages/<int:id>", methods=['DELETE', 'GET'])
def delete_msg(id):
    delete_message = Messages.query.filter(Messages.id ==int(id)).one_or_none();
    if delete_message.user == current_user.id:
        delete_message.delete()
    return redirect('/')
