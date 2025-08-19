import pandas as pd
from bokeh.plotting import figure, save
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10_4

# Cargar datos
df = pd.read_csv('../datos/dataset.csv')

# Crear ColumnDataSource
source = ColumnDataSource(df)

# Mapear colores para ciudades
ciudades = df['ciudad'].unique()
paleta = Category10_4

# Crear figura
p = figure(
    title="Relación entre Ingresos y Gastos (Bokeh)",
    width=1000,
    height=600,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)

# Crear scatter plot
scatter = p.scatter(
    x='ingresos',
    y='gastos',
    source=source,
    size=12,
    alpha=0.7,
    color=factor_cmap('ciudad', palette=paleta, factors=ciudades),
    legend_field='ciudad'
)

# Configurar tooltips
hover = HoverTool(
    tooltips=[
        ("Ciudad", "@ciudad"),
        ("Ingresos", "@ingresos{0,0} €"),
        ("Gastos", "@gastos{0,0} €"),
        ("Edad", "@edad"),
        ("Score", "@score_credito")
    ]
)
p.add_tools(hover)

# Personalizar
p.xaxis.axis_label = "Ingresos Anuales (€)"
p.yaxis.axis_label = "Gastos Anuales (€)"
p.title.text_font_size = "16pt"

# Guardar
save(p, '../salidas/bokeh_scatter.html')
print("Gráfico de Bokeh guardado en outputs/bokeh_scatter.html")