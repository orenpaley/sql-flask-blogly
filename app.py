"""Blogly application."""

from models import db, connect_db, User
from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "jjF73!rtc"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_users():
  users = User.query.order_by(User.last_name).all()

  return render_template('users.html', users = users)

@app.route('/users')
def user_hub():
  users = User.query.all()

  return render_template('list.html', users = users)

@app.route('/add_user')
def get_add_user():
  users = User.query.all()
  return render_template('add_user.html', users=users)

@app.route('/add_user', methods=['POST'])
def post_add_user():
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  image_url = request.form['image_url']
  user = User(first_name=first_name, last_name=last_name, image_url=image_url)
  
  db.session.add(user)
  db.session.commit()

  return redirect('/users')

@app.route('/<id>', methods=['GET', 'POST'])
def get_info_user(id):
  user = User.query.get(id)

  return render_template('user.html', user=user)

@app.route('/<id>/edit')
def get_edit_form(id):
  user = User.query.get(id)
  return render_template('edit_user.html',user=user)

@app.route('/<id>/edit/update', methods=['POST'])
def edit_user(id):
  user = User.query.get(id)
  first_name = request.form['first_name']
  last_name = request.form['last_name']
  image_url =request.form['image_url']

  if (first_name) :
    user.first_name = first_name
  if (last_name) :
    user.last_name = last_name
  if (image_url) :
    user.image_url = image_url

  db.session.add(user)
  db.session.commit()

  return redirect(f'/{user.id}')

@app.route('/<id>/edit/delete', methods=['GET','POST'])
def delete_user(id):
  User.query.filter(User.id == id).delete()
  db.session.commit()

  return redirect('/users')

