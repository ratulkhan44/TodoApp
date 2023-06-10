from db_init import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    status = db.Column(db.Boolean())

    def __repr__(self):
        return f'<Post "{self.name}">'