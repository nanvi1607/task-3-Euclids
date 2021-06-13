#!/usr/bin/env python
# coding: utf-8

# ## Registeration ID- SIRSS1005
# ## Name- Dhanisha Sharma
# ## College- Poornima University

# ## Q1. Write a function to return nth term of Fibonacci sequence.

# In[11]:


def fib(n):
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    print(c)

fib(8)


# ## Q2. Write a function to find out GCD of two numbers using EUCLID'S algorithm.

# In[20]:


def euclids_gcd(x,y):
    if x<y:
        x,y = y,x
    while(y):
        x, y = y, x%y
    return x

euclids_gcd(16,48)


# ## Q3. Write a function to find LCM of two number in most optimizers way.

# In[21]:


def euclids_gcd(x,y):
    if x<y:
        x,y = y,x
    while(y):
        x, y = y, x%y
    return x
def lcm(x,y):
    lcm=x*y//euclids_gcd(x,y)
    return lcm


# In[22]:


lcm(14,7)


# In[ ]:




