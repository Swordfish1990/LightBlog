from flask import Blueprint

front=Blueprint('front',__name__,template_folder='templates',url_prefix='/views')
plugin=Blueprint('plugin',__name__,url_prefix='/plugin')
admin=Blueprint('admin',__name__,template_folder='templates')

import views
import ueditor
import AdminController

