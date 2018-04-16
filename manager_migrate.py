from flask import Flask

from flask_script import Manager
from flask.ext.script import Manager
from flask_migrate import MigrateCommand,Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:mysql@127.0.0.1:3306/flask_test'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'qiong'

db = SQLAlchemy(app)

maneger = Manager(app)

Migrate(app,db)