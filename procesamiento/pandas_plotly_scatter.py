import pandas as pd
import plotly.express as px
import plotly.io as pio

df = pd.read_csv('../datos/resumen_delitos_por_sector.csv')
print("Datos cargados:")
print(df.head())
print(f"\nForma del dataset: {df.shape}")

fig = px.scatter(
    df, 
    x='total_delitos', 
    y='total_delitos', 
    color='evaluacion',
    size='total_delitos',
    title='Gráfica de dispersión por sector',
    labels={
        'nombre_sec': 'nombre_sec',
        'nombre_sec': 'nombre_sec',
        'categoria_delito': 'categoria_delito'
    },
    hover_data=['total_delitos']
)

fig.update_layout(
    width=1500,
    height=1000,
    font=dict(size=12)
)

def update_bar_chart(slider_range):
    df = pd.read_csv('../datos/resumen_delitos_por_sector.csv')
    low, high = slider_range
    mask = (df['petal_width'] > low) & (df['petal_width'] < high)
    fig = px.scatter(
        df[mask], x="sepal_width", y="sepal_length",
        color="species", size='petal_length',
        hover_data=['petal_width'])
    return fig

update_bar_chart(df['total_delitos'])

pio.write_html(fig, '../salidas/plotly_scatter.html')