import pandas as pd #importa a biblioteca pandas com a abreviação pd
import matplotlib.pyplot as plt #importa a biblioteca  como plt

dados = pd.read_csv('cancer_prediction_dataset.csv') # Usa o Pandas para ler o arquivo CSV 'dados.csv' e armazenar os dados em um DataFrame chamado 'dados'
print(dados.head(10)) #vizualização do cabeçalho e das primeiras 9 linhas do arquivo csv

mulheres_com_cancer = dados[(dados['Gender'] == 1) & (dados['Cancer'] == 1)].head(10) #cria um filtro de apenas pessoas do sexo feminino com câncer
print(mulheres_com_cancer) #mostra as primeiras 10 mulheres com câncer

mulheres_fumantes = dados[(dados['Gender'] == 1) & (dados['Smoking'] == 1)].head(10) #cria um filtro apenas com mulheres fumantes
print(mulheres_fumantes) #mostra as primeiras 10 linhas de mulheres fumantes

num_cancer = dados[(dados['Gender'] == 1) & (dados['Cancer'] == 1)].shape[0] #cria um filtro apenas com pessoas do genero feminino que tem cancer e conta quantas pessoas tem
print(num_cancer) #mostra quantas pessoas são mulheres e tem cancer

num_fumantes = dados[(dados['Gender'] == 1) & (dados['Smoking'] == 1)].shape[0] #cria um filtro de apenas mulhares fumantes e conta quantas tem
print(num_fumantes) #mostra quantas mulheres fumantes participaram da pesquisa

porcentagem = (num_cancer/num_fumantes) * 100 #divide o numero de mulhares com cancer pelo numero de mulheres fumantes e multiplica por 100 para saber a porcentagem de mulhares fumantes que tem cancer
print(f'A porcentagem de mulheres fumantes com cancer é: {porcentagem:.2f}%')

