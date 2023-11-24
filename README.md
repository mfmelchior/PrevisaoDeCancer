## Sobre o conjunto de dados

O conjunto de dados fornecido é uma coleção de informações gerada sinteticamente com o objetivo de simular um cenário de previsão de câncer para fins de pesquisa. É composto por 10.000 pseudopacientes, cada um caracterizado por cinco parâmetros distintos, a saber: Gênero, Idade, Tabagismo, Fadiga e Alergia, juntamente com um indicador binário que denota a presença ou ausência de câncer. Este conjunto de dados sintético serve como uma ferramenta para os pesquisadores explorarem e experimentarem modelos preditivos para detecção de câncer.

A coluna ‘Gênero’ é representada por valores binários, onde 0 corresponde ao masculino e 1 corresponde ao feminino. 'Idade' abrange uma faixa de 18 a 100 anos, refletindo a idade do paciente em anos. 'Fumar' é um atributo binário, com 0 indicando não fumante e 1 significando histórico de tabagismo. 'Fadiga' é igualmente binário, com 0 denotando a ausência de fadiga e 1 representando a sua presença. 'Alergia' é uma variável binária que indica a presença ou ausência de alergias no paciente.

A coluna 'Câncer' é a variável alvo principal, onde 0 significa a ausência de câncer e 1 indica um caso simulado de câncer. É importante enfatizar que este conjunto de dados é totalmente sintético e não derivado de registros clínicos reais. Os pesquisadores são incentivados a usar este conjunto de dados para fins exploratórios, desenvolvimento de modelos e testes de algoritmos. No entanto, deve notar-se que os resultados obtidos a partir deste conjunto de dados não devem ser extrapolados para cenários médicos do mundo real sem validação em dados clínicos autênticos. A natureza sintética deste conjunto de dados permite a experimentação controlada e serve como um recurso valioso para pesquisas preliminares no campo da previsão do câncer. - Safiul

Fonte dos dados: https://www.kaggle.com/datasets/ohinhaque/synthetic-cancer-prediction-dataset-for-research/

## Sobre as previsões em Python

No arquivo **mulheres fumantes** temos a visualização de dados e a relação de porcentagem entre mulheres fumantes e o câncer.
<br>
O arquivo **homens idosos** trabalha a relação entre homens idosos (60+) e a incidência de câncer.
<br>
O arquivo **fadiga** mostra a porcentagem de pessoas com câncer que apresentam fadiga.