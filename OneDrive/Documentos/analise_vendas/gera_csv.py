import pandas as pd
import numpy as np
import os

# Passo 1: Preparar dados
categories = ['Eletrônicos', 'Roupas', 'Livros', 'Casa', 'Brinquedos']
dates = pd.date_range(start='2025-05-01', end='2025-05-15')
n = 100

# Passo 2: Gerar dados aleatórios
np.random.seed(42)
data = {
    'date': np.random.choice(dates, size=n),
    'category': np.random.choice(categories, size=n),
    'price': np.round(np.random.uniform(10, 1500, size=n), 2),
    'quantity': np.random.randint(1, 5, size=n),
    'rating': np.random.randint(1, 6, size=n)
}

# Passo 3: Criar DataFrame
df = pd.DataFrame(data)

# Passo 4: Verificar os dados no terminal
print("\nPrimeiras linhas do DataFrame:")
print(df.head())

# Passo 5: Salvar como CSV
csv_path = os.path.abspath('sales.csv')
df.to_csv(csv_path, index=False)
print(f"\n✅ Arquivo 'sales.csv' criado com sucesso em: {csv_path}")
