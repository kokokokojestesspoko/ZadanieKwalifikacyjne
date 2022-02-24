#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np


# In[12]:


# save filepath to variable for easier access
forecast_path = pd.read_csv(r'C:\Users\User\OneDrive\Pulpit\zadanie rekrutacyjne\jena_climate_2009_2016.csv')


# In[20]:


# read the data and store data in DataFrame titled prognoza_data
forecast_data = forecast_path



# In[26]:


#sprawdzanie czy nie ma brakujących danych

missing_values_count = forecast_data.isnull().sum()
# get the number of missing data points per column
missing_values_count[0:len(forecast_data.columns)]


# In[ ]:


#jak widać nie ma brakujących danych, więc nie jest konieczne uzupełnianie zmiennymi bądź usuwanie danych z pliku


# In[19]:


# Tworzenie opisu danych
forecast_data.describe()


# In[15]:


# Interpretacja Danych
# Resultatem describe() jest pokazanie ośmiu liczb dla każdej z oryginalnych kolumn.


# In[16]:


forecast_data.columns


# In[17]:


# Plik posiada 16 kolumn które przechowują różne wartości fizyczne, niekonieczne niezbędne do stworzenia modelu prognozy pogody


# In[ ]:


# Na przykład: Kolumna 'Tpot (K)' jest temperaturą podaną w kelvinach. 
# Takie dane nie są potrzebne do wyznaczonego modelu, zatem zostaną usunięte.


# In[27]:


forecast_data.drop('Tpot (K)', axis=1) 


# In[ ]:


# Tak przygotowane dane można użyć do stworzenia modelu prognozy pogody

