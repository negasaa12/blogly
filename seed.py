from models import User, db, Post, Tag, PostTag
from app import app


db.drop_all()
db.create_all()


"""USERS IN DATA BASE"""
Damon = User(first_name= 'Damon', last_name='Salvatore', image_url = 'https://tv-fanatic-res.cloudinary.com/iu/s--i1jwm5Lt--/t_xlarge_p/cs_srgb,f_auto,fl_strip_profile.lossy,q_auto:420/v1522946316/ian-somerhalder-attends-elle-event.jpg')


derek = User(first_name='Derek', last_name='Sheppard', image_url='https://hips.hearstapps.com/digitalspyuk.cdnds.net/14/20/ustv-greys-anatomy-patrick-dempsey.jpg?crop=1.00xw:0.334xh;0,0.0983xh&resize=1200:*')


ben = User(first_name='Ben', last_name='Bagel', image_url='https://olympics.nbcsports.com/wp-content/uploads/sites/10/2013/02/uspw_6375366-e1361893354120.jpg')


diana = User(first_name='Diana', last_name='Smith', image_url='https://i.pinimg.com/564x/71/48/68/714868c20c9b397d00710a74e39d6aa7.jpg')



nicki = User(first_name='Nicki', last_name='Minaj', image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRowXzoZikAsl5urLd8Fuh1jqBd7xvhDw5e0g&usqp=CAU')


peter = User(first_name='Nicki', last_name='Minaj', image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScXxu3S5MvB7sRmKqb9kz2Swog54Le3sDEuA&usqp=CAU')


"""POSTS OF USERS"""

p1 = Post(title='The Lock Woods', content='Anyone knows where the Lockwoods are?', user_id= 1)
p2 = Post(title='Divorce', content='My wife just cheated on me with my best friend. Any tips of Divorce Lawyers', user_id= 2)
p3 = Post(title='Is Mayo an instrument?', content='I was wondering just because I heard it is somewhere.', user_id= 3)
p4 = Post(title='Best Wine Ever', content='The best place to have wine is always in this little cafe Downtown!', user_id= 4)
p5 = Post(title='Get A Grip', content='My little brother is always so gloomy?', user_id= 1)



"""TAGS"""
tag1 = Tag(name='Fun')
tag2 = Tag(name = 'Other')
tag3 = Tag(name ='Scary')

post_tag1 = PostTag(post_id=3, tag_id=1)
post_tag2 = PostTag(post_id=1, tag_id=3)
post_tag3 = PostTag(post_id=3, tag_id=2)
post_tag4 = PostTag(post_id=4, tag_id=2)
post_tag5= PostTag(post_id=5, tag_id=1)

"""users commit"""
db.session.add(Damon)
db.session.add(derek)
db.session.add(ben)
db.session.commit()
db.session.add(diana)
db.session.add(peter)

"""post commit"""
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)



"""tag commit"""
db.session.add(tag1)
db.session.add(tag2)
db.session.add(tag3)
db.session.commit()



"""post_tag commit"""
db.session.add(post_tag1)
db.session.add(post_tag2)
db.session.add(post_tag3)
db.session.add(post_tag4)
db.session.add(post_tag5)

db.session.commit()

# add users
