from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memo.db'
db = SQLAlchemy(app)


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text())
    content = db.Column(db.Text())


@app.route('/')
def list_reviews():
    message = "mylog"

    reviews = Review.query.all()
    return render_template('list.html', message = message, reviews = reviews)


@app.route('/show/<int:id>')
def show_review(id):

    review = Review.query.get(id)

    return render_template('show.html', review = review)


@app.route('/new')
def new_review():

    return render_template('new.html')


@app.route('/create', methods=['post'])
def create_review():

    new_review = Review()
    new_review.title = request.form['title']
    new_review.content = request.form['content']
    db.session.add(new_review)
    db.session.commit()

    review = Review.query.get(new_review.id)

    return render_template('show.html', review = review)


@app.route('/destroy/<int:id>')
def destroy_review(id):
    message = "mylog"

    destroy_review = Review.query.get(id)
    db.session.delete(destroy_review)
    db.session.commit()

    reviews = Review.query.all()

    return render_template('list.html', message = message, reviews = reviews)


@app.route('/edit/<int:id>')
def edit_review(id):

    review = Review.query.get(id)

    return render_template('edit.html', review = review)


@app.route('/update/<int:id>', methods=['post'])
def update_review(id):

    update_review = Review.query.get(id)
    update_review.title = request.form['title']
    update_review.content = request.form['content']
    db.session.commit()

    review = Review.query.get(id)

    return render_template('show.html', review = review)
