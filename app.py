import flask
from flask_pymongo import PyMongo
import json

app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)

@app.route('/')
def index():
    return flask.render_template('index.html', has_result=False)

@app.route('/signup', methods=['POST'])
def signup():
	user = flask.request.form['username']
	print(user)
	result = mongo.db.users.find({"name": user})
	if(result.count() == 0):
		mongo.db.users.insert({"name": user})
		return json.dumps({"success": 1})
	else:
		print('用户已存在')
		return json.dumps({"success": 0})

@app.route('/login', methods=['POST'])
def login():
	user = flask.request.form['username']
	print(user)
	result = mongo.db.users.find({"name": user})
	if(result.count() == 0):
		print('用户不存在')
		return json.dumps({"success": 0})
	else:
		return json.dumps({"success": 1})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=10086)
