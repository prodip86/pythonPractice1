#!/usr/bin/env python
# coding: utf-8

# ## Start Python 11 Dec 2023
# 

# if 5<8:
#     print("eight greater than five")

# In[1]:


#commenting for single line
"""
this is multiple commenting system

"""
print("this is comment")


# ## Variables

# In[2]:


x=5              # this is an int
y="Prodip"       # this is a str
print(x)
print(y)


# In[3]:


# How to casting 

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)


# In[4]:


#how to get variable type by type() function
print(type(x))


# In[5]:


a=4
A='PKD'
print(a)
print(A)


# ### Variable labeling

# In[6]:


#Camel case
myVariable = 5

#Pascal
MyVariable = 5

#snake 
my_variable = 5


# In[7]:


#Many values to multiple variable
a, b, c = 11, 22, 33

print(a)
print(b)
print(c)

#One Value to Multiple Variables
a=b=c='prodip'
print(b)


# In[8]:


#Unpack a list
fruits = ['apple', 'banana', 'lemon']
x, y, z = fruits
print(x)
print(y)
print(z)


# In[9]:


#Output Variables

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)    #use + sign 
print(x +' '+ y+' '+ z)


# In[10]:


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# In[11]:


print("Python is " + x)


# ### Data Type
# 

# In[12]:


x = ["apple", "banana", "cherry"] #	list	

x = ("apple", "banana", "cherry") #	tuple	

x = range(6)                      #	range	

x = {"name" : "John", "age" : 36} #dict	

x = {"apple", "banana", "cherry"} #set

x = frozenset({"apple", "banana", "cherry"}) #frozenset


# In[13]:


import random

print(random.randrange(1, 10))


# In[14]:


x = 5
y= x % 3        # x%3 Reminders/Bhagshes
print(y)
z = x //3       # x//=3 Resutls/Bhagfol
print(z)
x |= 3


# ### List
# 

# In[15]:


myList = ['honda', 'yahama', 'sizuki']
print(myList[-1])


# In[16]:


#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-7:])       
print(thislist[:-2])
print(thislist[:2])
print(thislist[2:])
print(thislist[-4:-1])    


# In[17]:


nameList = ['PKD', 'Raju', 'Sujan']
if 'Raju' in nameList:
    print('Yes, Raju is in the list')


# In[18]:


#Change List Items

nameList = ['PKD', 'Raju', 'Sujan']
nameList[1] = 'Sajib'
print(nameList)


# In[19]:


#If you insert less items than you replace, the new items will be inserted where you specified,
#and the remaining items will move accordingly

nameList = ['PKD', 'Raju', 'Sujan']
nameList[1:2] = ['Sajib','Mamu']
print(nameList)
nameList[1:4] = ['Sajib','Mamu']
print(nameList)


# In[20]:


#insertation 
nameList = ['PKD', 'Raju', 'Sujan']
nameList.insert(2,'Madhu')
print(nameList)

#Append Items end of the list  #
nameList = ['PKD', 'Raju', 'Sujan']
nameList.append('Madhu')
print(nameList)


# In[21]:


#To add another list in a existing list the use extend

nameList = ['PKD', 'Raju', 'Sujan']
fruits = ["mango", "pineapple", "papaya"]
nameList.extend(fruits)
print(nameList)


# In[22]:


#Remove Items from the list
#pop() from any specific index

nameList = ['PKD', 'Raju', 'Sujan']
nameList.remove('PKD')
print(nameList)


# In[23]:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


# In[24]:


myDic = {
    'Name' : 'pkd',
    'Age' : 37,
    'occu' : 'service'
}
print(myDic)


# In[25]:


# importing panda and numpay libraries
import pandas as pd 
import numpy as np


# In[26]:


exp=np.random.normal(250,150,10000)


# In[27]:


exp


# In[28]:


len(exp)


# In[29]:


