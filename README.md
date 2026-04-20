# Análise de Churn de Clientes

Este projeto apresenta uma análise de churn com o objetivo de identificar padrões de cancelamento e entender os principais fatores que impactam a retenção de clientes.

A proposta é explorar os dados, gerar insights relevantes e aplicar um modelo simples de previsão para antecipar possíveis cancelamentos.

---

## Objetivo

Identificar variáveis que influenciam o churn e avaliar a possibilidade de prever quais clientes têm maior risco de cancelar o serviço.

---

## Etapas do projeto

**1. Exploração dos dados**
- Leitura e entendimento do dataset
- Verificação de tipos de dados e valores ausentes

**2. Tratamento**
- Conversão de variáveis
- Remoção de valores inconsistentes

**3. Análise exploratória**
- Taxa geral de churn
- Churn por tipo de contrato
- Relação entre tempo de cliente e cancelamento
- Impacto do valor mensal

**4. Visualização**
- Construção de gráficos para facilitar a interpretação dos dados

**5. Modelo de previsão**
- Aplicação de um modelo de machine learning (Random Forest)
- Avaliação da capacidade de prever churn

---

## Principais insights

- Clientes com contrato mensal apresentam maior taxa de cancelamento
- Clientes com menor tempo de permanência tendem a sair mais
- Valores mensais mais altos estão associados a maior churn
- Contratos de longo prazo contribuem para retenção

---

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib /  Seaborn
- Scikit-learn

---

## Como executar

1. Instalar as dependências:
pip install pandas matplotlib seaborn scikit-learn

2. Executar o notebook:
notebook/analise_churn.ipynb

---

## Sobre o projeto

Este projeto foi desenvolvido com foco em aplicar conceitos de análise de dados em um cenário próximo do mundo real, passando por todas as etapas do processo: tratamento, análise, visualização e modelagem preditiva.