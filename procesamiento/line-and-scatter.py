from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Gráfica de dispersión por sector'),
    dcc.Graph(id="line-and-scatter-x-scatter-plot"),
    html.P("Filtro por Carpetas de Investigación:"),
    dcc.RangeSlider(
        id='line-and-scatter-x-range-slider',
        min=0, max=200, step=1,
        marks={str(i): str(i) for i in range(0, 201, 10)},
        value=[60, 120]
    ),
])

@app.callback(
    Output("line-and-scatter-x-scatter-plot", "figure"),
    Input("line-and-scatter-x-range-slider", "value"))
def update_scatter_plot(slider_range):
    df = pd.read_csv('../datos/resumen_delitos_con_variacion_y_eficiencia.csv')
    low, high = slider_range
    mask = (df['total_delitos_primera'] > low) & (df['total_delitos_segunda'] < high)

    fig = px.scatter(
        df[mask], x="total_delitos_primera", y="total_delitos_segunda",
        color="total_delitos_primera", size='total_delitos_segunda',
        hover_data=['nombre_sec','variacion_porcentual','eficiencia'])
    
    fig.update_layout(
        width=1800,
        height=800,
        font=dict(size=20)
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)