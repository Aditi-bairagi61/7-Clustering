# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 08:33:26 2024

@author: Admin
"""

##################################################################################
''' Scatter Plot '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#let us try to understand first how k means works for the two
#dimentional data
#for that, generte the random numbers in the range 0 to 1
#and with uniform probability of 1/50
X=np.random.uniform(0,1,50)
Y=np.random.uniform(0,1,50)
#create a empty dataframe with 0 rows and 2 columns
df_xy=pd.DataFrame(columns=["X","Y"])
#assign the values of X and Y to there columns
df_xy.X=X
df_xy.Y=Y
df_xy.plot(x="X",y="Y",kind="scatter")
model1=KMeans(n_clusters =3).fit(df_xy)

'''
with data X and Y , apply kmeans model,
generate scatter plot
with scale/font=10
cmap=plt.cm.coolwarm:cool color combination
'''
model1.labels_
df_xy.plot(x="X",y="Y",c=model1.labels_,kind="scatter",s=10,cmap=plt.cm.coolwarm)

##########################################################
Univ1=pd.read_excel("C:/7-Clustering/University_Clustering.xlsx")
Univ1.describe()
Univ=Univ1.drop(["State"],axis=1)
#we know that there is scale difference among the columns ,which we
#either by using normalizatiom or stamardization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now apply this normalization function to Univ dataframe for all the 

df_norm=norm_func(Univ.iloc[:,1:])

'''
What will be ideal cluster number,will it be 1,2, or 3
'''

TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans =KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    
    TWSS.append(kmeans.inertia_)#total within sum of square
'''
KMeans inertia, also known as Sumof Squares Errors
(or SEE), calcualtes the sum of distances of all the 
points.It is the difeerence between tjhe observed
value and the predicted value.
'''

TWSS
#As kvalue increases the TWSS value decreses
plt.plot(k,TWSS,'ro-');
plt.xlabel('No_of_clusters');
plt.ylabel('Total_within_SS')

'''
How to select value of k from elbow curve 
When k changes from 2 to 3 ,then decreses
in twss is higher than
When k changes from 3 to 4.
When k values changes from 5 to 6 decreses
'''
model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
Univ['clust']=mb
Univ.head()
Univ=Univ.iloc[:,[7,0,1,2,3,4,5,6]]
Univ
Univ.iloc[:,2:8].groupby(Univ.clust).mean()

Univ.to_csv("kmeans_University.csv",encoding="utf-8")
import os
os.getcwd()

################################################################################
'''Problem Statment : -
Peform clustering


Business Objectives :-
Identify Crime Patterns: Group states with similar crime profiles
 (e.g., high murder rates and low urban population) to understand different
 crime patterns across the country. This can help in deploying targeted crime
 prevention strategies.
Resource Allocation: By clustering states with similar crime statistics,
 policymakers can better allocate resources such as law enforcement or 
 community programs to regions that exhibit similar crime profiles.
 
 1. Enhanced Decision-Making
Targeted Interventions: Clustering helps identify areas with similar
 crime profiles, allowing for tailored interventions that are more likely to succeed.
Resource Optimization: By understanding the specific needs of each cluster, 
resources can be allocated more efficiently, ensuring that high-risk areas receive the attention they need.

2. Improved Policy Formulation
Data-Driven Strategies: Policymakers can use insights from clustering 
to develop evidence-based policies that address the unique challenges of 
different regions.
Benchmarking: States can benchmark against others in their cluster to 
understand relative performance and identify best practices.
'''

#Data Description
#Data Description
#Murder -- Murder rates inn 
























