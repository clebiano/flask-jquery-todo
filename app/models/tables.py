from app import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    complete = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, title, complete):
        self.title = title
        self.complete = complete

    def __repr__(self):
        return "<Task %r>" % self.title
