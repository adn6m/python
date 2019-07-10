# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 19:29:41 2019

@author: adn6m
"""

# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))

print (p)



def functionpass(x):
    if x>=5 and x<=8:
        s = "abcdefghijklmnopqrstuvwxyz"
        t = "01234567890"
        u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        v = "!@#$%^&*()?"
        w = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        p =  "".join(random.sample(s,1))
        p1 = "".join(random.sample(t,2))
        p2 = "".join(random.sample(u,1))
        p3 = "".join(random.sample(v,1))
        p4 = "".join(random.sample(w,x-5))
        p5 = p+p1+p2+p3+p4
        p6 = random.sample(p5,x)
        print (p6)
    else:
        print("Run the function with an argument/password length of 5-8 char.")
        
functionpass(6)
