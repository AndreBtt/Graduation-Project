# Graduation Project

## Dados dos voos cedidos pela ANAC

- ICAO Empresa Aérea

- Número Voo

- Código DI (Dígito Identificador - exemplo : Vôo Regular, Vôo Cargueiro, Vôo de Serviço, ...)	

- Código Tipo Linha (Sub-Regional, Internacional, Nacional, ...)

- ICAO Aeródromo Origem

- ICAO Aeródromo Destino

- Data Partida Prevista ( dia/mes/ano hora:minuto )

- Data Partida Real ( dia/mes/ano hora:minuto )

- Data Chegada Prevista ( dia/mes/ano hora:minuto )

- Data Chegada Real ( dia/mes/ano hora:minuto )

- Situação Voo (realizado ou cancelado)

- Código Justificativa (em caso de atraso ou cancelamento)

### Dados que iremos definitivamente usar e pq ?

1 - Dados que a principio nao fazem sentido afetar o tempo de atraso
  - Número Voo
 
2 - Dados que talvez sejam menos relevantes e que é bom deixar para teste
  - ICAO Empresa Aérea

3 - Dados que nao fazem sentido deixar pois na previsao nao teremos eles disponiveis
  - Data Partida Real
  - Data Chegada Real
  - Situação Voo
  - Código Justificativa

### Dados que nos restaram depois do filtro acima :

- ICAO Empresa Aérea
- Código DI	
- Código Tipo Linha 
- ICAO Aeródromo Origem
- ICAO Aeródromo Destino
- Data Partida Prevista
- Data Chegada Prevista

## Dados climáticos cedidos pela INMET ([link](./Nota_Tecnica-Rede_estacoes_INMET.pdf))

- codigo estacao (localizacao)

- data  (dia/mes/ano)

- hora  (apenas a hora)

- Temperatura Instantânea do Ar (medida em °C)

- Temperatura Máxima do Ar    (medida em °C)

- Temperatura Mínima do Ar    (medida em °C)

- Umidade Relativa Instantânea do Ar   (indicada em %)

- Umidade Relativa Máxima do Ar    (indicada em %)

- Umidade Relativa Mínima do Ar    (indicada em %)

- Temperatura Instantânea do Ponto de Orvalho  (medida em °C)

- Temperatura Máxima do Ponto de Orvalho   (medida em °C)

- Temperatura Mínima do Ponto de Orvalho   (medida em °C)

- Pressão Atmosférica Instantânea do Ar   (medida em hPa)

- Pressão Atmosférica Máxima do Ar    (medida em hPa)

- Pressão Atmosférica Mínima do Ar    (medida em hPa)

- Direção do Vento  (medida em °)

- Velocidade Instantânea do Vento  (medida em m/s)

- Intensidade da Rajada do Vento   (medida em m/s)

- Radiação Solar  (medida em kJ/m²)

- Precipitação acumulada no período  (medida em mm)

### Dados que iremos definitivamente usar e pq ?

1 - Dados que a principio nao fazem sentido afetar o tempo de atraso
  - todos os dados parecerem fazer sentido
 
2 - Dados que talvez sejam menos relevantes e que é bom deixar para teste :
  - temperatura maxima
  - temperatura minima
  - umidade maxima
  - umidade minima
  - ponto de orvalho maximo
  - ponto de orvalho minimo
  - pressao maxima
  - pressao minima

  Será que os minimos é maximos afetam ? Ou apenas os instantaneos ?

3 - Dados que nao fazem sentido deixar pois na previsao nao teremos eles disponiveis
  - Talvez todos os dados citados sejam possiveis de serem previstos

### Dados que nos restaram depois do filtro acima :
    
- codigo estacao
- data
- hora
- temperatura instantanea
- umidade instantanea   
- ponto de orvalho instantanea  
- pressao instantanea   
- direcao do vento  
- velocidade vento  
- rajada do vento   
- radiacao  
- precipitacao  

## Como juntar dados dos voos e dados climáticos ?

## O que é atraso ??

Qual tempo iremos considerar para julgar se um voo está atrasado ?
