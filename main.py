# Passo a passo
# Passo 0: Entender a empresa e o desafio dela
# Passo 1: Importar a base de dados 
import pandas as pd

tabela = pd.read_csv("clientes.csv")
print(tabela)

# Passo 2: Preparar a base de dados para a IA
# Passo 3: Treinar a IA -> Criar o modelo: Nota de crédito: Boa, Ok, Ruim
# Passo 4: Escolher qual o melhor modelo
# Passo 5: Usar a IA para fazer novas previsões

#pandas e scikit-learn é para usar a IA

#Score de crédito = Nota de crédito