from . import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    entity_name = db.Column(db.String(100), nullable=False)
    task_type = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)
    note = db.Column(db.Text)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Task {self.entity_name}>"
