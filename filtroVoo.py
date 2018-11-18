import pandas as pd

def flightFilter(filePath):

    flight = pd.read_csv(filePath)
    flight = flight.drop(columns="ICAO Empresa A�rea")
    flight = flight.drop(columns="N�mero Voo")
    flight = flight.drop(columns="C�digo Autoriza��o (DI)")
    flight = flight.drop(columns="C�digo Tipo Linha")
    flight.rename(columns={'ICAO Aer�dromo Origem': 'origem', 'ICAO Aer�dromo Destino': 'destino', 'Situa��o Voo': 'situacao', 'C�digo Justificativa': 'justificativa'}, inplace=True)

    # Origin airport
    flight = flight[flight.origem == "SBBR"]

    # Destination airport
    flight = flight[flight.destino == "SBSP"]

    for i, _ in flight.iterrows():
        # primeiro verificar se ouve atraso dps atualiza os valores
        # flight.at[i,'atraso'] = True

        if str(flight.at[i,'Chegada Prevista']) != "nan": 
            flight.at[i,'Chegada Prevista'] =  str(flight.at[i,'Chegada Prevista']).split(':')[0]
        if str(flight.at[i,'Partida Prevista']) != "nan": 
            flight.at[i,'Partida Prevista'] = str(flight.at[i,'Partida Prevista']).split(':')[0]

    flight = flight.drop(columns="Chegada Prevista")
    flight = flight.drop(columns="Partida Prevista")
    flight = flight.drop(columns="Partida Real")
    flight = flight.drop(columns="Chegada Real")

    flight = flight[(flight['justificativa'] == "WR") | (flight['justificativa'] == "XS") | (flight['justificativa'] == "RM") | (flight['justificativa'] == "AM") | (flight['justificativa'].isnull())]

    flight = pd.get_dummies(flight)

    return flight