from flask import Flask, render_template, request
import hashlib 

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/level1')
def level1():
    return render_template('level1.html')

@app.route('/level2')
def level2():
  return render_template('level2.html')

@app.route('/level3')
def level3():
  return render_template('level3.html')

@app.route('/level4')
def level4():
  return render_template('level4.html')

@app.route('/level5')
def level5():
  return render_template('level5.html')

@app.route('/login1', methods = ['GET'])
def login1():
  username = request.args.get('username')
  password = request.args.get('password')

  # foo - wordpass
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

  # kar - willow
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
      # wre - trout
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')