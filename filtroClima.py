import pandas as pd

def weatherFilter(filePath):

    weather = pd.read_csv(filePath)
    weather['periodo'] = weather['data'] + ' ' + weather['hora'].astype(str)

    weather = weather.drop(columns="data")
    weather = weather.drop(columns="hora")
    weather = weather.drop(columns="temp_max")
    weather = weather.drop(columns="temp_min")
    weather = weather.drop(columns="umid_max")
    weather = weather.drop(columns="umid_min")
    weather = weather.drop(columns="pto_orvalho_inst")
    weather = weather.drop(columns="pto_orvalho_max")
    weather = weather.drop(columns="pto_orvalho_min")
    weather = weather.drop(columns="pressao_max")
    weather = weather.drop(columns="pressao_min")
    # weather = weather.drop(columns=" vento_rajada")
    weather = weather.drop(columns="radiacao")
    # weather = weather.drop(columns="precipitacao")
    weather.rename(columns={'codigo_estacao': 'regiao', 'temp_inst': 'temperatura', 'umid_inst': 'umidade', 'vento_direcao': 'direcaoVento', 'vento_vel' : 'velocidadeVento'}, inplace=True)


    return weather