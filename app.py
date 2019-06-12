from flask import Flask, render_template, request
import requests, json
app = Flask(__name__)

@app.route("/")
def run():
    return render_template("index.html")

@app.route("/info", methods = ["POST"])
def display_info():
	r = requests.get("https://jsonplaceholder.typicode.com/todos/" + str(request.form.get("id")))
	info_set = json.loads(r.text)
	user_id = info_set['userId']
	id = info_set['id']
	title = info_set['title']
	completed = info_set['completed']
	return render_template("info.html", user_id = user_id, id = id, title = title, completed = completed)


