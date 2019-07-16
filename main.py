import pandas as pd

data = pd.read_csv("./vra_062019.csv")

# por padrao ele da drop nas linhas, como queremos dropar colunas temos que setar axis (eixo) para 1
data = data.drop(["Número Voo", "ICAO Empresa Aérea", "Data Partida Real", "Data Chegada Real", "Situação Voo", "Código Justificativa"], axis=1)

print(data.head())