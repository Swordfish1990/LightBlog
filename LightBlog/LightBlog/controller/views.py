
from datetime import datetime
from flask import render_template
from . import front

@front.route('/')
@front.route('/home')
def home(n=1):
    """Renders the home page."""
    return render_template(
        'login.html',
        title='Home Page',
        year=datetime.now().year,
    )

@front.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@front.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )