from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# Read the Excel file
df = pd.read_excel("Pasta1.xlsx")

# Create the initial figure
fig = px.bar(df, x="Produto", y="Valor Unitario", color="Produto")

app.layout = html.Div(children=[
    html.H1(children="Faturamento do Produto"),
    html.H2(children='Gráfico com faturamento de todos os produtos'),

    dcc.Graph(
        id='grafico_quandidade_produto',
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)