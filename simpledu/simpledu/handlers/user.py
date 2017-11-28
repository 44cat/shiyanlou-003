from flask import Blueprint,render_template
from simpledu.models import User

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/admin')
def index():
    users = User.query.all()
    if users is None:
        return 404
    else:
        return render_template('user.html',users=users)
