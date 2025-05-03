from app import db

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer,primary_key = True,autoincrement=True)
    name = db.Column(db.Text)
    Job = db.Column(db.Text)
    department = db.Column(db.Text)

    def __repr__(self):
        return f"{self.name} is in {self.department} in {self.Job}"