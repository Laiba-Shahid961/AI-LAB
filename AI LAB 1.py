#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter a number"))
if n%2==0:
    print("you entered an even number")
else:
    print("you entered an odd number")


# In[2]:


sum=0
n=int(input("enter an integer value:"))
while n!=0:
    sum=sum+n
    n=int(input("enter an integer value:"))
print("sum of given values is",sum)


# In[3]:


isPrime=True
i=2
n=int(input("enter a number:"))
while n>i:
    remainder=n%i
    if remainder==0:
        isPrime=False
        break
    else:
        i=i+1
if isPrime:
    print("The number is a prime number")
else:
    print("The number is a not a prime number")


# In[4]:


sum=0
i=0
while i<5:
    num=int(input("enter a number"))
    sum=sum+num
    i=i+1
print("the sum of five integers is ",sum)


# In[5]:


sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1
print("the sum of first ten numbers is ",sum)


# In[6]:


name = input('What is your name? ') 
print('Hello ' + name)
job = input('What is your job? ') 
print('Your job is ' + job)
num = input('Give me a number? ') 
print('You said: ' + str(num))


# In[7]:


import random
# Awroken
MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True
print ("Alright...")
while RUNNING:
 GUESS =input("What is your lucky number? ")
 if int(GUESS) < NUMBER:
        print ("Wrong, too low.")
 elif int(GUESS) > NUMBER:
     print ("Wrong, too high.")
 elif GUESS.lower() == "exit":
     print ("Better luck next time.")
 elif int(GUESS) == NUMBER:
     print ("Yes, that's the one, %s." %str(NUMBER))
 if TRY < 2:
     print ("Impressive, only %s tries." % str(TRY))
 elif TRY > 2 and TRY < 10:
     print( "Pretty good, %s tries." % str(TRY))
 else:
     print ("Bad, %s tries." % str(TRY))
 RUNNING = False
 TRY += 1


# In[8]:


n=str(input("enter the integers"))
i=len(n)
k=i-1
while k>=0:
    print(n[k],end='')
    k=k-1


# In[11]:


setOfIntegers=[]
n=int(input("enter the number of integers you want to enter"))
i=0
while n-1>=i:
    integer=int(input())
    setOfIntegers.append(integer)
    i=i+1
k=0
sumEven=0
sumOdd=0
while n-1>=k:
    if setOfIntegers[k]%2==0:
        sumEven=sumEven+setOfIntegers[k]
    else:
        sumOdd=sumOdd+setOfIntegers[k]
    k=k+1
print("The sum of even numbers is :",sumEven)
print("The sum of odd numbers is :",sumOdd)

    


# In[13]:


i=0
k=1
sum=0
l=1
while l<=10:
    sum=i+k
    print(sum,end=' ')
    i=k
    k=sum
    l=l+1
    


# In[16]:


n=int(input("Enter a number"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print("The factorial of the number is",fact)


# In[21]:


marks=int(input("Enter your marks"))
if marks<50:
    print("YOUR GRADE IS F")
if marks>50 and marks<60:
    print("YOUR GRADE IS E")
if marks>61 and marks<70:
    print("YOUR GRADE IS D")
if marks>71 and marks<80:
    print("YOUR GRADE IS C")
if marks>81 and marks<90:
    print("YOUR GRADE IS B")
if marks>91 and marks<=100:
    print("YOUR GRADE IS A")


# In[ ]:





# In[ ]:





