from EQFINANCES import *
''' TESTES EQFINANCES_Taxas '''
#TESTE MÉTODO JUROS SIMPLES


jurossimples = JurosSimples(1000, 0.05, 2)
print(jurossimples)

#TESTE MÉTODO JUROS COMPOSTOS
'''capital = 1000
taxa = 0.05
tempo = 2 #anos

juroscomp = JurosCompostos(capital, taxa, tempo)
print(juroscomp)'''

#TESTE MÉTODO TAXA DE JUROS
'''capital = 2000
futuro = 3000
tempo = 2

taxajuros = TaxaJuros(capital, futuro, tempo)
print(f"{taxajuros:.4f}")'''

#TESTE MÉTODO TAXA EQUIVALENTE
'''taxa = 0.1
periodo_taxa = 12
periodo_equivalente = 1

taxaeq = TaxaEquivalente(taxa, periodo_taxa, periodo_equivalente)
print(f"{taxaeq:.2f}")'''

#TESTE MÉTODO TAXA NOMINAL
'''taxa_efetiva = 0.1
periodo = 12

taxanominal = TaxaNominal(taxa_efetiva, periodo)

print(f"{taxanominal:.2f}")'''

#TESTE MÉTODO TAXA REAL
'''taxa_nominal = 10
taxa_inflacao = 3.5

taxareal = TaxaReal(taxa_nominal, taxa_inflacao)

print(f"{taxareal:.2f}")'''

#TESTE MÉTODO TAXA EFETIVA
'''taxa_nominal = 10
periodo = 12

taxaefetiva = TaxaEfetiva(taxa_nominal, periodo)

#print(f"{taxaefetiva:.2f}")'''

''' TESTES EQFINANCES_Custos '''
#TESTE MÉTODO CUSTO REAL 
'''custos_diretos = 1000
custos_indiretos = 500

custoreal = CustoReal(custos_diretos,custos_indiretos)

print(custoreal)'''

#TESTE MÉTODO CUSTO TOTAL EMPRÉSTIMO
'''valor_emprestado  = 10000
taxa_juros = 0.05
periodo_pagamento = 2

totalemprestimo = CustoTotalEmprestimo(valor_emprestado,taxa_juros, periodo_pagamento)
print(f"{totalemprestimo:.2f}")'''




