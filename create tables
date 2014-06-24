//creating tables in pgadmim using python file
//commands to be executed
//compile your python file
//go to python cosole and type this...

>>from filename import *
>>db.create_all()

//python code
from flask import Flask, jsonify ,flash 
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import deferred
from sqlalchemy.ext.hybrid import hybrid_property, Comparator
from sqlalchemy import func
import psycopg2


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:balaji@localhost:5432/tnt'
db = SQLAlchemy(app)
app.secret_key="appsecret"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    parent=db.Column(db.String(30))
    school=db.Column(db.String(30))
    std=db.Column(db.String(10))
    dob=db.Column(db.String(11))
    email=db.Column(db.String(50))
    mobile=db.Column(db.String(10))
    username=db.Column(db.String(20))
    password_hashed = deferred(db.Column(db.String(250)))
    reg_id=db.Column(db.String(15),unique=True)    

    @hybrid_property
    def password(self):
        """Relying upon database-side crypt() only, so in-Python usage
        is notimplemented.

        """
        raise NotImplementedError(
                "Comparison only supported via the database")

    class CryptComparator(Comparator):
        """A Comparator which provides an __eq__() method that will run
        crypt() against both sides of the expression, to provide the 
        test password/salt pair.

        """
        def __init__(self, password_hashed):
            self.password_hashed = password_hashed

        def __eq__(self, other):
            return self.password_hashed == \
                    func.crypt(other, self.password_hashed)

    @password.comparator
    def password(cls):
        """Provide a Comparator object which calls crypt in the
        appropriate fashion.

        """
        return User.CryptComparator(cls.password_hashed)

    @password.setter
    def password(self, value):
        """assign the value of 'password', 
        using a UOW-evaluated SQL function.

        See http://www.sqlalchemy.org/docs/orm/session.html#embedding-sql-insert-update-expressions-into-a-flush
        for a description of SQL expression assignment.

        """
        self.password_hashed = func.crypt(value, func.gen_salt('bf'))

class prepost(db.Model):
    reg_id=db.Column(db.String(15),unique=True) 
    name=db.Column(db.String(30))
    pre_test=db.Column(db.Float)
    post_test=db.Column(db.Float)
    total=db.Column(db.Float)
    comments=db.Column(db.String(150))
    id = db.Column(db.Integer, primary_key=True)
    

