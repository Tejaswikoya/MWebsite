from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://admin:<password>@cluster0.0uzzzz2.mongodb.net/?retryWrites=true&w=majority")

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
      return ""
   else:
        return render_template('login1.html')

@app.route('/signup/student', methods = ['POST', 'GET'])
def signupStudent():
   if request.method == 'POST':
      print(request.form)

      return ""
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