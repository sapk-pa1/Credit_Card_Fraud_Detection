
from imblearn.over_sampling import SMOTE


def oversampling(x_train, y_train):
    oversample = SMOTE()
    overSM_x_train,overSM_y_train = oversample.fit_resample(x_train,y_train)
    ##After Oversampling using the smote 
    print("After Oversampling:")
    no_of_fraud_records = len(overSM_y_train[overSM_y_train==1])
    print(no_of_fraud_records)
    no_of_valid_records = len(overSM_y_train[overSM_y_train==0])
    print(no_of_valid_records)
