from LightBlog.ext import db
from LightBlog.model.Category import Category

class CategoryService(object):
    
    def __init__(self):
        self.Session=db.session

    def AddCategory(self,category):
        self.Session.add(category)
        self.Session.commit()
        return None

    def GetCategory(self,id):
        category=self.Session.query(Category).get(id)
        return category

    def RemoveCategory(self,id):
        self.Session.query(Category).filter(Category.Id==id).delete(synchronize_session=False)
        self.Session.commit()
        return None
    
    def ListCategories(self,start,stop):
        categories=self.Session.query(Category).order_by(Category.Id).slice(start,stop)
        return categories

    def UpdateCategory(self,category):
        self.Session.merge(category)
        self.Session.commit()
        return None

    def ModifyCategory(self,id,**changes):
        self.Session.query(Category).filter(Category.Id==id).update(changes,synchronize_session=False)
        self.Session.commit()
        return None
    
    def GetCategoriesNumber(self):
        number=self.Session.query(Category).count()
        return number

    def Execute(self,sql):
        results=self.Session.execute(sql).fetchall()
        return results




