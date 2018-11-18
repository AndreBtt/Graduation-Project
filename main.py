import pandas as pd
from filtroClima import weatherFilter
from filtroVoo import flightFilter

originWeather = weatherFilter("climaOrigem.csv")
print(originWeather.iloc[:,:].head(10))
flights = flightFilter("aviao.csv")
# flights = pd.get_dummies(flights, columns = ['ICAO Aer�dromo Destino'])
print(flights.iloc[:,:].head(10))

# NO JOIN DA PRA PROCURAR POR PREFIXO 

# aviao = pd.read_csv('aviao.csv')
# aviao['periodo'] = aviao['']


# print(features.iloc[:,:5].head(10))