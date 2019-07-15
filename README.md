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

## Dados climáticos cedidos pela INMET

- codigo estacao (localizacao)

- data  (dia/mes/ano)

- hora  (apenas a hora)

- temperatura instantanea (medida em °C)

- temperatura maxima    (medida em °C)

- temperatura minima    (medida em °C)

- umidade instantanea   (indicada em %)

- umidade maxima    (indicada em %)

- umidade minima    (indicada em %)

- ponto de orvalho instantanea  (medida em °C)

- ponto de orvalho maximo   (medida em °C)

- ponto de orvalho minimo   (medida em °C)

- pressao instantanea   (medida em hPa)

- pressao maxima    (medida em hPa)

- pressao minima    (medida em hPa)

- direcao do vento  (medida em °)

- velocidade vento  (medida em m/s)

- rajada do vento   (medida em m/s)

- radiacao  (medida em kJ/m²)

- precipitacao  (medida em mm)

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
