from flask import Flask
from .api.v1.views import api_views
from config import Config
from db_init import db
from flask_cors import CORS,cross_origin


def settings_api_hub(debug):
    try:
        config_class = Config()
        api_init = Flask(__name__)
        api_init.config["DEBUG"] = debug
        api_init.config.from_object(config_class)
        CORS(api_init,resources={r"/": {"origins": "*"}})
        api_init.config['CORS_HEADERS'] = 'Content-Type'
        # Initialize Flask extensions here
        db.init_app(api_init)
        with api_init.app_context():
            db.create_all()

        api_init.register_blueprint(api_views, url_prefix="/")

        return api_init
    
    except Exception as e:
        print(f"Integration error : {e.args[0]}")