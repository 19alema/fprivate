from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
database_name = "private"
database_path = "postgresql://postgres:root@{}/{}".format('localhost:5432', database_name)


def setup_db(app):
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# uSERS
class Users(db.Model, UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(1000), nullable=False,unique=True)
    password=db.Column(db.String(5000), nullable=False)

    messages =db.relationship('Messages',lazy=True, backref='users')
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# USERS MESSAGES 
class Messages(db.Model):
    __tablename__='messages'
    id =db.Column(db.Integer,primary_key=True)
    message_title=db.Column(db.String(500))
    message_body =db.Column(db.String(1000))
    # date = db.Column(db.String())

    # The below column indaicates the author of that message
    user=db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return f"id: {self.id}"

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


