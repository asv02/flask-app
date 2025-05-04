from flask import Flask,render_template,Blueprint,request,redirect,url_for
from blueprintsapp.todoblueprint.models import todo
from blueprintsapp.app import db

blue = Blueprint("todoblueprint",__name__,template_folder ="templates")

@blue.route('/')
def index():
   todos = todo.query.all()
   return render_template('todoblueprint/todoblueprint.html',todos=todos)

@blue.route('/create_todo',methods=['GET','POST'])
def create():
   
   if request.method == 'GET':
       todos = todo.query.all()
       return render_template('todoblueprint/createtodo.html')   
   elif request.method == 'POST':
      info = request.form
      task = info.get('task')
      description = info.get('description')
      status = info.get('status')
      
      new_todo = todo(task = task,description=description,status=status) 
     
      db.session.add(new_todo)
      db.session.commit()
      return redirect(url_for('todoblueprint.index'))

@blue.route('/delete_todo/<int:tid>',methods = ['Delete'])
def delete_todo(tid):
   to_do = db.query.filter(tid)

   db.session.delete(to_do)
   db.session.commit()


      