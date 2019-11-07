from app import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.Text)
    complete = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, name, description, complete):
        self.name = name
        self.description = description
        self.complete = complete

    def __repr__(self):
        return "<Task %r>" % self.name
