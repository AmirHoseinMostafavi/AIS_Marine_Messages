from cmath import sin
from tkinter.filedialog import SaveAs
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from import_DB import importDataFromDB

class AIS_DBscan:

    def __init__(self,df) -> None:
        
        self.df = df = importDataFromDB()
        pass
    
    
# Describe Database...................................................
    def Describe_DB(df):
        print(df.head(),end='\n')
        print(df.describe(),end='\n')
        print(df.info(),end='\n')
        print(type(df),end='\n')

    
# Plot .......................01.....................................
    def Plots(df):    
        ax1 = sns.pairplot(df)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Test')

        plt.savefig('ax1.png',dpi = 150)
        plt.close()

# Plot .......................02......................................
    def Plots_Heatmap(df): 
        df=df.drop(['CustomerID'],axis=1)
# print(df.head())
        sns.heatmap(df.corr())
        plt.savefig('ax2.png',dpi = 150)
        plt.close()

# Plot .......................03......................................
    def Plots_Pie(df): 
        plt.figure(figsize=(7,7))
        size=df['Gender'].value_counts()
        label=['Female','Male']
        color=['Pink','Blue']
        explode=[0,0.1]
        plt.pie(size,explode=explode,labels=label,colors=color,shadow=True)
        plt.legend()
        plt.savefig('ax3.png',dpi = 150)
        plt.close()

# Plot .......................04......................................

    def Plots_Countplot(df):
        plt.figure(figsize=(10,5))
        sns.countplot(df['Age'])
        plt.xticks(rotation=90)
        plt.savefig('ax4.png',dpi = 150)
        plt.close()

# Plot .......................05......................................
    def Plots_Boxplot(df):
        sns.boxplot(df['Gender'],df['SpendScore'])
        plt.savefig('ax5.png',dpi = 150)
        plt.close()

# Plot .......................06......................................
    def Plots_Bar(df):
        plt.bar(df['Income'],df['SpendScore'])
        plt.title('Spendscore over income',fontsize=20)
        plt.xlabel('Income')
        plt.ylabel('Spendscore')
        plt.savefig('ax5.png',dpi = 150)
        plt.close()