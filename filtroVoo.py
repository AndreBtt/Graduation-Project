import pandas as pd

def deleteUselessColumns(flight):
    flight = flight.drop(columns="ICAO Empresa A�rea")
    flight = flight.drop(columns="N�mero Voo")
    flight = flight.drop(columns="C�digo Autoriza��o (DI)")
    flight = flight.drop(columns="C�digo Tipo Linha")

    return flight

def renameColumns(flight):
    flight.rename(
        columns={
            'ICAO Aer�dromo Origem': 'origem',
            'ICAO Aer�dromo Destino': 'destino',
            'Situa��o Voo': 'situacao',
            'C�digo Justificativa': 'justificativa'
        }, 
        inplace=True
    )

    return flight

def getTime(x):
    x = str(x)
    print(x.split(' '))
    return "15"

def checkDelay(flight):

    # FILTRAR OS DADOS PARA VALORES NULOS


    # modificar o valor de partida e chegada para ser HH:MM onde HH = hora e MM = minuto
    flight['Partida Prevista'] = flight['Partida Prevista'].apply(getTime)

    # filtrar apenas voos que possuem justificativa do clima ou nulos (nao atrasado)
    # flight = flight[(flight['justificativa'] == "WR") | (flight['justificativa'] == "XS") | (flight['justificativa'] == "RM") | (flight['justificativa'] == "AM") ]

    # deletar colunas que eram uteis apenas para verificar o atraso
    flight = flight.drop(columns="Partida Real")
    flight = flight.drop(columns="Chegada Real")
    flight = flight.drop(columns="justificativa")

    return flight

def flightFilter(filePath):

    # colunas importantes : chegada prevista, partida prevista, origem, destino, target
    # OBS: chegada e partida oq é importante ? O dia a hora e o minuto, ou apenas o dia e hora, ou apenas a hora ...
    # para o primeiro teste vou deixar apenas a hora e minuto

    # target sera calculado com a diferença de tempo entre chegada real e chegada prevista e ainda se a justificativa foi devido ao tempo
    # devemos estabelecer um threshold para saber se foi atraso ou nao, a principio 15 min 

    flight = pd.read_csv(filePath)

    # deletar colunas inuteis
    flight = deleteUselessColumns(flight)
    
    # renomear colunas
    flight = renameColumns(flight)

    # verificar se houve atraso e se foi devido as codicoes climaticas
    flight = checkDelay(flight)
    
    # para filtrar os elementos de uma coluna basta botar a condicao dentro das chaves
    # livros[livro.paginas > 100] -> filtra a coluna paginas ( livros que tem mais de 100 paginas )
    
    # Origin airport
    flight = flight[flight.origem == "SBBR"]

    # Destination airport
    flight = flight[flight.destino == "SBSP"]
    
    # essa funcao categoriza as colunas
    # se tem origem X e origem Y vira ->  origem_X   origem_Y
    #                                       0           1
    flight = pd.get_dummies(flight)

    return flight