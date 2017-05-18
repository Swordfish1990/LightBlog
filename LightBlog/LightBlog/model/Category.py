from LightBlog.ext import db

class Category(db.Model):
    __tablename__='Category'
    Id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(20))


