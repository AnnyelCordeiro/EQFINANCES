# eqfinances
#### A biblioteca provém de módulos de cálculos de matemática financeira básicos, analises de investimentos, permitindo que o usuário realize cálculos financeiros complexos, análise de investimentos e construção de modelos financeiros de forma eficiente e personalizada.
## Vale ressaltar que há módulos que contém a utilização de APIS, para fins de obter informações de ações, dados financeiros, obter taxas de cambio e entre outras análises de dados financeiros.

#
## Instalação
```
pip install eqfinances
```

#
## Como utilizar
```
from eqfinances import *
```
#### Exemplo de aplicabilidade de uma das funções básica: 
##### *JurosSimples(principal, taxa, tempo)*
### Exemplo de uso:

```py
#calcula o valor total (incluindo juros) resultante de um empréstimo com juros simples.
from eqfinances import * 
jurossimples = JurosSimples(1000, 0.05, 2)
print(jurossimples)
```
```py
# Calcula o montante total, incluindo juros compostos, ganho a partir de um capital inicial durante um determinado período de tempo a uma taxa de juros fixa. 
from eqfinances import *
juroscomp = JurosCompostos(1000, 0.03, 3)
print(juroscomp)
```
