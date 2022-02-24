#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


# save filepath to variable for easier access
forecast_path = pd.read_csv(r'C:\Users\User\OneDrive\Pulpit\zadanie rekrutacyjne\jena_climate_2009_2016.csv')


# In[ ]:


# read the data and store data in DataFrame titled prognoza_data
forecast_data = forecast_path

forecast_data.info();


# In[ ]:


#Date Time ma NIEODPOWIEDNI format, należy go zrzutować na format daty
from datetime import datetime, timedelta
from pandas import DataFrame

forecast_data['Date Time'] = pd.to_datetime(forecast_data['Date Time'],unit='ns')

# Podgląd wskazuje, że rzutowanie przebiegło pomyślnie
print(forecast_data['Date Time'])


# In[ ]:


#sprawdzanie czy nie ma brakujących danych

missing_values_count = forecast_data.isnull().sum()
# get the number of missing data points per column
missing_values_count[0:len(forecast_data.columns)]


# In[ ]:





# In[ ]:


#jak widać nie ma brakujących danych, więc nie jest konieczne uzupełnianie zmiennymi bądź usuwanie danych z pliku


# In[ ]:


# Tworzenie opisu danych
forecast_data.describe()


# In[ ]:


# Interpretacja Danych
# Resultatem describe() jest pokazanie ośmiu liczb dla każdej z oryginalnych kolumn.


# In[ ]:


forecast_data.columns


# In[ ]:


# Plik posiada 16 kolumn które przechowują różne wartości fizyczne, niekonieczne niezbędne do stworzenia modelu prognozy pogody


# In[ ]:


# Na przykład: Kolumna 'Tpot (K)' jest temperaturą podaną w kelvinach. 
# Takie dane nie są potrzebne do wyznaczonego modelu, zatem zostaną usunięte.


# In[ ]:


forecast_data.drop('Tpot (K)', axis='columns',inplace=True) 


# In[19]:


# Następnie usuwam dane które mają wysoką kardynalność
# wczesniej jednak tworzę kopię obiektu i na nim wykonuję operację

forecast_data.drop(columns=['Date Time', 'p (mbar)', 'T (degC)', 'Tdew (degC)','rh (%)', 
                                 'VPmax (mbar)', 'VPact (mbar)', 'VPdef (mbar)', 'sh (g/kg)',
       'H2OC (mmol/mol)', 'rho (g/m**3)', 'wv (m/s)', 'max. wv (m/s)',
       'wd (deg)'], axis=1)


# In[20]:


# Tak przygotowane dane można użyć do stworzenia modelu prognozy pogody


# In[21]:


# Ustalanie Targetu
 
y = forecast_data['T (degC)']
# Ustalanie Feature


X = forecast_data[['Date Time', 'p (mbar)', 'T (degC)', 'Tdew (degC)','rh (%)', 
                                 'VPmax (mbar)', 'VPact (mbar)', 'VPdef (mbar)', 'sh (g/kg)',
       'H2OC (mmol/mol)', 'rho (g/m**3)', 'wv (m/s)', 'max. wv (m/s)',
       'wd (deg)']]


# In[22]:


# import Split Data do dokładniejszego treningu
from sklearn.model_selection import train_test_split
# podział danych jest konieczny. Należy podzielić dane na treningowe i validacyjne i na nich osobno stworzyć modele do porównania 
# MAE
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)


# In[23]:


# import Modelu Random Forest Regressor 
#import Mean Absolute Error
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# In[18]:


#Tworzenie modelu

forecast_model = RandomForestRegressor(random_state=1)
forecast_model.fit(train_X, train_y)
forecast_predictions = forest_model.predict(val_X)
print(mean_absolute_error(val_y, forecast_predictions))


# In[ ]:




