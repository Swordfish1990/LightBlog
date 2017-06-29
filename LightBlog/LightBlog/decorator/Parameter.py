from flask import request
from LightBlog.ext import db

def Parameter(model,name):
    def decorator(func):
        def wrapper(*args, **kw):
            if name in kw:
                if kw[name]==None:
                    m=model()
                    for attr_name in [i for i in dir(m) if type(getattr(m,i))==type(db.Column())]:
                        attr_value=request.form[attr_name] if attr_name in request.form else None
                        setattr(m,attr_name,attr_value)
                    kw[name]=m
            else:
                raise Exception('wrong parameter name!')
            return func(*args, **kw)
        return wrapper
    return decorator