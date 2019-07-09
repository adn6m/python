# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:38:49 2019

@author: adn6m
"""


import numpy as np

# 1 

#Create a function to calculate the absolute value of a number without using the abs() function to calculate the absolute value for -9 and 7.2

def my_function4(a=7.2):
    if a<0: 
        return(a*-1)
    else:
        return(a)
        
my_function4()

x = lambda a: np.sqrt(a*a)
print(x(7.2))




# 2

# for the given data (20,30,40,50,100), create a function to calcuate the total/3 
#note that all the calcualtions have to be done within the function
def any(*args):
  total = 0
  for i in args:
    total += i
  return total/3

# Calculate the sum  
any(20,30,40,50,100)

## 3
#create a function to work in range(43,60) such that if the number is <50, it prints out "LT_50" else it should print out (number+3)
def mycoolfunct(number):
    for number in range(43,60):
        if number <50:
            print("LT_50")
        else:
            print(number + 3)
        
mycoolfunct(44)

#4

# create a functio which takes 2 inputs as num and x and do the following
#if num>=0 then calcuate num*x else num*x/2

def mycoolfunct2(num,x):
    if num>=0:
        return(num*x)
    else:
        return(num*x/2)
        
mycoolfunct2(-1,2)

#5 create a function to create a new list with only the nos which can be divided by 3 from the following list

li = [5, 7, 21, 99, 51, 62, 77, 27, 73, 61] 
final_list = list(filter(lambda x: (x%3 == 0) , li)) 
print(final_list)  

# 6

#create a function using lambda function to overwrite the following list with all the elements squared

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*x , li)) 
print(final_list) 