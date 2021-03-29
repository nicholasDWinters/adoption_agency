from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    '''model for a pet'''
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable = False)
    species = db.Column(db.String(50), nullable = False)
    photo_url = db.Column(db.String(1000), nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.String(1000), nullable = True)
    available = db.Column(db.Boolean, nullable = False, default = True)
