#!flask/bin/python

from flask import Flask,jsonify
from flask_cors import CORS
from flask import request

from modules.places import search

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


@app.route('/place', methods=['POST'])
def sample():
	req_data = request.get_json()
	source = req_data['source']
	lat,lon,radius = source['lat'],source['lon'],source['radius']
	result = search(lat,lon,radius)
	result = jsonify({'result':result})
	
	return result

if __name__ == '__main__':
    app.run(debug=True)