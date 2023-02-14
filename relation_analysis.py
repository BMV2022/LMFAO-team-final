# -*- coding: utf-8 -*-
"""relation_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bZ4sbuE-rHoDIbQOMkgyG88LQX7mmq4a
"""

#Using SEER-BreastCancer.csv for prediction and analysis
#LMFAO team

import numpy
import sklearn
import matplotlib 
import pandas as pd

dataset = pd.read_csv(/kai/liao/BIO/breast-cancer/Breast_Cancer.csv")

dataset.info()
dataset.describe() 
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,4))  
ax1 = ax[0]    # axisx
ax2 = ax[1]    # aixsy

sns.countplot(data=dataset, hue='Status', ax=ax1, x='Race',    ) 
#define x as race
sns.countplot(data=dataset, hue='Status', ax=ax2, x='Marital Status',)
#define x as marital status


fig, ax = plt.subplots(figsize=(6,4))
ax = sns.scatterplot(data=data, x='Regional Node Examined', y='Regional Node Positive', 
                     hue='Status', palette='Blues')

#Heatmap for relation-index between different feature labels
                     fig, ax = plt.subplots(figsize=(20,16))
sns.heatmap(dcorr, cmap='Blues', annot=True, fmt='.2f', linewidths=2, linecolor='white', square=True, ax=ax)

ax.tick_params(bottom=False, labelbottom=False, top=True, labeltop=True)
plt.setp(ax.get_xticklabels(), rotation= 60, ha="left")    

plt.show()

plt.show()



#lymph nodes and tumor size 
fig, ax = plt.subplots(figsize=(6,4))
ax = sns.scatterplot(data=data, x='Regional Node Examined', y='Regional Node Positive', 
                     hue='Status', palette='Blues')

plt.show()