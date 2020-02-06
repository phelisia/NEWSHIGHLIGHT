from flask import Flask
# from .config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options
from .request import configure_request

bootstrap  = Bootstrap()
def create_app(config_name):
# Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')
    # Initializing Flask Extensions
    # bootstrap = Bootstrap(app)
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #Setting Config
    configure_request(app)

    return app