from flask import Flask,Blueprint,render_template
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_restx import Api
from flask_cors import CORS
from .config import Config   
from .models import db
from .views.EmployeesView import nsEmployees as nsemployees
from .views.BeneficiariesView import nsBeneficieries as nsbeneficieries
import requests

def create_app():
    app = Flask(__name__)  
    cors= CORS(app, supports_credentials=False, resources={r"/api/*": {"origins": "*"}})
    bootstrap = Bootstrap(app)
    if Config is None:
        app.config.from_object(Config.BaseConfig)
    else:
        app.config.from_object(Config)

    db.init_app(app)
    
    migrate= Migrate(app, db) 
    ###Routes
    bluePrint = Blueprint('api', __name__, url_prefix='/api/v1')
    api = Api(bluePrint, doc='/doc', version='1.0', title='Employees Configuration API', description='Swagger for Employee Configuration API')
    api.add_namespace(ns=nsemployees)
    api.add_namespace(ns=nsbeneficieries)
    

    app.register_blueprint(bluePrint)
    @app.route('/')                       
    def index():
        return  render_template('index.html')
    @app.route('/beneficiarios')                       
    def beneficiario():
        return  render_template('beneficiarios.html')
    return app