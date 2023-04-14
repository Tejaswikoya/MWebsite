import pickle
import joblib
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier

model1=joblib.load('case1.joblib')
model2=joblib.load('case2.joblib')
model3=joblib.load('case3.joblib')

encoder=LabelEncoder()


def pred1(values):
    df=pd.DataFrame(values,index=[0])
    fields=os.listdir('./classes1/')
    for column in df.columns:
        if column+'.npy' in fields:
            path='./classes1/'+column+'.npy'
            classes=np.load(path,allow_pickle=True)
            encoder.classes_=classes
            df[column]=encoder.transform(df[column])
    model=joblib.load('case1.joblib')
    pred=model.predict(df)
    y=np.load('./classes1/student_engagement_status.npy',allow_pickle=True)
    pred=pred[0]
    return y[pred]

def pred2(values):
    df=pd.DataFrame(values,index=[0])
    fields=os.listdir('./classes2/')
    for column in df.columns:
        if column+'.npy' in fields:
            path='./classes2/'+column+'.npy'
            classes=np.load(path,allow_pickle=True)
            encoder.classes_=classes
            df[column]=encoder.transform(df[column])
    model=joblib.load('case2.joblib')
    pred=model.predict(df)
    pred=pred[0]
    return pred

def pred3(values):
    df=pd.DataFrame(values,index=[0])
    fields=os.listdir('./classes3/')
    for column in df.columns:
        if column+'.npy' in fields:
            path='./classes3/'+column+'.npy'
            classes=np.load(path,allow_pickle=True)
            encoder.classes_=classes
            df[column]=encoder.transform(df[column])
    model=joblib.load('case3.joblib')
    pred=model.predict(df)
    y=np.load('./classes3/NameofEmployer.npy',allow_pickle=True)
    pred=pred[0]
    pred=y[pred]
    return pred

def pred4(values):
    df=pd.DataFrame(values,index=[0])
    fields=os.listdir('./classes4/')
    for column in df.columns:
        if column+'.npy' in fields:
            path='./classes4/'+column+'.npy'
            classes=np.load(path,allow_pickle=True)
            encoder.classes_=classes
            df[column]=encoder.transform(df[column])
    model=joblib.load('case4.joblib')
    pred=model.predict(df)
    return pred

