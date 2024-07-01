from flask import Flask # type: ignore
from flask_cors import CORS

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config['CORS_HEADERS'] = 'Content-Type'


    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.customer import bp as customer_bp
    app.register_blueprint(customer_bp, url_prefix='/customer')
    
    from app.employee import bp as employee_bp
    app.register_blueprint(employee_bp, url_prefix='/employee')
    
    from app.order import bp as order_bp
    app.register_blueprint(order_bp, url_prefix='/order')
    
    from app.product import bp as product_bp
    app.register_blueprint(product_bp, url_prefix='/product')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app