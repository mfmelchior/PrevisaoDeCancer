import pandas as pd #importa a biblioteca pandas com a abreviação pd
import matplotlib.pyplot as plt #importa a biblioteca  como plt

dados = pd.read_csv('cancer_prediction_dataset.csv') # Usa o Pandas para ler o arquivo CSV 'dados.csv' e armazenar os dados em um DataFrame chamado 'dados'
print(dados.head(10)) #vizualização do cabeçalho e das primeiras 9 linhas do arquivo csv

homens_com_cancer = dados[(dados['Gender'] == 0) & (dados['Cancer'] == 1)].head(10) #cria um filtro de apenas pessoas do sexo masculino com cancer
print(homens_com_cancer) #mostra as primeiras 10 linhas de homens com câncer

homens_idosos = dados[(dados['Gender'] == 0) & (dados['Age'] > 59)].head(10) #cria um filtro apenas com masculino idosos
print(homens_idosos) #mostra as primeiras 10 linhas de homens idosos

num_cancer = dados[(dados['Gender'] == 0) & (dados['Cancer'] == 1)].shape[0] #cria um filtro apenas com pessoas do genero masculino que tem cancer e conta quantas pessoas tem
print(num_cancer) #mostra quantas pessoas são homens e tem cancer

num_idosos = dados[(dados['Gender'] == 0) & (dados['Age'] > 59 )].shape[0] #cria um filtro de apenas homens idosos e conta quantas tem
print(num_idosos) #mostra quantos homens idosos participaram da pesquisa

porcentagem = (num_cancer/num_idosos) * 100 #divide o numero de homens com cancer pelo numero de homens idosos e multiplica por 100 para saber a porcentagem de homens idosos que tem cancer
print(f'A porcentagem de homens idosos com cancer é: {porcentagem:.2f}%')