# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:01:07 2020

@author: bharg
"""

s1 = "manav"
s2=[]
s3=[]
#a=3
#for i in range(0,len(s1)-(a-1),a):
#    s2.append(s1[i:i+a])
#
#print(s2)
#        

k=2
j=1
a=2
g=1
t=1
while(j!=len(s1)-1):
    for i in range(0,len(s1),k):
        s2.append(s1[i:i+k])
    
    
    for e in range(len(s1)-(a-1)):
#            print(s1[e:e+a]," = ",s2)
            for g in range(len(s2)):
#                print(s1[e:e+a]," = ",s2[g])
                if(s1[e:e+a]==s2[g]):
                    if(t==1):
                        t=t+1
                        continue
                    print("match")
                    s3.append(s2[g])
            
    a=a+1
    k=k+1
    j=j+1
    t=t-1


print(s3)
