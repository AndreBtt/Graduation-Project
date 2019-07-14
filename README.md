# Graduation-Project

Dados dos voos cedidos pela ANAC

- ICAO Empresa Aérea
- Número Voo
- Código DI (Dígito Identificador - exemplo : Vôo Regular, Vôo Cargueiro, Vôo de Serviço, ...)	
- Código Tipo Linha (Sub-Regional, Internacional, Nacional, ...)
- ICAO Aeródromo Origem
- ICAO Aeródromo Destino
- Data Partida Prevista
- Data Partida Real
- Data Chegada Prevista
- Data Chegada Real
- Situação Voo
- Código Justificativa

Dados que iremos definitivamente usar e pq ?

1 - Dados que a principio nao fazem sentido afetar o tempo de atraso
  - Número Voo
 
2 - Dados que talvez sejam menos relevantes e que é bom deixar para teste
  - ICAO Empresa Aérea

3 - Dados que nao fazem sentido deixar pois na previsao nao teremos eles disponiveis
  - Data Partida Real
  - Data Chegada Real
  - Situação Voo
  - Código Justificativa

Dados que nos restaram depois do filtro acima :

- ICAO Empresa Aérea
- Código DI	
- Código Tipo Linha 
- ICAO Aeródromo Origem
- ICAO Aeródromo Destino
- Data Partida Prevista
- Data Chegada Prevista


O que é atraso ??

- qual tempo iremos considerar para julgar se um voo está atrasado ?
