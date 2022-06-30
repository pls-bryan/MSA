import flask
from flask import request, jsonify
import student_processor

app = flask.Flask(__name__)

app.config["DEBUG"] = True
#Creating site data
student_dictionaries = student_processor.get_student_dictionaries()

#Create Routes to webpages
@app.route('/', methods=['GET'])
def home():
    return'''<h1>Student Data API</h1>
    <p>This site makes student data available to you!</p>'''

#return all students
@app.route('/api/v1/resources/students/all', methods=['GET'])
def api_all():
    return jsonify(student_dictionaries)

#return students by id
@app.route('/api/v1/resources/students', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "ERROR: No ID field provided. Please specify an ID."
    results = []

    for student in student_dictionaries:
        if id == student['id']:
            results.append(student)
            return jsonify(results)

    return f"Student with ID {id} not found."        
    
app.run()
