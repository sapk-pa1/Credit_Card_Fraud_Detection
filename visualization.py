import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings 

warnings.filterwarnings('ignore')
#ignoreing all the futture warnings 

def visualize_data(data_needed_for_viz):
    sample_data, valid, fraud, v_features = data_needed_for_viz
    #bar plot for the valid and the fraud cases 
    x = ["Valid", "Fraud"]
    y = [valid.shape[0], fraud.shape[0]]
    fig, ax = plt.subplots()
    plt.yticks([0,500000,1000000,4000000,5000000])
    ax.bar(x, y, color = ('green', 'red'))
    ax.set(title= "Credit Card Transaction Types", ylabel = "No of Transactions")

    #Text rakheko ho tyo plot ko top ma 
    for i in range(len(x)):
        plt.text(i,y[i],str(y[i]), ha= "center", va= 'bottom', color ='black' )
    plt.show()
    fig, ax = plt.subplots(1, 2, figsize=(18,4))