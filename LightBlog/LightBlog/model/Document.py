from LightBlog.ext import db

class Document(db.Model):
    __tablename__='Document'
    Id=db.Column(db.Integer,primary_key=True)
    Title=db.Column(db.String(255))
    Content=db.Column(db.Text)
    CategoryId=db.Column(db.Integer)
    Cover=db.Column(db.String(255))
    Abstract=db.Column(db.String(255))
    CreateTime=db.Column(db.DateTime)
    UpdateTime=db.Column(db.DateTime)
    UserId=db.Column(db.Integer)
    Partition=db.Column(db.String(255))
    


