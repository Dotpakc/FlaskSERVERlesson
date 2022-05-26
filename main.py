from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'first_name': 'John','last_name': 'Robin','age':35},
    {'first_name': 'Bob','last_name': 'Dilin','age':64},
    {'first_name': 'Mark','last_name': 'Pool','age':24},
    {'first_name': 'Mark2','last_name': 'Pool2','age':21},
    {'first_name': 'Mark3','last_name': 'Pool3','age':43},
    {'first_name': 'Mark4','last_name': 'Pool4','age':54},
    {'first_name': 'Mark5','last_name': 'Pool5','age':33}
]

@app.route("/")
def hello_world():
    return render_template("index.html",users = users)



if __name__ == "__main__":
    app.run()