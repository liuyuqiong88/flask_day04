# coding:utf-8

from flask import Flask, request, render_template, url_for, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField
from flask_migrate import MigrateCommand,Migrate
from flask_script import Manager

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:mysql@127.0.0.1:3306/flask_test'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'qiong'

db = SQLAlchemy(app)

manager = Manager(app)

Migrate(app,db)

manager.add_command(db,MigrateCommand)



class Author(db.Model):
    """模型类"""

    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), unique=True)

    au_book = db.relationship("Book", backref='author')

    def __str__(self):
        return "<Author: %s%s>" % (self.id, self.name)


class Book(db.Model):

    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(99), unique=True)

    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))

    def __str__(self):
        return "<Books: %s%s>" % (self.id, self.name)


class AppenForm(FlaskForm):

    author_info = StringField(u"作者: ", validators=[DataRequired()])
    book_info = StringField(u"书名: ", validators=[DataRequired()])
    submit = SubmitField(u"添加")


@app.route('/', methods=["POST", "GET"])
def index():

    book_form = AppenForm()
    if request.method == "POST":
        author = request.form.get('author_info')
        book = request.form.get('book_info')

        author_db = Author.query.filter(Author.name==author).first()

        if author_db:
            book_db = Book.query.filter(Book.author_id==author_db.id,Book.name==book).first()
            if book_db:
                flash(u"书名已存在")
            else:
                new_book = Book(name=book,author_id=author_db.id)

                try:
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print e
                    db.session.rollback()
                    flash(u"添加作者书名失败")
        else:

            new_author = Author(name = author)
            new_book = Book(name = book)
            new_book.author = new_author

            try:

                db.session.add(new_book)
                db.session.commit()
            except Exception as e:
                print e
                db.session.rollback()
                flash(u"添加书名作者失败")


    authors = Author.query.all()


    return render_template('books.html',form = book_form,authors = authors)

@app.route('/delbook/<book_id>',methods=["POST","GET"])
def delbook(book_id):

    book = Book.query.get(book_id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e :
            print e
            db.session.rollback()
            flash(u"删除书本错误")

    else:
        flash(u"书本不存在")

    return redirect(url_for('index'))

@app.route('/delauthor/<author_id>',methods=["POST","GET"])
def delauthor(author_id):

    author = Author.query.get(author_id)

    if author:
        books = author.au_book
        try:
            for book in books:
                db.session.delete(book)
            db.session.delete(author)
            db.session.commit()
        except Exception as e :
            print e
            db.session.rollback()
            flash(u"删除书本错误")

    else:
        flash(u"书本不存在")

    return redirect(url_for('index'))

if __name__ == '__main__':



    app.run(debug=True)
    # manager.run()