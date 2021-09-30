from decimal import Decimal
from datetime import datetime

from flask import request
from flask_restplus import Resource, fields, Namespace

from .models import CategoryModel, ItemModel, OrderModel
from .schema import CategorySchema, ItemSchema, OrderSchema



CATEGORY_NOT_FOUND = "Category not found."
ITEM_NOT_FOUND = "Item not found."
ORDER_NOT_FOUND = "Order not found."
ORDER_ITEM_NOT_FOUND = "Order Item not found."

category_ns = Namespace('category', description='Category related operations')
item_ns = Namespace('item', description='Item related operations')
order_ns = Namespace('order', description='Order related operations')

category_schema = CategorySchema()
category_list_schema = CategorySchema(many=True)

item_schema = ItemSchema()
item_list_schema = ItemSchema(many=True)

order_schema = OrderSchema()
order_list_schema = OrderSchema(many=True)


category = category_ns.model('Category', {
    'name': fields.String(description='Name of the category'),
    'image_id': fields.String(description='Image of the category'),
})

item = item_ns.model('Item', {
    'name': fields.String(description='Name of the item'),
    'image_id': fields.String(description='Image of the item'),
    'price': fields.Float(description='Price of the item'),
    'category_id': fields.Integer(description='Category of the item')
})

order_item = order_ns.model('OrderItem', {
    'item_id': fields.String(description='Id of the item'),
    'name': fields.String(description='Name of the item when order was created'),
    'price': fields.Float(description='Price of the item when order was created'),
    'quantity': fields.Integer(description='Quantity of purchased items'),
})

order = order_ns.model('Order', {
    'timestamp': fields.String(description='Timestamp of the order'),

    'card_number': fields.String(description='Card Number'),
    'card_expiry': fields.String(description='Card Expiry'),
    'card_cvc': fields.String(description='Card CVC'),

    'items': fields.List(fields.Nested(order_item), description='Item in the order'),
})



class Category(Resource):
    @category_ns.doc('Get a Category')
    @category_ns.response(200, 'Success')
    @category_ns.response(404, 'Not Found')
    def get(self, id):
        category_data = CategoryModel.query.filter_by(id=id).first()
        if category_data:
            return category_schema.dump(category_data)
        return {'message': CATEGORY_NOT_FOUND}, 404

    @category_ns.doc('Delete a Category')
    @category_ns.response(200, 'Success')
    @category_ns.response(404, 'Not Found')
    def delete(self, id):
        category_data = CategoryModel.query.filter_by(id=id).first()
        if category_data:
            category_data.delete_from_db()
            return {'message': "Category Deleted successfully"}, 200
        return {'message': CATEGORY_NOT_FOUND}, 404

    @category_ns.doc('Create or Update a Category')
    @category_ns.expect(category)
    @category_ns.response(200, 'Success')
    def put(self, id):
        category_data = CategoryModel.query.filter_by(id=id).first()
        category_json = request.get_json()

        if category_data:
            category_data.name = category_json['name']
            category_data.image_id = category_json['image_id']
        else:
            category_data = category_schema.load(category_json)

        category_data.save_to_db()
        return category_schema.dump(category_data), 200


class CategoryList(Resource):
    @category_ns.doc('Get all the Categories')
    @category_ns.response(200, 'Success')
    def get(self):
        return category_list_schema.dump(CategoryModel.query.all()), 200

    @category_ns.expect(category)
    @category_ns.doc('Create a Category')
    @category_ns.response(201, 'Created')
    def post(self):
        category_json = request.get_json()
        category_data = category_schema.load(category_json)
        category_data.save_to_db()

        return item_schema.dump(category_data), 201


class Item(Resource):
    @item_ns.doc('Get an Item')
    @item_ns.response(200, 'Success')
    @item_ns.response(404, 'Not Found')
    def get(self, id):
        item_data = ItemModel.query.filter_by(id=id).first()
        if item_data:
            return item_schema.dump(item_data)
        return {'message': ITEM_NOT_FOUND}, 404

    @item_ns.doc('Delete an Item')
    @item_ns.response(200, 'Success')
    @item_ns.response(404, 'Not Found')
    def delete(self, id):
        item_data = ItemModel.query.filter_by(id=id).first()
        if item_data:
            item_data.delete_from_db()
            return {'message': "Item Deleted successfully"}, 200
        return {'message': ITEM_NOT_FOUND}, 404

    @item_ns.doc('Create or Update an Item')
    @item_ns.expect(item)
    @item_ns.response(200, 'Success')
    def put(self, id):
        item_data = ItemModel.query.filter_by(id=id).first()
        item_json = request.get_json()

        if item_data:
            item_data.name = item_json['name']
            item_data.price = Decimal(item_json['price'])
            item_data.image_id = item_json['image_id']
            item_data.category_id = item_json['category_id']
        else:
            item_data = item_schema.load(item_json)

        item_data.save_to_db()
        return item_schema.dump(item_data), 200


class ItemList(Resource):
    @item_ns.doc('Get all the Items')
    @item_ns.response(200, 'Success')
    def get(self):
        return item_list_schema.dump(ItemModel.query.all()), 200

    @item_ns.expect(item)
    @item_ns.doc('Create an Item')
    @item_ns.response(201, 'Created')
    def post(self):
        item_json = request.get_json()
        item_data = item_schema.load(item_json)
        item_data.save_to_db()

        return item_schema.dump(item_data), 201


class Order(Resource):
    @order_ns.doc('Get an Order')
    @order_ns.response(200, 'Success')
    @order_ns.response(404, 'Not Found')
    def get(self, id):
        order_data = OrderModel.query.filter_by(id=id).first()
        if order_data:
            return order_schema.dump(order_data)
        return {'message': ORDER_NOT_FOUND}, 404

    @order_ns.doc('Delete an Order')
    @order_ns.response(200, 'Success')
    @order_ns.response(404, 'Not Found')
    def delete(self, id):
        order_data = OrderModel.query.filter_by(id=id).first()
        if order_data:
            order_data.delete_from_db()
            return {'message': "Category Deleted successfully"}, 200
        return {'message': ORDER_NOT_FOUND}, 404

class OrderList(Resource):
    @order_ns.doc('Get all the Orders')
    @order_ns.response(200, 'Success')
    def get(self):
        return category_list_schema.dump(OrderModel.query.all()), 200

    @order_ns.expect(order)
    @order_ns.doc('Create an Order')
    @order_ns.response(201, 'Created')
    def post(self):
        order_json = request.get_json()
        order_data = order_schema.load(order_json)
        order_data.timestamp = datetime.now()

        order_data.card_number = order_data.card_number.replace(' ', '')
        order_data.card_number = order_data.card_number[:4] + '********' + order_data.card_number[-4:]

        for order_item in order_data.items:
            item = ItemModel.query.filter_by(id=order_item.item_id).first()
            order_item.price = item.price
            order_item.name = item.name

        order_data.save_to_db()

        return order_schema.dump(order_data), 201
