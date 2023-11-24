import pandas as pd #importa a biblioteca pandas com a abreviação pd
import matplotlib.pyplot as plt #importa a biblioteca  como plt

dados = pd.read_csv('cancer_prediction_dataset.csv') # Usa o Pandas para ler o arquivo CSV 'dados.csv' e armazenar os dados em um DataFrame chamado 'dados'
print(dados.head(10)) #vizualização do cabeçalho e das primeiras 9 linhas do arquivo csv

pessoas_com_cancer_fadiga = dados[(dados['Cancer'] == 1) & (dados['Fatigue'] == 1)].head(10) #cria um filtro de apenas pessoas com cancer e fadiga
print(pessoas_com_cancer_fadiga) #mostra as primeiras 10 linhas de pessoas com câncer e fadiga

pessoas_com_cancer = dados[(dados['Cancer'] == 1 )].head(10) #cria um filtro apenas com pessoas com Cancer
print(pessoas_com_cancer) #mostra as primeiras 10 linhas de pessoas com cancer

num_cancer_fadiga = dados[(dados['Cancer'] == 1) & (dados['Fatigue'] == 1)].shape[0] #cria um filtro apenas com pessoas que tem cancer e fadiga e conta quantas pessoas tem
print(num_cancer_fadiga) #mostra quantas pessoas tem cancer e fadiga

num_cancer =  dados[(dados['Cancer'] == 1 )].shape[0] #cria um filtro de apenas pessoas com cancer e conta quantas tem
print(num_cancer) #mostra quantas pessoas com cancer participaram da pesquisa

porcentagem = (num_cancer_fadiga/num_cancer) * 100 #divide o numero de pessoas com cancer e fadiga pelo numero depessoas com cancer e multiplica por 100 para saber a porcentagem de pessoas com cancer que apresentam fadiga
print(f'A porcentagem de pessoas com cancer que apresentam fadiga é: {porcentagem:.2f}%')