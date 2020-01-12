import random
import os
while 1:
    s = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm@#"
    ary=open("arrivo.txt","r")
    l=ary.readline()
    l=int(l)
    ary.close()
    passlen = l
    p =  "".join(random.sample(s,passlen ))
    with open('password.txt') as file:
        contents = file.read()
        search_word = p
        if search_word in contents:
            print ('parola trovata non aggiungo nulla')
            p=open("aumento.txt","r")
            s=p.readline()
            s=int(s)
            p.close()
            if s==100:
                p=open("aumento.txt","w")
                p.write('0')
                p.close()
                parte=open("arrivo.txt","r")
                s=parte.readline()
                s=int(s)
                parte.close()
                h=open("arrivo.txt","w")
                s+=1
                f=h.write(str(s))
                h.close()
            p=open("aumento.txt","w")
            s=s+1
            p.write(str(s))
            p.close()

        else:
            testate = open('password.txt', 'a')
            testate.write(p + '\n')
            print("parola aggiunta")
