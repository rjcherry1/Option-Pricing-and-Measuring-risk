#!/usr/bin/env python
# coding: utf-8

# In[15]:


#import necessary libraries and packages
import numpy as np
import pandas as pd
from scipy.stats import *
import random


# In[23]:


seed = 123
risk_free_rate = 0.065
initial_stock_price = 75.00
strike_price = 65.00
volatility = 0.3
time = 365/365
trials = 1000



def calculate_black_scholes_price(risk_free_rate, initial_stock_price, strike_price, time, decision = "call"):
    d1 = (np.log(initial_stock_price/strike_price) + time * (risk_free_rate + volatility**2/2))/(volatility * np.sqrt(time))
    d2 = d1 - volatility * np.sqrt(time)
    if decision == "call":
        #price equation if specification is for a call
        price = initial_stock_price * norm.cdf(d1) - strike_price * np.exp(-risk_free_rate * time) * norm.cdf(d2)
        return round(price, 3)
    elif decision == "put":
        #price equation  if specification is for a put
        price = strike_price * np.exp(-risk_free_rate * time) * norm.cdf(-d2) - initial_stock_price * norm.cdf(-d1) 
        return round(price, 3)

print("The price for a put is $", 
calculate_black_scholes_price(risk_free_rate, initial_stock_price, strike_price, time, decision = "put"))

print("The price for a call is $", 
calculate_black_scholes_price(risk_free_rate, initial_stock_price, strike_price, time))

#I am aiming to create an array and through a for loop, output the results of C for each trial 
#trials = 500
#for i in range(trials):
    #r = random()
    #S = randint(1, 500)
    #K = randint(1, 500)
    #T = random()
    #sigma = random()
    #C = calculate_C(r, S, K, T, sigma)
    #array['T'] = T
    #array['r'] = r
    #array['S'] = S
    #array['K'] = K
    #array['Sigma'] = sigma
    #array['Option Price'] = C
       
#print(array)    


# In[ ]:




