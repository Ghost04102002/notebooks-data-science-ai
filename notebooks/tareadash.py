import dash
from dash import dcc
from dash import html
import pandas as pd
import geopandas as gpd
import plotly.express as px

#Creo que tuve problemas con las rutas porque lo trabaje sin "Anaconda Navigator" y me perdi de la ruta...
#Por eso esta con la absoluta y no con relativas
gdf = gpd.read_file(r"C:\Users\Sebastian\OneDrive\Escritorio\ICD\notebooks\data.geojson")
fig = px.scatter_geo(gdf,
                     lat=gdf.geometry.y,
                     lon=gdf.geometry.x,
                     color="precio",
                     hover_name="Name",
                     size="precio",
                     projection="mercator",
                     title="Precios por Región")

gdf2 = gpd.read_file(r"C:\Users\Sebastian\OneDrive\Escritorio\ICD\notebooks\data2.geojson")
fig2 = px.scatter_geo(gdf2,
                      lat=gdf2.geometry.y,
                      lon=gdf2.geometry.x,
                      color="preciomt2",
                      hover_name="Name",
                      size="preciomt2",
                      projection="mercator",
                      title="Precio por metro cuadrado por Región")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Visualización de Parroquias y Zonas"),
    dcc.Graph(id='geo-graph1', figure=fig, style={'height': '40vh', 'width': '80vw'}),
    dcc.Graph(id='geo-graph2', figure=fig2, style={'height': '40vh', 'width': '80vw'})
])

if __name__ == '__main__':
    app.run_server(debug=True)