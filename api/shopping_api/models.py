from .database import db


class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    image_id = db.Column(db.String(32))

    items = db.relationship("ItemModel", back_populates="category")

    def __repr__(self):
        return '<Category {}>'.format(self.id)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    image_id = db.Column(db.String(32))
    price = db.Column(db.Numeric)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("CategoryModel", back_populates="items")

    def __repr__(self):
        return '<Item {}>'.format(self.id)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class OrderModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)

    card_number = db.Column(db.String(20))
    card_expiry = db.Column(db.String(5))
    card_cvc = db.Column(db.String(4))

    items = db.relationship("OrderItemModel", back_populates="order")

    def __repr__(self):
        return '<Order {}>'.format(self.id)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class OrderItemModel(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Numeric)
    quantity = db.Column(db.Integer)

    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    order = db.relationship("OrderModel", back_populates="items")

    def __repr__(self):
        return '<OrderItem {}>'.format(self.id)

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
