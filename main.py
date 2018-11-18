import pandas as pd
from filtroClima import *
from filtroVoo import *

# originWeather = weatherFilter("climaOrigem.csv")
# print(originWeather.iloc[:,:].head(50))
flights = flightFilter("aviao.csv")
# flights = pd.get_dummies(flights, columns = ['ICAO Aer�dromo Destino'])
print(flights.iloc[:,:].head(100))
# print('The shape of our features is:', flights.shape)


# NO JOIN DA PRA PROCURAR POR PREFIXO 

# aviao = pd.read_csv('aviao.csv')
# aviao['periodo'] = aviao['']


# print(features.iloc[:,:5].head(10))