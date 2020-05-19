# Flask maps HTTP requests to Python functions.
import techtinium_assignment
import flask
from flask import request, jsonify


app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route("/", methods=['GET'])
def home():
	return "<h2> Techtinium Assignment API </h2>"

@app.route("/api", methods=['GET'])
def api():

	if 'capacity' and 'hours' in request.args:
		capacity_units = int(request.args['capacity'])
		hours = int(request.args['hours'])
	else:
		return "No argument provided"

	result = []
	result_dict = techtinium_assignment.assignment(capacity_units, hours)
	result.append(result_dict)
	return jsonify(result)

if __name__ == "__main__":
	app.run()