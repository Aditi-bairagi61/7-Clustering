# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:31:20 2024

@author: Admin
"""

import pandas as pd
import matplotlib .pyplot as plt
#now import file from dataset and create a dataset
Univ1 = pd.read_excel("C:/7-Clustering/University_Clustering.xlsx")

a=Univ1.describe()
#we have one column "State" which really not useful we will drop it
#5 number summary is applicable only for the collitative data
Univ1.columns
#we have one coluns "state which really not useful so we will drop "state" column
Univ=Univ1.drop(["State"],axis=1) 
Univ
#we know thate there is a scale difference among the columns,
#either by using normalization or standardlization 
#whenever their is mixed data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now apply this normalization function to Univ dataframe 
#for all the rowa and column from until end
#since 0th colun has university name hence skipped
df_norm=norm_func(Univ.iloc[:,1:])
df_norm
#you can check the df_norm dataframe which is scaled 
#betwwen values from 0 to 1
#you can apply describe function to new data frame
b=df_norm.describe()
b

#before you apply clustering you need to plot dendrogram first
#nowS to create dendrogram we need to measure distence,
#we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierarchical or algorative clustering
#ref the help for linkage


z=linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15,8));
plt.title("Hierarchical Clustering dendogram");
plt.xlabel("Index");
plt.ylabel("Distance")
#ref help of dendogram
#sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#Dendrogram
#applying agglomerative clustering choosing 3 as clusters from dendrogram
#whatever has been displyed in dendrogram is no clustering
#it is just showing number of possible clustering

from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters=3,linkage='complete',metric='euclidean').fit(df_norm)

'''Afinity has been depticited,use mertric='euclidean' , instrad affinity = 'euclidean' 
'''
#apply labels to the clusters
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#assign this series to Univ DataFrame as Column and name the columns as "clust"
Univ['clust']=cluster_labels
#we want to relocate the column 7 to 0th position
Univ1=Univ.iloc[:,[7,1,2,3,4,5,6]]
#now check the Univ1 dataframe
Univ1.iloc[:,2:].groupby(Univ.clust).mean()
#from the output cluster 2 has got highest Top10


#lowest accepts ratio,best facilty ratio and highest expenses
#highest graduates ratio
Univ1.to_csv("University.csv",encoding="utf-8")
import os 
os.getcwd()
