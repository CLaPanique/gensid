from flask import Flask, request, jsonify 
import samino
app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def login():
  data = request.form
  email = data["email"]
  password = data["password"]
  device = data["device"]
  client = samino.Client(device)
  login = client.login(email,password).json
  return jsonify(login)
