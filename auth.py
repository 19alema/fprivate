from flask import render_template,Blueprint,request,jsonify,abort,redirect,url_for,flash
from flask_login import logout_user,login_required,login_user
from werkzeug.security import generate_password_hash,check_password_hash
from models import Users
auth = Blueprint('auth', __name__)


# A register user can log in to access account

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password =request.form.get("password")
        # pwd = check_password_hash(password)
        user = Users.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            return redirect(url_for("auth.login"))
        else:
            login_user(user)
        return redirect(url_for('main.index'))

# Register a new user
@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    else: 
    #    Collecting User data from the signup form
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        try:
            if password ==confirm_password:
                flash('Account created at Success')
                pwd = generate_password_hash(password, 'sha256')
                new_user=Users(username=username, password=pwd)
                new_user.insert()
            if password != confirm_password:
                flash("Non Matching Password")
        except Exception as e:
            flash("Error has Occured")
        return redirect(url_for('auth.login'))
# logout authenticated user
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
    