from LightBlog.ext import db

class User(db.Model):
    __tablename__='User'
    Id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(255))
    Password=db.Column(db.String(255))


