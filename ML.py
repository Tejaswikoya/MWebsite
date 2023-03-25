import pickle
import joblib
from sklearn.preprocessing import LabelEncoder
import numpy as np

model1=joblib.load('case1.joblib')
model2=joblib.load('case2.joblib')
model3=joblib.load('case3.joblib')

encoder1=LabelEncoder()
encoder1.classes_=np.load('classes1.npy',allow_pickle=True)
encoder2=LabelEncoder()
encoder2.classes_=np.load('classes2.npy',allow_pickle=True)
encoder3=LabelEncoder()
encoder3.classes_=np.load('classes3.npy',allow_pickle=True)


def pred1():
    return ""

def pred2():
    return ""

def pred3():
    return ""

