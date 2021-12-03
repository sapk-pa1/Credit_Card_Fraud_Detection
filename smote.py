from sklearn.model_selection import train_test_split
x_train , x_test , y_train, y_test = train_test_split(x,y,test_size= 0.6, random_state=12)

from imblearn.over_sampling import SMOTE


oversample = SMOTE()

overSM_x_train,overSM_y_train = oversample.fit_resample(x_train,y_train)




##After Oversampling using the smote 
print("After Oversampling:")
no_of_fraud_records = len(overSM_y_train[overSM_y_train==1])
print(no_of_fraud_records)
no_of_valid_records = len(overSM_y_train[overSM_y_train==0])
print(no_of_valid_records)
