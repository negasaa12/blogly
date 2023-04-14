
from datetime import datetime
from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
from sqlalchemy import text


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_data_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "HELLO"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.app_context().push()




connect_db(app)
# db.create_all()


@app.route('/', methods=["GET","POST"])
def home():

   
    return redirect('/users')






@app.route('/users')
def list_users():

    """shows list of all users"""
    users = User.query.all()

    
    return render_template('users.html', users=users)





@app.route('/user/new')
def create_user():
    """Create A User Form """
    
    
    return render_template('create.html')


@app.route('/users/new', methods=["POST"])
def created_user():

    """handle user form to create user"""

    first = request.form['fname']
    last = request.form['lname']
    url = request.form['url']
    print(first,last)
   
    new_user = User(first_name=first, last_name=last, image_url=url)
    db.session.add(new_user)
    db.session.commit()

    print(new_user)
        
    return redirect('/')



@app.route('/users/<int:user_id>')
def show_details(user_id):
   
    """show detail about a single user"""


    users = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(user_id=user_id)
   
    return render_template('details.html', users=users,posts=posts)


@app.route('/users/<int:user_id>/edit')
def edit_details(user_id):
    
    """edit user profile"""

    users = User.query.get_or_404(user_id)


    return render_template('edits.html', users=users)




@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_details(user_id):
    
    """update user"""

    first = request.form['first_name']
    last = request.form['last_name']
    url = request.form['image']

    users = User.query.get_or_404(user_id)

    users.first_name = first 
    users.last_name = last
    users.image_url = url
    
  

    
    db.session.commit()

    return redirect("/users")



@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):


   """DELETE USER"""

   users = User.query.get_or_404(user_id)
   db.session.delete(users)
   db.session.commit()
    
   return redirect('/users')



@app.route('/users/<int:user_id>/posts/new')
def post_form(user_id):
    
    """A form for a post """

    users = User.query.get_or_404(user_id)

    return render_template('post_form.html', users=users)




@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def add_post(user_id):
   """Adding users post to their page"""


   title = request.form['title']
   content = request.form['content']

   post = Post(title=title, content=content, user_id=user_id)
   db.session.add(post)
   db.session.commit()


     
   return redirect(f"/users/{user_id}")




@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """SHOWS USERS POSTS"""

    posts = Post.query.get_or_404(post_id)


    return render_template('posts.html', posts=posts)




@app.route('/posts/<int:post_id>/edit')

def edit_post(post_id):
    """FORM TO EDIT POST"""


    post = Post.query.get_or_404(post_id)

    return render_template('edit_post.html', post=post)






@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def handle_post(post_id):

    "EDIT POST AND RETURN TO USER"
    title = request.form['title']
    content = request.form ['content']

    post = Post.query.get_or_404(post_id)
    
    post.title = title
    post.content = content

    db.session.commit()

    return redirect(f"/posts/{post_id}")