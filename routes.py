from models import Person
from flask import request,render_template

def register_routes(app,db):
    @app.route('/',methods = ['GET','POST'])
    def register_user():
        if request.method == 'POST':
            name = request.form.get('name')
            department = request.form.get('department')
            job = request.form.get('job')
            
            p1 = Person(name = name,department = department,Job = job)

            db.session.add(p1)
            db.session.commit()
            people = Person.query.all()
            print("People->",type(people))
            return render_template('index.html',People=people),200
        else:
            people = Person.query.all()
            return render_template('index.html',People=people),200


