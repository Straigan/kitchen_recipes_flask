from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy_mptt.mixins import BaseNestedSets

from webapp.db import db


class Category(db.Model, BaseNestedSets):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=True)

    def __repr__(self):
        return f'<Category {self.name}>'


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
    category = relationship('Category', backref='recipes', lazy='joined')
    name = db.Column(db.String(180), index=True, nullable=False)
    description = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Recipe name {self.name}, id {self.id}, category {self.category}>'