## plotting the randomly generated exp
#import seaborn as sns
#sns.distplot(exp)
# or sns.histplot(exp)
## plotting the randomlh genereted exp

import seaborn as sb
sb.distplot(exp)
sb.histplot(exp)


# In[30]:


#calcualte mean
np.mean(exp)


# In[31]:


np.median(exp)


# In[32]:


exp1=np.append(exp,[3000])


# In[33]:


exp1


# In[34]:


sb.histplot(exp1)


# In[35]:


# generates 200random integer nyumbers between 15-50
#exp=np.random.randint(15,50,200) #(start,stop,num of values)
exp2=np.random.randint(20,30,5000)


# In[36]:


len(exp2)


# In[37]:


exp2


# In[38]:


sb.histplot(exp2)
sb.distplot(exp2)


# In[39]:


from scipy import stats


# In[40]:


stats.mode(exp2)


# In[41]:


## calculating IQR

data=[346,47,56,2,36,39,75,79,79,88,89,91,92,93,96,97,101,105,112,115]


# In[42]:


IQR=stats.iqr(data,interpolation='midpoint')


# In[43]:


IQR


# In[44]:


# Sample Data 
arr = [1, 2, 3, 4, 5]

#Finding Max 
Maximum = max(arr)
# Finding Min 
Minimum = min(arr) 

# Difference Of Max and Min
Range = Maximum-Minimum
#print("Maximum = {}, Minimum = {} and Range = {}".format(Minimum, Maximum,  Range))
print('maximun={}, minimum = {}, range = {}'.format(Maximum,Minimum,Range))


# In[45]:


#User input to Number
a=input(int('enter number: '))


# In[ ]:


int_text = input("Give me an integer number: ")
int_num = int(int_text)
float_text = input("Give me a float  number: ")
float_num = float(float_text)
result = int_num * float_num
print("Your result is: ", result)


# In[ ]:


# Write a Python program to print "Hello, World!
text='Hello World'

print(text2)


# In[ ]:


# Calculate the sum of two numbers entered by the user
num1=int(input('enter your 1st no.: '))
num2=int(input('enter your 2nd no.: '))
add=num1+num2
#print('The sum of {} and {} is {}'.format(num1, num2,add))
#print('sum of two number is', add)
#print('the sum of two numner is', num1+num2)
#add


# In[ ]:


# Convert temperature from Celsius to Fahrenheit
ctemp=int(input('Enter tempature in celsius:' ))
ftemp= ctemp*(9/5)+32       #calculation 1
ftemp = (ctemp*(5/9))+32    #calculation 2 
print('Convert temperature from {} Celsius to Fahrenheit is {}'.format(ctemp, ftemp))


# In[ ]:


# Create a program that takes a user's name and age as input and prints a greeting message
name=input('Enter your Name: ')
age=int(input('Enter your age: '))
#print('Hello, My name is {} and I am {} years old'.format(name, age))

print(f'"Hello, My name is {name} and I am {age} years old')

#print(f'"{input_string}" is a palindrome.')


# In[ ]:


# find out minimum number
a = []
size = int(input('Enter array size: '))

for i in range(size):
    val = int(input('Enter array values: '))
    a.append(val)

min_value = a[0]

for i in range(size):
    if a[i] < min_value:
        min_value = a[i]

print('Minimum number:', min_value)


# In[ ]:


a = [3,6,1,-4,5,8]

min_value = a[0]

for i in range(size):
    if a[i] < min_value:
        min_value = a[i]

print('Minimum number:', min_value)


# In[ ]:


a = [3,77,1,5,80]

min_value = a[0]

for i in range(size):
    if a[i] > min_value:
        min_value = a[i]

print('Max number:', min_value)


# In[ ]:


# Given a list of numbers, find the maximum and minimum values
List = [90, -1, 10, 24, 78, 34, 56, 70, 26, 0]
count = max = min = 0  #Variable Initialization

