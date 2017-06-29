from LightBlog.model.Document import Document
from LightBlog.repository.DocumentRepository import DocumentRepository

class DocumentService(object):
    """description of class"""

    def __init__(self):
        self.DocumentRespository=DocumentRepository()

    def AddDocument(self,document):
        self.DocumentRespository.AddDocument(document)
        return None

    def GetDocument(self,id):
        return self.DocumentRespository.GetDocument(id)

    def RemoveDocument(self,id):
        self.Session.query(Document).filter(Document.Id==id).delete(synchronize_session=False)
        self.Session.commit()
        return None

    def ListDocuments(self,start,stop):
        documents=self.Session.query(Document).order_by(Document.CreateTime).slice(start,stop)
        return documents

    def ListDocumentsByCategory(self,category_id,start,stop):
        documents=self.Session.query(Document).filter(Document.CategoryId==category_id).order_by(Document.CreateTime).slice(start,stop)
        return documents

    def ListDocumentsByPartition(self,partition,start,stop):
        documents=self.Session.query(Document).filter(Document.Partition==partition).order_by(Document.CreateTime).slice(start,stop)
        return documents

    def UpdateDocument(self,document):
        self.Session.merge(document)
        self.Session.commit()
        return None

    def ModifyDocument(self,id,**changes):
        self.Session.query(Document).filter(Document.Id==id).update(changes,synchronize_session=False)
        self.Session.commit()
        return None

    def GetDocumentNumber(self):
        number=self.Session.query(Document).count()
        return number

    def GetDocumentNumberByCategory(self,category_id):
        number=self.Session.query(Document).filter(Document.CategoryId==category_id).count()
        return number

    def GetDocumentNumberByPartition(self,partition):
        number=self.Session.query(Document).filter(Document.Partition==partition).count()
        return number

    def Execute(self,sql):
        results=self.Session.execute(sql).fetchall()
        return results

