from flask import Flask, render_template, make_response, request

app = Flask(__name__)

@app.route("/")
def index():
  resp = make_response(render_template('index.html'))
  resp.mimetype = 'text/html'
  return resp

@app.route("/user", methods=['POST'])
def create_user():
  request.form.get('firstname')
  resp = make_response(render_template('user.html', firstname=request.form.get('firstname'), lastname=request.form.get('lastname')))
  resp.mimetype = 'text/html'
  return resp
  