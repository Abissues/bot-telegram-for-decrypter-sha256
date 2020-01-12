import random
import os
catto=0
while 1:
    catto=catto+1
    print(catto)
    passlen = 1
    data="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm@#1234567890"
    p =  "".join(random.sample(data,passlen ))
    leggi=open("password.txt",'r')
    l=leggi.readlines()
    if p in l:
        a=open("aumento.txt","r")
        n=a.readline()
        n=int(n)
        n=n+1
        a.close()
        a=open("aumento.txt","w")
        a.write(str(n))
        a.close()       
        a=open("aumento.txt","r")
        n=a.readline()
        n=int(n)
        if n>100:
            n=n*0
            passlen+=1
            a.close()
            a=open("aumento.txt","w")
            a.write(str(n))
            a.close()
        leggi.close()
    else:
        x=open("password.txt",'a')
        xa=x.write(p+'\n')
        x.close()
        
