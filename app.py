


from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
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

    
    
    return render_template('create.html')


@app.route('/users/new', methods=["POST"])
def created_user():

    """create user"""

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
   
    return render_template('details.html', users=users)