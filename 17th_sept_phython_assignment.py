#!/usr/bin/env python
# coding: utf-8

# # For loop

# In[1]:


#1
for i in range(1,11):
    print(i)


# In[6]:


#3
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)


# In[50]:


#4
list=[1,2,3,4,5,6,7,8]
for i in list:
    print(i)


# In[7]:


#5
list=[3,4,60,7,9,11]
multiple=1
for i in list:
    multiple=multiple*i
print(multiple)
    


# In[56]:


#6
for i in range(2,21,2):
    print(i)
    
  


# In[30]:


#7
a=int(input("enter any number = "))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
print(factorial)
    


# In[51]:


#8
a="Pwskills"
b=[]
for i in a:
    b.append(i)
print(b)


# In[64]:


#9
list=[2,3,4,5,6,7,54]
largest=0

for i in list:
    if i>largest:
        largest=i
print(largest)
    
    


# In[76]:


#10
a=int(input("enter the limit = "))
m=0
n=1
for i in range(1,a+1):
    print(m)
    m,n=n,m+n
    
    


# In[78]:


#11
a=input("enter the string = ")
b=a.lower()
vowels='a,e,o,u,i'
count=0
for i in b:
    if i in vowels:
        count+=1
print(count)


# In[80]:


#12
a=int(input("enter the number whose multiple table is "))
for i in range(1,11):
    print(a,'x',i,'=',a*i)


# In[93]:


#13
a=[1,2,3,4,5,6,7]
b=[]
for i in a[::-1]:
    b.append(i)
print(b)
    


# In[103]:


#14
a=[1,2,3,4,5]
b=[4,5,6,7,8]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)


# In[115]:


#15
a={'company':'apple','processor':'ios','mobile_name':'iphone'}
for i,j in a.items():
    print("keys:",i)
    print("values:",j)
    print(" ")


# In[123]:


#16
a=int(input("enter the number = "))
b=int(input("enter the number = "))
gcd=1
for i in range(1,min(a,b)):
    if a%i==0 and b%i==0:
        gcd=i
print("gcd of number is: ",gcd)


# In[5]:


#18
list=[1,22,3,4,3,5,4,6,5,7,6,77,88,77]
my_lst=[]
for i in list:
    if i not in my_lst:
        my_lst.append(i)
print(my_lst)


# In[12]:


#19
a=input("enter the sentence : ")
count=0
for i in a:
    count+=1
    
print(count)


# In[15]:


#20
sum=0
for i in range(1,51):
    if i%2!=0:
        sum=sum+i
print(sum)


# In[32]:


#21
a=int(input("enter the year = "))
if a%4==0 and a%100!=0:
    print(a)
            
        


# In[35]:


#22
a=int(input("enter the number = "))
for i in a:
    i=a**0.5
    print(i)


# In[42]:


#23
a=int(input('enter the number = '))
b=int(input('enter the number = '))
max_num=max(a,b)
for lcm in range(max_num,a*b+1,max_num):
    if lcm%a==0 and lcm%b==0:
        print(lcm)


# # if else

# In[46]:


#1
num=int(input("enter the number = "))
if num<0:
    print("num is negative")
elif num==0:
    print("num is zero")
else:
    print("num is positive")
    


# In[49]:


#3
num=int(input("enter the number = "))
if num%2==0:
    print("num is even ")
else:
    print("num is odd")


# In[52]:


#4
a=int(input("enter the number = "))
b=int(input("enter the number = "))
c=int(input("enter the number = "))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)


# In[55]:


#5
a=float(input("enter any number = "))
if a<0:
    a=-a
    print(a)
else:
    print(a)


# In[58]:


#6
a=input("enter the character = ")
c=a.lower()
b='aeoui'
if c in b:
    print("given character is a vowel")
else:
    print("given character is a consonant")


# In[60]:


#7
a=int(input("enter the age = "))
if a>=18:
    print("person is eligible to vote")
else:
    print("person is not eligible to vote")


# In[63]:


#9
a=int(input("enter the number = "))
if a in range(1,11):
    print("number is in specific range")
else:
    print('number is not in specific range')


# In[4]:


#10
a=int(input('enter the marks of student = '))
if a>90:
    print("student secured grade A")
elif 75<a<=90:
    print("student secured grade B")
elif 50<a<=75:
    print("student secured grade C")
