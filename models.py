
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

def connect_db(app):
    db.app= app
    db.init_app(app)




class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(100),
                           nullable=False,
                           unique=True)
   
    last_name = db.Column(db.String(100),
                          nullable=True,
                          unique=False)
    
    image_url = db.Column(db.String)

    posts = db.relationship('Post', backref='user')

    def __repr__(self):
        return f"<User {self.id}, {self.first_name}, {self.last_name}>"
    






class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    title = db.Column(db.String(80),
                      nullable=False,
                      unique=False)
    
    content = db.Column(db.String(1000),
                        nullable=False,
                        unique=False)
    
    created_at = db.Column(db.DateTime,
                            nullable=False,
                            default=datetime.utcnow())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Post {self.id}, {self.title}, {self.content}>"






class Tag(db.Model):
    """Tag that can be added to posts."""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship(
        'Post',
        secondary="posts_tags",
        # cascade="all,delete",
        backref="tags",
    )

    
class PostTag(db.Model):
    """Tag on a post."""

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
