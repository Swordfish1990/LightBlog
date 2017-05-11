from flask import Blueprint

front=Blueprint('front',__name__,template_folder='templates')
ueditor=Blueprint('ueditor',__name__,url_prefix='ueditor')
from . import views

