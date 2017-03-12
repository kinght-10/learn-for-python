# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 16:34:26 2017

@author: ycb
"""

import numpy as np
import pandas as pd
data=pd.DataFrame({'A':[1,3],
                  'B':[2,4]})
print(data)

#for i in data.columns:
#    print data[i].sum(0)

sum1=0
i=0
while i<2:
    sum1=sum1+data.iloc[i,:].sum()
#print(data.iloc[1,:].sum())
    i=i+1
   
print(sum1)
print(data.iloc[:,1].sum())
#print(sum(data.iloc[0,:]))
#print (sum(data.iloc[0,:]))
#i=1
#sum_1=0
#while i<3:
#    sum_1=sum_1+sum(data.iloc[i,1])
#    i=i+1
    

#print(data.sum(axis=1))