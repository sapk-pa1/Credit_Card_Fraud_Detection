import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings 

warnings.filterwarnings('ignore')
#ignoreing all the futture warnings 

def visualize_data(sample_data):
    #bar plot for the valid and the fraud cases 
    transactions = pd.value_counts(sample_data['Class'], sort = True)
    transactions.plot(kind = 'bar', color = 'g')
    plt.title("Valid and Fraud Transactions")
    plt.xlabel("Class")
    plt.ylabel("No of Transactions")
    Labels = ["Valid", "Fraud"]
    plt.xticks(range(2), Labels)
    ## Keeping the text in the bar plot 
    for i in range(len(Labels)):
        plt.text(i,transactions[i],str(transactions[i]), ha = 'center', va = 'bottom', color = 'black')
    plt.show()