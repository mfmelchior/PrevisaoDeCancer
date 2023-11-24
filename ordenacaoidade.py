import pandas as pd #importa a biblioteca pandas com a abreviação pd

dados = pd.read_csv('cancer_prediction_dataset.csv') # Carregar o arquivo CSV para um DataFrame
dados_ordenados = dados.sort_values(by='Age') #ordena os dados pela coluna da idade

dados_ordenados.to_csv('ordenado_por_idade.csv', index=False)  # Salvar o DataFrame ordenado de volta para um novo arquivo CSV
# index=False para evitar a gravação do índice
