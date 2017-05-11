from ext import db
from LightBlog.model import Category
class CategoryService(object):
    """description of class"""
    def __init__(self):
        pass

    def AddCategory(self,category):
        db.session.add(category)
        db.session.commit()
        return




