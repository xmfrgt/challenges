from flask import Flask, render_template, request
from database import initalize_database, execute_query, get_database_handle
import hashlib 

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/<level>')
def level(level):
    return render_template('%s.html'%level)

@app.route('/login1', methods = ['GET'])
def login1():
  username = request.args.get('username')
  password = request.args.get('password')

  correct_creds = ['acbd18db4cc2f85cedef654fccc4a4d8', 'e80eded141e1295d694cd35cf2b8f675']
  username_hash = hashlib.md5(username.encode()).hexdigest()
  pw_hash = hashlib.md5(password.encode()).hexdigest()

  if (username_hash == correct_creds[0] and pw_hash == correct_creds[1]):
    return 'Login Success!'
  else:
    return 'Login Failure'

@app.route('/login2', methods = ['POST'])
def login2():
  username = request.form.get('username')
  password = request.form.get('password')

  correct_creds = ['aa8ae3b340c34010e4500a0d6294dc2c', '592cec0a3fc4d8cf9b6e57a09bff554b']
  username_hash = hashlib.md5(username.encode()).hexdigest()
  pw_hash = hashlib.md5(password.encode()).hexdigest()

  if (username_hash == correct_creds[0] and pw_hash == correct_creds[1]):
    return 'Login Success!'
  else:
    return 'Login Failure'

@app.route('/login3', methods = ['GET'])
def login3():
  auth_header = request.headers.get('Authorization')
  if auth_header:
    try:
      correct_creds = ['80743387e7cd5fb5cc71693b16859e80', '14bb02c03c92af99ac2cb42dea8a1bd2']
      username, password = auth_header.split(':')
      username_hash = hashlib.md5(username.encode()).hexdigest()
      pw_hash = hashlib.md5(password.encode()).hexdigest()
      if (username_hash == correct_creds[0] and pw_hash == correct_creds[1]):
        return 'Login Success!'
      else:
        return 'Login Failure'
    except:
      return "Login Failure"
  else:
    return "Login Failure"

@app.route('/login10', methods = ['POST'])
def login10():
  try:
    query = request.form.get('query')
    conn = get_database_handle(r'users.db')
    res = execute_query(conn, query)
    if len(res) > 0:
      return "success"
    else:
      return "failure"
  except Exception as e:
    print('got exception', e)
    return "failure"

@app.route('/login11', methods = ['POST'])
def login11():
  try:
    query = request.form.get('query')
    conn = get_database_handle(r'users.db')
    res = execute_query(conn, query)
    if len(res) == 1:
      return res[0][1]
    elif len(res) > 1:
      return "SQL Injection attempt detected!"
    else:
      return "failure"
  except Exception as e:
    print('got except', e)
    return "failure"


if __name__ == '__main__':
    # Initalize sqlite database
    initalize_database()
    app.run(debug=True, host='0.0.0.0')