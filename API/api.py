import flask
from flask import request, jsonify
import GenerateUUID

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return ["At Root"]

@app.route('/api/v1/GenerateUUID', methods = ['POST'])
def api_all():
    data = request.form
    print(data["count"])
    if data["count"]>0:
        GenerateUUID.UUID(data.count)
    return GenerateUUID.getUUID()

app.run()