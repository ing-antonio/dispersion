import pandas as pd
import plotly.express as px
import plotly.io as pio

# Cargar datos
df = pd.read_csv('../datos/dataset.csv')
print("Datos cargados:")
print(df.head())
print(f"\nForma del dataset: {df.shape}")

# Crear gráfico de dispersión con Plotly
fig = px.scatter(
    df, 
    x='ingresos', 
    y='gastos', 
    color='ciudad',
    size='score_credito',
    title='Relación entre Ingresos y Gastos por Ciudad',
    labels={
        'ingresos': 'Ingresos Anuales (€)',
        'gastos': 'Gastos Anuales (€)',
        'ciudad': 'Ciudad',
        'score_credito': 'Score Crediticio'
    },
    hover_data=['edad']
)

# Personalizar el gráfico
fig.update_layout(
    width=1000,
    height=600,
    font=dict(size=12)
)

# Guardar como HTML interactivo
pio.write_html(fig, '../salidas/plotly_scatter.html')
print("Gráfico de Plotly guardado en outputs/plotly_scatter.html")