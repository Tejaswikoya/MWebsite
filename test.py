import numpy as np
import os

for column in os.listdir('./classes4/'):    
    path='./classes4/'+column
    classes=np.load(path,allow_pickle=True)
    print(column)
    print(classes)

