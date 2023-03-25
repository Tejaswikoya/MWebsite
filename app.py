from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.0uzzzz2.mongodb.net/?retryWrites=true&w=majority")
db=client['mydb']

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('demo1.html')

@app.route('/login/student', methods = ['POST', 'GET'])
def loginStudent():
   if request.method == 'POST':
      print(request.form)
      credentials={
         "email":request.form['email'],
         "password":request.form['psw']
      }
      coll=db['students']
      x=coll.find_one(credentials)
      if(x):
         return render_template('student.html',name=request.form['email'])
      else:
         return render_template('login1.html')
   else:
        return render_template('login1.html')

@app.route('/signup/student', methods = ['POST', 'GET'])
def signupStudent():
   if request.method == 'POST':
      print(request.form)
      newUser={
         "email":request.form['email'],
         "password":request.form['psw'],
         "gender":request.form['gender'],
         "college":request.form['college']
      }
      coll=db['students']
      coll.insert_one(newUser)
      return render_template('student.html',name=request.form['email'])
   else:
        return render_template('signup.html')

@app.route('/login/admin',methods = ['POST', 'GET'])
def loginAdmin():
   if request.method == 'POST':
      print(request.form)
      return ""
   else:
        return render_template('login2.html')



if __name__ == "__main__":
    app.run(debug=True)