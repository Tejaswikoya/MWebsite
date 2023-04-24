from flask import Flask, render_template, request
import pymongo
import pickle
import ML
import numpy as np

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.0uzzzz2.mongodb.net/?retryWrites=true&w=majority")
db=client['mydb']
currentUser=""

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
         global currentUser
         currentUser=x['email']
         return render_template('student.html',email=x['email'],name=(str(x['first_name']+" "+str(x['last_name']))),college=x['college'])
      else:
         return render_template('login1.html')
   else:
        return render_template('login1.html')
   
@app.route('/student',methods=['GET'])
def student():
   return render_template('student.html')

@app.route('/signup/student', methods = ['POST', 'GET'])
def signupStudent():
   if request.method == 'POST':
      print(request.form)
      newUser={
         "email":request.form['email'],
         "password":request.form['psw'],
         "gender":request.form['gender'],
         "college":request.form['college'],
         "first_name":request.form['first_name'],
         "last_name":request.form['last_name']
      }
      coll=db['students']
      coll.insert_one(newUser)
      currentUser=request.form['email']
      return render_template('student.html',name=request.form['email'])
   else:
        return render_template('signup.html')

@app.route('/login/admin',methods = ['POST', 'GET'])
def loginAdmin():
   if request.method == 'POST':
      coll=db['students']
      res=coll.find()
      data=[]
      for temp in res:
         tempData=[]
         tempData.append(temp['email'])
         tempData.append(temp['college'])
         tempData.append(str(temp['first_name'])+str(temp['last_name']))
         data.append(tempData)
      return render_template('adminPage.html',data=data)
   else:
        return render_template('login2.html')

@app.route('/admin',methods=['POST','GET'])
def showPage():
   if request.method=='GET':
      args=request.args
      print(args['email'])
      query={"email":args['email']}
      coll=db['students']
      res=coll.find_one(query)
      if 'form1' in res:
         f1=res['form1']
      else:
         f1='not filled'
      if 'form2' in res:
         f2=res['form2']
      else:
         f2='not filled'
      if 'form3' in res:
         f3=res['form3']
      else:
         f3='not filled'
      if 'form4' in res:
         f4=res['form4']
      else:
         f4='not filled'
      return render_template('usersPage.html',f1=f1,f2=f2,f3=f3,f4=f4)

@app.route('/student/form1',methods=['GET','POST'])
def form1():
   if request.method=='POST':
      inputs={}
      for i in request.form:
         inputs[i]=request.form[i]
      pred=ML.pred1(inputs)
      query={"email":currentUser}
      update={"$set":{"form1":str(pred)}}
      coll=db['students']
      coll.update_one(query,update)
      return render_template('submission.html')
   else:
      return render_template('form1.html')

@app.route('/student/form2',methods=['GET','POST'])
def form2():
   if request.method=='POST':
      inputs={}
      for i in request.form:
         inputs[i]=request.form[i]
      pred=ML.pred2(inputs)
      query={"email":currentUser}
      update={"$set":{"form2":str(pred)}}
      coll=db['students']
      coll.update_one(query,update)
      return render_template('submission.html')
   else:
      return render_template('form2.html')

@app.route('/student/form3',methods=['GET','POST'])
def form3():
   if request.method=='POST':
      inputs={}
      for i in request.form:
         inputs[i]=request.form[i]
      pred=ML.pred3(inputs)
      print(pred)
      query={"email":currentUser}
      update={"$set":{"form3":pred}}
      coll=db['students']
      print(update)
      coll.update_one(query,update)
      return render_template('submission.html')
   else:
      return render_template('form3.html')

@app.route('/student/form4',methods=['GET','POST'])
def form4():
   if request.method=='POST':
      inputs={}
      for i in request.form:
         inputs[i]=request.form[i]
      pred=ML.pred4(inputs)
      query={"email":currentUser}
      update={"$set":{"form4":str(pred)}}
      coll=db['students']
      coll.update_one(query,update)
      print(request.form)
      return render_template('submission.html')
   else:
      return render_template('form4.html')


if __name__ == "__main__":
    app.run(debug=True)