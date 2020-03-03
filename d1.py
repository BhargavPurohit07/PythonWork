# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 13:31:46 2020

@author: bharg
"""

s1 = "aabhjklmbhj"
s2=[]

l=0
g=2
i=0
d=0
def mat(a):
    
    f=1
    global g,l,d
    while(a <= len(s1)):
        
        for i in range(len(s1)-(a-1)):
            
            if(l>0):
                print(s1[l:a]," = ",s1[i:(i+a)-g])
                d=d+1;
                s2.append(s1[i:i+a])
                if(s1[l:a]==s1[i:i+a]):
                    if(f==1):
                        f+=1
                        continue
                    print("match")
                    continue
            
            elif(s1[l:a]==s1[i:i+a]):
                if(f==1):
                    f+=1
                    continue
                print("match")
                continue
            
                
        a=a+1
        f=1
        
    if(g<=(len(s1)/2)):
        l=l+1
        d=0
        i=0
        g=g+1
        mat(g)
    

                
mat(g)
    

for l in range(len(s2)):
    for w in range(len(s1)):
        print(s2[l]," = ",s1[w])
        