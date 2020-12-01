import flask
from flask import request, jsonify
import json
import UUID

app = flask.Flask(__name__)
app.config["DEBUG"] = True
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

@app.route('/', methods=['GET'])
def home():
    y = UUID.UUID()
    return jsonify(y.getUUID())

@app.route('/api/v1/UUID', methods = ['POST'])
def api_all():
    data = request.json
    y = UUID.UUID(int(data["count"]))
    return jsonify(y.getUUID())

app.run()