from flask import Flask
from flask_login import LoginManager

from webapp.db import posts, users
# from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

# from webapp.user.models import Client, Credit
from webapp.config import SECRET_KEY, WTF_CSRF_TIME_LIMIT
from webapp.user.forms import LoginForm

from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    app.config['SECRET_KEY'] = 'ehuiwevwevwbveu'

    # migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)


    # @app.route('/')
    # def flask_mongodb_atlas():
    #     return "flask mongodb atlas!"
    #
    # @app.route('/db')
    # def test():
    #     try:
    #         users.insert_one({"first_name": "Gina", "last_name": "Grey"})
    #         return "Connected to the data base!"
    #     except:
    #         return "error base..."
    #
    # @app.route("/dbout")
    # def test2():
    #     post = posts.find_one()
    #     view = post['username']
    #     return view

    @login_manager.user_loader
    def load_user(user_id):
        return users.find({'id': user_id})

    if __name__ == '__main__':
        app.run(debug=True)

    return app
