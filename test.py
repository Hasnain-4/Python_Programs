# [-1,2,-3,4,5]

# lst = []

# num = int(input("Please Enter Array length : "))

# for i in range(num):
#     elem = int(input())
#     list_data = lst.append(elem)
# list_data = [1,2,6,3,9]
# new_list = list_data.sort()
# a=0
# for item in new_list:

#     # if item 
#     print(item)



# print(list_data)
# for j in list_data:
#     if j>0:
#         maxelem = max(j)
#         for k in range(maxelem):
#             if k in list_data:
#                 pass
#             else:
#                 print(min(k))

#     else:
        
#         print()
# # print(a)
# # for j in list_item:
    
#     print(j)


#'''''''''''''''''''''new Program''''''''''''

# n = int(input("Enter Number : "))

# if n%2 == 0:
#     for i in range(2,6):
        
#         if n==i:
#             print('Not Weird')
#     for j in range(6,21):
        
#         if n==j:
#             print('Weird')
#     if n>20:
#         print('Not Weird')
# else:
#     print('Weird')

#++++++++++++++++++++++++++++++++++++++++++++++++++++

# num = int(input('enter the number: '))

# a=0

# b=0

# for i in range(1,num+1):

#     if(i%2!=0):

#         a= a+7

#     else:

#         b = b+6

# if(num%2!=0):

#     print(' {} term of series is {}'.format(num,a-7))

# else:

#     print('{} term of series is {}'.format(num,b-6))

#+++++++++++++++++++++++str to int an vice-versa+++++++++++++++++++++++++++++

# def str_to_int(n):
#     print(int(n))
# def int_to_str(n):
#     print(str(n))

# str_to_int('4')
# int_to_str(4)

# inp = input("Enter Number Or Character: ")
# if inp == str:
#     str_to_int(inp)
# else:
#     int_to_str(inp)

# class Calculator:
#     def add(self,a,b):
#         # return a+b
#         print(a+b)
    
#     def div(self,a,b):
#         # return a-b
#         print(a-b)
    
#     def mul(self,a,b):
#         return a*b
    
#     def divide(self,a,b):
#         return a/b
    
# calculator = Calculator()

# calculator.add(2,3)
# calculator.div(4,3)
# calculator.mul(2,3)
# calculator.divide(4,2)

# --------------------------------------
# a=int(input('enter : '))
# d = [int(g) for g in range(a)]
# print(d)
# b = sum(d)
# print(b)

# --------------------------------------
# n=int(input('enter: '))
# n1=str(n)
# print(len(n1))
#===========================

# size=int(input("ENTER ARRAY SIZE"))

# arr=[]

# for i in range(size):

#     element=int(input('enter: '))

#     arr.append(element)

# print("SMALLEST ELEMENT",min(arr))
# =========================================================
# n = int(input('enter number : '))

# for i in range(n):
#     print((n-(i+1)) * ' ' + '*' *(i+1))

# ======================================================
# String = input('Enter the String : ')

# s = String[0].capitalize() + String[1:-1] + String[-1].capitalize()
# print(s)


from collections import Counter 
import requests
from bs4 import BeautifulSoup
  
source_code = requests.get("https://www.geeksforgeeks.org/programming-language-choose/").content 
# split() returns list of all the words in the string 
soup = BeautifulSoup(source_code, 'lxml').text
import re
# ask = re.sub(r'\band\b,\bto\b,\bin\b,','',soup) #delete one word from text
new_string = soup
characters_to_remove = ['to','and','in','of','or','is','on','which','Which','what','where','it','you','the','for','a','an','as']
for character in characters_to_remove:
  new_string = new_string.replace(character, "")
split_it = new_string.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(10) 
  
print(most_occur) 