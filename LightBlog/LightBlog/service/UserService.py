from LightBlog.ext import db
from LightBlog.model.User import User

class UserService(object):
    """description of class"""

    def __init__(self):
        self.Session=db.session

    def AddUser(self,user):
        self.Session.add(user)
        self.Session.commit()
        return None

    def GetUser(self,id):
        user=self.Session.query(User).get(id)
        return user

    def RemoveUser(self,id):
        self.Session.query(User).filter(User.Id==id).delete(synchronize_session=False)
        self.Session.commit()
        return None

    def ListUsers(self,start,stop):
        users=self.Session.query(User).order_by(User.Id).slice(start,stop)
        return users

    def UpdateUser(self,user):
        self.Session.merge(user)
        self.Session.commit()
        return None

    def ModifyUser(self,id,**changes):
        self.Session.query(User).filter(User.Id==id).update(changes,synchronize_session=False)
        self.Session.commit()
        return None

    def GetUserNumber(self):
        number=self.Session.query(User).count()
        return number

    def Execute(self,sql):
        results=self.Session.execute(sql).fetchall()
        return results

