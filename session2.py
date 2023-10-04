# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:00:30 2023

@author: Acer
"""
from math import * # * import for all functions in this library


r= 15 %2
print(r)
x= 7 ** 2 # 7^2

print(x)


y= 7 **3 

print(y) # 7^3

########################

x=7

print(type(x))

myfloat= float(x)

print(type(myfloat))

newvar= str(x) # "7" transform integer into string

print(newvar)
print(type(newvar))

####################################

num = -5

print(abs(-5)) # absolute value

print(pow(7, 2)) # power(number, (2,3,4...ect)

print(min(3,4)) #minimum

print(max(10, 222))

print(sqrt(9))


x= 7
y=8

print("x= " + str(x)) # concatenate x= 7

# concatenation 


print("x="+ " " + str(x)) # concatenate x= 7



#############################################33


print("hello \npython") # to return to a new line

# \t = 4 spaces

text= "PYThon is my favorite programming language"


# .lower --> small letter
#upper ---> capital letter


print(text.lower()) 
#text=text.lower()

print(text) #text remain the same
print(text.upper())

text= text.upper()

print(text.isupper())

print(text.islower())

print(text.lower().islower()) #in the same line

print(text.lower().isupper())

#####################################
print(len(text))


text= "PYThon is my favorite programming language"

print(text[6])

print(text[-1])

print(text[len(text)-1])


print(5+3)

var="python"

print(var + "is " + "easy" + "!" + " 5")





















