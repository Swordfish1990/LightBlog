from LightBlog.model.User import User
from LightBlog.repository.UserRepository import UserRepository
from LightBlog.tools.EncryptHelper import EncryptHelper

class UserService(object):
    """description of class"""

    def __init__(self):
        self.UserRepository=UserRepository()
        self.MD5=md5.new()

    def AddUser(self,user):
        user.Password=EncryptHelper.GetMD5(user.Password)
        self.UserRepository.AddUser(user)
        return None

    def RemoveUser(self,id):
        self.UserRepository.RemoveUser(id)
        return None

    def ListUsers(self,start,stop):
        return self.UserRepository.ListUsers(start,stop)

    def ChangeUserName(self,id,name):
        self.UserRepository.ModifyUser(id,Name=name)
        return None

    def ChangeUserPassword(self,id,password):
        password=EncryptHelper.GetMD5(password)
        self.UserRepository.ModifyUser(id,Password=password)
        return None

    def GetUserNumber(self):
        return self.UserRepository.GetUserNumber()

    def Login(self,user_name,user_password):
        user_password=EncryptHelper.GetMD5(user_password)
        user=self.UserRepository.GetUserByFilter(Name=user_name,Password=user_password)
        return user

