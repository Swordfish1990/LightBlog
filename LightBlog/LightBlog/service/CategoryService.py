from LightBlog.model.Category import Category
from LightBlog.repository.CategoryRepository import CategoryRepository

class CategoryService(object):
    
    def __init__(self):
        self.CategoryRepository=CategoryRepository()

    def AddCategory(self,category):
        self.CategoryRepository.AddCategory(category)
        return None

    def RemoveCategory(self,id):
        self.CategoryRepository.RemoveCategory(id)
        return None
    
    def ListCategories(self,start,stop):
        return self.CategoryRepository.ListCategories(start,stop)

    def UpdateCategory(self,category):
        self.CategoryRepository.UpdateCategory(category)
        return None
    
    def GetCategoriesNumber(self):
        return self.CategoryRepository.GetCategoriesNumber()




