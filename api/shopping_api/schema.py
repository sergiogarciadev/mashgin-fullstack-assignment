from flask_marshmallow import Marshmallow
from marshmallow.fields import Float
from .models import CategoryModel, ItemModel, OrderModel, OrderItemModel


ma = Marshmallow()


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel
        load_instance = True
        include_fk= True


class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_instance = True
        include_fk= True

    price = Float()


class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderItemModel
        load_instance = True
        include_fk= True

    price = Float()


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderModel
        load_instance = True
        include_fk= True

    items = ma.List(ma.Nested(OrderItemSchema))
