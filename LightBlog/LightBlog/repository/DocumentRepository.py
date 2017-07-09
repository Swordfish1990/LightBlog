from LightBlog.ext import db
from LightBlog.model.User import User
from LightBlog.model.Category import Category
from LightBlog.model.Document import Document

class DocumentRepository(object):
    """description of class"""

    def __init__(self):
        self.Session=db.session

    def AddDocument(self,document):
        self.Session.add(document)
        self.Session.commit()
        return None

    def GetDocument(self,id):
        document=self.Session.query(Document).get(id)
        return document

    def RemoveDocument(self,id):
        self.Session.query(Document).filter(Document.Id==id).delete(synchronize_session=False)
        self.Session.commit()
        return None

    def ListDocumentsInfo(self,start,stop):
        results=self.Session.query(Document.Id,Document.Title,Document.CreateTime,Document.UpdateTime,User.Name,Category.Name).join(User,Document.UserId==User.Id).join(Category,Document.CategoryId==Category.Id).order_by(Document.CreateTime.desc()).slice(start,stop).all()
        return [{'Id':item[0],'Title':item[1],'CreateTime':item[2],'UpdateTime':item[3],'User':item[4],'Category':item[5]} for item in results]

    def ListDocumentsInfoByCategory(self,category_id,start,stop):
        results=self.Session.query(Document.Id,Document.Title,Document.CreateTime,Document.UpdateTime,User.Name,Category.Name).join(User,Document.UserId==User.Id).filter(Document.CategoryId==category_id).join(Category,Document.CategoryId==Category.Id).order_by(Document.CreateTime.desc()).slice(start,stop).all()
        return [{'Id':item[0],'Title':item[1],'CreateTime':item[2],'UpdateTime':item[3],'User':item[4],'Category':item[5]} for item in results]

    def ListDocumentsInfoByPartition(self,partition,start,stop):
        results=self.Session.query(Document.Id,Document.Title,Document.CreateTime,Document.UpdateTime,User.Name,Category.Name).join(User,Document.UserId==User.Id).filter(Document.Partition==partition).join(Category,Document.CategoryId==Category.Id).order_by(Document.CreateTime).slice(start,stop).all()
        return [{'Id':item[0],'Title':item[1],'CreateTime':item[2],'UpdateTime':item[3],'User':item[4],'Category':item[5]} for item in results]

    def UpdateDocument(self,document):
        self.Session.merge(document)
        self.Session.commit()
        return None

    def ModifyDocument(self,id,**changes):
        self.Session.query(Document).filter(Document.Id==id).update(changes,synchronize_session=False)
        self.Session.commit()
        return None

    def CountDocument(self):
        number=self.Session.query(Document).count()
        return number

    def CountDocumentByCategory(self,category_id):
        number=self.Session.query(Document).filter(Document.CategoryId==category_id).count()
        return number

    def CountDocumentByPartition(self,partition):
        number=self.Session.query(Document).filter(Document.Partition==partition).count()
        return number

    def Execute(self,sql):
        results=self.Session.execute(sql).fetchall()
        return results
