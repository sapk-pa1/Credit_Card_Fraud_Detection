import pandas as pd 
from visualization import visualize_data 
from smote import oversampling
from sklearn.model_selection import train_test_split
from TSNE import dim_reduc


## main file for the project 
## Edit 1 By Pawan Sapkota Sharma 

dataset = pd.read_csv("./dataset/creditcard.csv")
sample_data = dataset.sample(frac = 0.5, random_state = 1)
x = sample_data.drop(['Class', 'Time'], axis = 1)
y = sample_data['Class']
x_train , x_test , y_train, y_test = train_test_split(x,y,test_size= 0.6, random_state=12)
# Fraud and Valid case from the sample data 
fraud= sample_data[sample_data["Class"] ==1]
valid = sample_data[sample_data["Class"]==0]
print("Valid Cases = "+ str(valid.size))
print("Fraud Cases = "+ str(fraud.size))
# v_features = ["V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13",
# "V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28"]
# data_needed_for_visualization = [sample_data, valid, fraud, v_features]
visualize_data(sample_data)
dim_reduc(x)
oversampling(x_train, y_train)
