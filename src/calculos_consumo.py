"""
WUE (Média do Data Center) - 1,8 L/kWh

WUE (Meta de Eficiência) - 0,2 L/kWh ou menos

Consumo de Energia (Tokens)	
0,24 Wh de energia por input de IA globalmente.	
Estimativa de metodologia abrangente para atender IA globalmente (Google).


Consumo de Água (Tokens)	
0,26 mL de água por input de IA globalmente.
Estimativa de metodologia abrangente (Google).

Consumo de Água (Geração)	
1 garrafa de água (aprox. 500 mL) a cada 100 palavras geradas.
Estimativa em estudo sobre o consumo de modelos como o ChatGPT.

Consumo de Energia (Geração)	
0,14 kWh a cada 100 palavras geradas.
Estimativa no mesmo estudo sobre o ChatGPT.

"""
def calcula_economia_de_tokens:
    tokens_ecnomizados = tokens_original - tokens_otimizados
    return None

def calcula_economia_de_conumo:
    economia_energia = tokens_ecnomizados*0.24
    economia_agua = tokens_ecnomizados*0.26
    return None
 