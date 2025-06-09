import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carrega os dados
df = pd.read_csv('sales.csv')

# Mostra as 5 primeiras linhas
print("🔍 Primeiras linhas do DataFrame:")
print(df.head())

# Verifica tipos de dados e valores nulos
print("\nℹ️ Informações do DataFrame:")
print(df.info())

print("\n📉 Estatísticas descritivas:")
print(df.describe())

# Total de vendas por categoria (faturamento = preço * quantidade)
df['total_venda'] = df['price'] * df['quantity']
vendas_por_categoria = df.groupby('category')['total_venda'].sum().sort_values(ascending=False)

print("\n💰 Vendas totais por categoria:")
print(vendas_por_categoria)

# Média de avaliação por categoria
avaliacao_media = df.groupby('category')['rating'].mean().sort_values(ascending=False)

print("\n⭐ Avaliação média por categoria:")
print(avaliacao_media)

# Gráfico de barras: Vendas por categoria
plt.figure(figsize=(10, 6))
vendas_por_categoria.plot(kind='bar', color='skyblue')
plt.title('💰 Faturamento por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Total em R$')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_vendas_categoria.png")  # salva o gráfico
plt.show()

# Gráfico de pizza: Distribuição de quantidade vendida
quantidade_total = df.groupby('category')['quantity'].sum()
plt.figure(figsize=(7, 7))
quantidade_total.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='tab20')
plt.title('📦 Distribuição de Produtos Vendidos por Categoria')
plt.ylabel('')
plt.tight_layout()
plt.savefig("grafico_pizza_quantidade.png")  # salva o gráfico
plt.show()

