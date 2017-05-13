from flask import Blueprint

front=Blueprint('front',__name__,template_folder='templates')
plugin=Blueprint('plugin',__name__,url_prefix='/plugin')

import views
import ueditor 

