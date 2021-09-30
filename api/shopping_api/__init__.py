import os

from flask import Blueprint, jsonify
from flask_migrate import upgrade
from flask_restplus import Api
from marshmallow import ValidationError

from .app import app
from .database import db, migrate
from .schema import ma
from .resources import Category, CategoryList, Item, ItemList, Order, OrderList, category_ns, item_ns, order_ns


api_blueprint = Blueprint('api', 'shopping_api', url_prefix='/api')
api = Api(api_blueprint, doc='/doc', title='Mashgin Shopping API')
app.register_blueprint(api_blueprint)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


api.add_namespace(category_ns)
api.add_namespace(item_ns)
api.add_namespace(order_ns)


category_ns.add_resource(Category, '/<int:id>')
category_ns.add_resource(CategoryList, "")
item_ns.add_resource(Item, '/<int:id>')
item_ns.add_resource(ItemList, "")
order_ns.add_resource(Order, '/<int:id>')
order_ns.add_resource(OrderList, "")


@app.before_first_request
def create_tables():
    upgrade()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)