for i in List:         #Loop through the List:
    count += 1
    if count == 1:
        max = min = i
    else:
        if i > max:
            max = i
        if i < min:
            min = i

print("Maximum number from this list is", max)
print("Minimum number from this list is", min)


# In[ ]:


# Create a Python function to check if a given string is a palindrome
text = input("the text is inputed here" )
if (text==text[::-1]):
    
    print(text,'the text is palindrome')
    
else:
    print('the text {} is not palindrome'.format(text))       


# In[ ]:


def is_palindrome(input_str):
    
    cleaned_str = input_str.replace(" ", "").lower() # Remove spaces and convert to lowercase for case-insensitive comparison
    
    return cleaned_str == cleaned_str[::-1]          # Check if the cleaned string is equal to its reverse

# Example usage:
input_string = "A man a plan a canal Panama"
result = is_palindrome(input_string)

if result:
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')


# In[ ]:


def is_palindrom(text):
    clear_text = text.replace(" ", "").upper()
    return clear_text == clear_text[::-1]


text = input("Write the palindrom name: ")

if is_palindrom(text):
    print("Palindrom")
else:
    print("not Palindrom")


# In[ ]:


# Create a Python function to check if a given string is a palindrome

def is_palindrome(text):
   # clear_text = text.replace(" ", "").lower()
    return text == text[::-1]

text = input("Write the palindrome name: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")


# In[1]:


pip install jupyter_contrib_nbextensions


# In[ ]:


pip install yapf


# In[46]:


jupyter nbextension enable
code_prettify/code_prettify


# In[2]:


pip install jupyter_contrib_nbextensions


# In[3]:


pip install yapf


# In[4]:


days = int(input("Enter the day you want to convert: "))
year = days//365
#month = (days%365)//12
month = days//30
day = (days%365)%12

print(days,"is",year,"year",month,"months",day,"days")


# In[9]:


text = input("Enter a message: ")

#words_List = text.replace(" ","") # use of charecter counting 
words_List = text.split(" ")       # use for word counting

#print("number of words are:",len(words_List))
print("number of words are:",len(words_List))


# In[15]:


list, sum1 =[-10,10,0,4,-1,-3,-3,24,2],0
i=0
for i in sum1:
    if i>0:
        sum1 += i
        print("sums of the positive number is:", sum1)


# In[11]:


num1 =[-10,10,0,4,-1,-3,-3,24,2]
if (num1 > 0):
    num1 += i
    print('sumation is ', num1)


# In[16]:


sum = [-10,10,0,4,-1,-3,-3,24,2]
List = 0
for i in List:
    if i>0:
        sum += i
        print("sum of the positive number is:",sum)


# In[28]:


# Given list of integers
my_list = [10, 10, 0, -4, -1, -3, -3, 24, 2]

# Initialize a variable to store the sum
sum_var = 0

# Iterate through the list and add each element to the sum
for num in my_list:
       
    sum_var += num

# Print the final sum
print("Sum of all numbers in the list:", sum_var)


# In[34]:


# Create a list of fruits and access elements using indexing
fruits = ['apple', 'banana', 'lici', 'tomato']
index_num = int(input('Enter index number ofr accessing the fruits:'  ))
print('index is' {index_num} 'and fruit name is' {fruits['index_num']})


# In[36]:


flist = ['apple', 'banana', 'lici', 'tomato']
index = int(input("number of f:" ))
print(flist[index])


# In[39]:


m_list = [10, 10, 24, 2]


# In[44]:


num = [10, 10, 24, 2]
sum = 0
for num in list:
    list += num
    print('sum of ', sum)


# In[48]:


num = [10, 10, 24, 2]
sum = 0
average = 0.0
for i in num:
    sum += i
print(sum)
print('average is', sum/len(num))


# In[ ]:


#write a program in reverse word

def rev(s):
    rev[] = rev[::-1]
    retun 

