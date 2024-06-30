from flask import Flask , render_template, request, redirect , url_for, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId #Imported ObjectId from bson to correctly identify and manipulate MongoDB documents

app = Flask(__name__)

#Mongo Setup
client = MongoClient('localhost', 27017)  # Default port used if no port provided  , this can also be used 'mongodb://localhost:27017/'
db = client.todo_db
todos_collection = db.todos

@app.route('/')  #The main route renders the list of to-do items.
def index():
    todos= list(todos_collection.find()) #fetching all the todos from the database
    return render_template('index.html',todos=todos) #passing the todos to the template

@app.route('/add', methods=['POST']) #route for adding a new todo
def add_todo():
    todo_item= request.form.get('todo') #getting the todo item from the form
    todos_collection.insert_one({"task": todo_item , "completed" :False}) #inserting the todo item into the database
    return redirect(url_for('index')) #redirecting to the index page

@app.route("/delete/<todo_id>", methods= ["POST"])#route for deleting a todo
def delete_todo(todo_id):
    todos_collection.delete_one({"_id": ObjectId(todo_id)}) #deleting the todo from the database
    return redirect(url_for('index')) #redirecting to the index page



@app.route("/toggle/<todo_id>", methods= ["POST"])#route for toggling a todo
def toggle_todo(todo_id):
    todo = todos_collection.find_one({"_id": ObjectId(todo_id)}) #fetching the todo from the database
    todos_collection.update_one({"_id": ObjectId(todo_id)}, {"$set": {"completed": not todo["completed"]}}) #toggling the completed status of the todo
    return redirect(url_for('index')) #redirecting to the index page

if __name__ == '__main__':
    app.run(debug=True)


