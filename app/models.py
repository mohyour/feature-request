from app import db


class Feature(db.Model):
    __tablename__ = 'feature'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(300))
    client = db.Column(db.String(60))
    client_priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.DateTime, nullable=False)
    product_areas = db.Column(db.String(32))

    def __repr__(self):
        return '<Feature ()>'.format(self.title)


class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    location = db.Column(db.String(120))

    def __repr__(self):
        return '<Client ()>'.format(self.name)
