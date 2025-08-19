import pandas as pd
import numpy as np

# Generar datos de ejemplo
np.random.seed(42)
n_samples = 100

data = {
    'edad': np.random.randint(18, 65, n_samples),
    'ingresos': np.random.normal(50000, 15000, n_samples),
    'gastos': np.random.normal(30000, 8000, n_samples),
    'ciudad': np.random.choice(['Madrid', 'Barcelona', 'Valencia', 'Sevilla'], n_samples),
    'score_credito': np.random.randint(300, 850, n_samples)
}

df = pd.DataFrame(data)
df['ingresos'] = df['ingresos'].astype(int)
df['gastos'] = df['gastos'].astype(int)

# Guardar en CSV
df.to_csv('../datos/dataset.csv', index=False)
print("Datos generados y guardados en data/dataset.csv")