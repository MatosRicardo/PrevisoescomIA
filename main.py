# Passo a passo
# Passo 0: Entender a empresa e o desafio dela
#pandas e scikit-learn é para usar a IA

# Passo 1: Importar a base de dados 
import pandas as pd

tabela = pd.read_csv("clientes.csv")


# Passo 2: Preparar a base de dados para a IA
print(tabela)

# LabelEncoder
from sklearn.preprocessing import LabelEncoder

# Profissão

# cientista - 1
# bombeiro - 2
# engenheiro - 3
# dentista - 4
# artista - 5

codificador_profissao = LabelEncoder()
tabela["profissao"] = codificador_profissao.fit_transform(tabela["profissao"])

#mix_credito
codificador_credito = LabelEncoder()
tabela["mix_credito"] = codificador_credito.fit_transform(tabela["mix_credito"])

#comportamento_pagamento
codificador_pagamento = LabelEncoder()
tabela["comportamento_pagamento"] = codificador_pagamento.fit_transform(tabela["comportamento_pagamento"])

# y -> É a coluna da base de dados que eu quero prever
y = tabela["score_credito"]

# x -> As colunas da base de dados que eu vou usar para fazer previsão
x = tabela.drop(columns="score_credito")

# Separar em dados de treino e dados de teste
from sklearn.model_selection import train_test_split

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Passo 3: Treinar a IA -> Criar o modelo: Nota de crédito: Boa, Ok, Ruim


# Passo 4: Escolher qual o melhor modelo
# Passo 5: Usar a IA para fazer novas previsões


#Score de crédito = Nota de crédito

