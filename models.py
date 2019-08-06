# For more details, see
# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#declare-a-mapping
from anthill.framework.db import db
from anthill.framework.utils import timezone
from sqlalchemy.ext.hybrid import hybrid_property


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.DateTime, default=timezone.now)
    content = db.Column(db.Text, nullable=False)
    enabled = db.Column(db.Boolean, nullable=False, default=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    image = db.Column(db.ImageType(width=None, height=None))

    @hybrid_property
    def active(self):
        return self.enabled and self.created <= timezone.now()

    @active.expression
    def active(cls) -> bool:
        return db.and_(
            cls.created <= timezone.now(),
            cls.enabled
        )


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.String(512), nullable=False)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category(name=%s)>' % self.name