else:
    print("student secured grade D")


# In[6]:


#11
a=input("enter the string : ")
if not a:
    print("string is empty")
else:
    print("string is not empty")


# In[24]:


#12
a=int(input("enter first side = "))
b=int(input("enter second side = "))
c=int(input("enter third side = "))
if a==b==c:
    print('this is an equilateral triangle')
elif a==b!=c or a!=b==c or a==c!=b:
    print("this is an isoceles triangle")
else:
    print("this is a scalar triangle")


# In[9]:


#13
a=int(input("enter the number from 1-7 : "))
if a==1:
    print("sunday")
elif a==2:
    print("monday")
elif a==3:
    print("tuesday")
elif a==4:
    print("wednesday")
elif a==5:
    print("thursday")
elif a==6:
    print("friday")
elif a==7:
    print("saturday")
else:
    print("invalid input")


# In[11]:


#14
def leap_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False
year=int(input("enter the year = "))
if leap_year(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


# In[40]:


#15
a=9
if a<0:
    print("no")
else:
    assert a>0
    print("yes")


# In[16]:


#16
age=int(input("enter the age "))
if age >=60:
    print("a person is eligible for a senior citizen discount")
else:
    print("a person is not eligible for a senior citizen discount")


# In[11]:


#17
a=input("enter the character = ")
if a.isupper():
    print("uppercase character")
elif a.islower():
    print("lowercase character")
else:
    print("neither")


# In[11]:


#18
a=float(input("enter the number = "))
b=float(input("enter the number = "))
c=float(input("enter the number = "))
dis=b**2-4*a*c
if dis>0:
    r1=(-b + dis**0.5)/2*a
    r2=(-b - dis**0.5)/2*a
    print("roots are real & distinct ",r1,r2)
elif dis==0:
    r1=r2=(-b)/(2*a)
    print("roots are equal",r1)
else:
    r1= -b/(2*a)
    r2=(-dis**0.5)/(2*a)
    print("roots are complex ",r1,r2)


# In[15]:


#19
a=int(input("enter the year "))
if a%100==0:
    print(a," is a century year")
else:
    print(a," is not a century year")


# In[1]:


#20
a=int(input("enter the number = "))
if a<1:
    perfect_square=False
else:
   square_root=int(a**0.5)
   perfect_square=square_root**2==a
if perfect_square:
    print(a,"is a perfect square")
else:
    print(a,"is not a perfect square")


# In[24]:


#22
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal Weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {bmi:.2f}. You are categorized as '{category}'.")


# In[15]:


#24
a=int(input("enter the number = "))
if a<=1:
    print(a," is not prime number")
elif a==2:
    print(a," is a prime number")
else:
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            print(a,"is not a prime number")
            break
        else:
            print(a," is a prime number")


# # Map:-

# In[3]:


#2
a=[1,2,3,4,5,6]
square=list(map(lambda x:x**2,a))
print(square)


# In[19]:


#4
a=['yes','no','true','false']
upper=list(map(str.upper,a))
print(upper)


# In[23]:


#5
a=['month','year','days','time']
length=list(map(len,a))
print(length)


# In[33]:


#6
a=[1,2,3,4,5]
b=[10,9,8,7,6]
def custom_func(x,y):
    return x-y
custom_list=list(map(custom_func,a,b))
print(custom_list)


# In[28]:


#7
a=[99,100,101,102,103]
def celsius_into_fahren(celsius):
    return (celsius*9/5)+32
fahrenheit=list(map(celsius_into_fahren,a))
print(fahrenheit)
    


# In[29]:


#8
a=[1.5,2.34,53.45,678.5]
round_off=list(map(round,a))
print(round_off)


# # Reduce

# In[5]:


#2
from functools import reduce
a=[1,2,3,4,5]
def product(x,y):
    return x*y
result=reduce(product,a)
print(result)


# In[9]:


#3
from functools import reduce
a=[3,45,56,432,1,4,5]
def max_num(x,y):
    return x if x > y else y
maximum=reduce(max_num,a)
print("the maximum number is : ",maximum)


# In[13]:


#4
from functools import reduce
a=['i',' ','live',' ','in',' ','punjab']
def string(x,y):
    return x+y
single_str=reduce(string,a)
print(single_str)


# In[26]:


#5
from functools import reduce
a=9
def factorial(x,y):
    return x * y
b=list(range(1,a+1))
c=reduce(factorial,b)
print(c)


# In[29]:


#6
from functools import reduce
a=[4,6,8,12]
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
b=reduce(gcd,a)
print(b)


# In[35]:


#7
from functools import reduce
a=int(input("enter the number = "))
def product(x,y):
    return int(x)+int(y)
b=str(abs(a))
c=reduce(product,b)
print(c)


# # Filter

# In[1]:


#2
a=[2,3,5,6,7,8,9,10]
b=list(filter(lambda x:x%2==0,a))
print(b)


# In[10]:


#3
a=['data science','da','dsa','java','c++','data master']
specific_word="d"
b=list(filter(lambda x:x.startswith(specific_word),a))
print(b)


# In[5]:


#4
a=[1,2,3,4,5,6,7,8,9,0,11,2,13,17]
b=list(filter(lambda x:all(x % i !=0 for i in range(2,x)),a))
print(b)


# In[39]:


#5
a=[1,None,2,None,3,None,4,None]
filter_list=list(filter(lambda x:x is not None,a))
print(filter_list)


# In[43]:


#6
a=['i','am','learing','data science','from','pwskills']
minimum_len = 4
b=list(filter(lambda word: len(word) > minimum_len,a))


# In[41]:


#7
a=[2,3,4,4,6,43,45,6,7,3,10]
threshold=5
b=list(filter(lambda x:x > threshold,a))
print(b)


# # Recursion

# In[2]:


#2
a=int(input("enter the number "))
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
if a<0:
    print("factorial is not defined")
else:
    result=factorial(a)
    print(result)


# In[7]:


#3
a=int(input("enter the number "))
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
if a<0:
    print("fibonacci is not defined")
else:
    result=fibonacci(a)
    print(result)


# In[9]:


#4
a=[1,2,3,4,5,6,7]
def list_sum(n):
    if not n:
        return 0
    else:
        return n[0]+list_sum(n[1:])
result=list_sum(a)
print(result)


# In[10]:


#6
m=int(input("enter the number "))
n=int(input("enter the number "))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
result=gcd(m,n)
print(result)


# In[2]:


#1
# A function is defined with the def keyword, then write the function identifier followed by parentheses and a colon.
# We use function for modularity,reusability,abstraction & organization.


# In[4]:


#2
def square(number):
    result = number ** 2
    return result
a=square(5)
print(a)


# In[ ]:


#3
Function Definition: This is where you create the function, specify its name, parameters, and code implementation. 
    It defines what the function does and how it does it. Function definitions are used to encapsulate and define reusable pieces of code.

Function Call: This is where you actually use the function in your code to execute the task it was designed for.
    During a function call, you provide the necessary arguments, and the function performs its operation and possibly returns a result. 
    Function calls are used to utilize the functionality of a defined function in your program.






# In[5]:


#4
def cal_sum(x,y):
    result=x+y
    return result
a=cal_sum(5,6)
print(a)


# In[ ]:


#5
A function signature, often referred to as a function prototype or declaration, is a concise way of specifying the essential information about a function without including the actual implementation details.
A function signature typically includes the following information:-Function name,parameters,return type,docstring


# In[7]:


#6
def product(x,y):
    result=x*y
    return result
a=product(4,5)
print(a)


# In[ ]:


#1
Formal parameters are placeholders or variables that are used in the function definition to represent the data (arguments) that the function expects to receive when it is called.
They are part of the function's definition and are specified within the parentheses following the function name.

Actual arguments, often simply referred to as "arguments," are the values or expressions provided to a function when it is called.
These values are passed to the corresponding formal parameters in the function definition.


# In[10]:


#2
def greet(name,greeting="hello"):
    message=greeting,name
    return message
a=greet("jas")
print (a)


# In[3]:


#3
##In Python, you can use keyword arguments in function calls to explicitly specify which argument corresponds to which parameter, regardless of the order in which they are defined in the function signature.
##This provides more clarity and flexibility when calling functions. 

def greet(name,greeting="hello"):
    message=greeting,name
    return message
a=greet(name="jas",greeting="hi")
print (a)

b=greet(greeting="hey",name="jessy")
print(b)


# In[1]:


#4
def sum_numbers(x,y):
    return x+y
a=sum_numbers(4,5)
print(a)


# In[ ]:




