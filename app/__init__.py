from flask import Flask        # , jsonify
from flask_restful import Api  # , Resource
from pprint import pprint
from app.views import User
from app.models import Oracle

def create_app():
    app: Flask = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    #print(app.config)
    db = Oracle()
    pprint(db.query("select owner, count(*) from all_tables group by owner order by 2 desc"))

    # rejestruje API users (nazwe usera podaje sie w sciezce a nie jako parametr URI)
    api.add_resource(User, '/users/<string:name>')

    # dodaje domyslna strone aplikacji
    @app.route("/")
    def test():
        return "Test 1,2,3,..."

    return app

