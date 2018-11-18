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

    return flight