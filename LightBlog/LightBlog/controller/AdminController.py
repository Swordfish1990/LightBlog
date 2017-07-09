#coding:utf-8

from datetime import datetime
from flask import render_template
from LightBlog.settings import AdminSettings
from LightBlog.controller import admin
from LightBlog.repository.CategoryRepository import CategoryRepository
from LightBlog.repository.DocumentRepository import DocumentRepository
from LightBlog.repository.UserRepository import UserRepository

categoryRepository=CategoryRepository()
documentRepository=DocumentRepository()
userRepository=UserRepository()

@admin.route('/')
@admin.route('/document')
def document(category_id=None,page_index=0):
    start=page_index*AdminSettings.PageLength
    stop=(page_index+1)*AdminSettings.PageLength-1
    documents=documentRepository.ListDocumentsInfo(start,stop) if category_id==None else documentRepository.ListDocumentsInfoByCategory(category_id,start,stop)
    print documents[0]
    document_amount=documentRepository.CountDocument() if category_id==None else documentRepository.CountDocumentByCategory(category_id)
    page_amount=document_amount/AdminSettings.PageLength if document_amount%AdminSettings.PageLength==0 else document_amount/AdminSettings.PageLength+1
    categories=categoryRepository.ListAllCategories()
    return render_template(
        'document.html',
        title='文章列表',
        categories=categories,
        documents=documents,
        page_index=page_index,
        page_amount=page_amount
    )