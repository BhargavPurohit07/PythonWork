s1= input("enter s1:-")
s2= input("enter s2:-")


s2len = len(s2)
s1len = len(s1)

if(s2len<s1len):
    for i in range(len(s1)-(s2len-1)):
            if(s1[i:i+s2len]==s2):
                         print("string match at:-",i)
else:
    for i in range(len(s2)-(s1len-1)):
            if(s1[i:i+s1len]==s1):
                print("string match at:-",i)
