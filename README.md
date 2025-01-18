# Análise de Score de Crédito com IA  - Jornada Python

Este projeto utiliza inteligência artificial para analisar o score de crédito de clientes, classificando o histórico financeiro em três categorias: **Bom**, **Ok** ou **Ruim**. A análise é baseada em dados fornecidos e utiliza algoritmos de machine learning para realizar predições com base no histórico financeiro.

## Funcionalidades  

- **Classificação do score de crédito:**  
  O sistema avalia se um cliente possui um histórico financeiro bom, ok ou ruim.  
- **Treinamento e validação:**  
  Utiliza algoritmos de aprendizado supervisionado para treinamento do modelo.  
- **Visualização e análise de dados:**  
  Processamento de dados para análise e insights utilizando o Pandas.

## Tecnologias Utilizadas  

- **Python**  
- **Pandas:** Para manipulação e análise de dados.  
- **Scikit-learn:** Para treinamento e validação de modelos de machine learning.  
- **Random Forest:** Algoritmo para classificação baseado em árvores de decisão.  
- **K-Nearest Neighbors (KNN):** Algoritmo para classificação baseado em proximidade dos dados.  

## Como Funciona  

1. **Pré-processamento de dados:**  
   Os dados dos clientes são carregados e tratados, incluindo limpeza, remoção de valores nulos e normalização.  

2. **Treinamento dos modelos:**  
   Os algoritmos Random Forest e KNN são treinados com os dados históricos.  

3. **Classificação:**  
   Após o treinamento, os modelos são utilizados para prever a categoria do score de crédito do cliente.  

4. **Validação dos resultados:**  
   Métricas como **acurácia** e **matriz de confusão** são usadas para avaliar o desempenho dos modelos.

## Instalação  

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seuusuario/score-credito-ia.git
   cd score-credito-ia
