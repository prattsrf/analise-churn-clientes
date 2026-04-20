import pandas as pd

# carregando dados
df = pd.read_csv('data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# visão geral
print("Primeiras linhas:")
print(df.head())

print("\nInformações:")
print(df.info())

# limpeza básica
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

# taxa de churn
churn_rate = df['Churn'].value_counts(normalize=True) * 100
print("\nTaxa de churn (%):")
print(churn_rate)

# churn por tipo de contrato
print("\nChurn por contrato:")
print(pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100)

# churn por tempo de cliente
print("\nTempo médio por churn:")
print(df.groupby('Churn')['tenure'].mean())

# churn por valor mensal
print("\nValor médio mensal por churn:")
print(df.groupby('Churn')['MonthlyCharges'].mean())