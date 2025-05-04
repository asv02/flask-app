from flask import Flask
from blueprintsapp.app import db


class todo(db.Model):
    __tablename__= "todos"
    tid = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String,nullable = False)
    description = db.Column(db.String,nullable = False)
    status = db.Column(db.String,nullable = False,default = "TODO")
    
    def __repr__(self):
        return f"{self.task} -> {self.description} is {self.status}"
    
    def getId(self):
        return f"{self.tid}"
