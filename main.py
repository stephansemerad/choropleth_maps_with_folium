import pandas as pd
import folium, requests, json 

# https://www.kaggle.com/datasets/kaggle/world-development-indicators?resource=download


df = pd.read_csv('./data/indicators.csv')

df['Year'].min(), df['Year'].max()
df['IndicatorName'].unique()
df['IndicatorName'].shape()

df[df['IndicatorName'].str.startswith("L")]['IndicatorName']

indicator = 'Life expectancy at birth, total (years)'
data = df[df['IndicatorName'] == indicator]

MAX_YEAR = data['Year'].max()
data = data[data['Year']== MAX_YEAR]
data.head()

map_data = data[['CountryCode', 'Value']]
map_data.head()

data = open('./data/world-countries.json', 'r', encoding='utf-8').read()
geojson = json.loads(data)


# Possible Color codes: 
# "Spectral", "RdYlGn", "PuBu", "Accent", "OrRd", "Set1", "Set2", "Set3", "BuPu", "Dark2", "RdBu", "Oranges", "BuGn", "PiYG", "YlOrBr", "YlGn", "Pastel2", "RdPu", "Greens", "PRGn", "YlGnBu", "RdYlBu", "Paired", "BrBG", "Purples", "Reds", "Pastel1", "GnBu", "Greys", "RdGy", "YlOrRd", "PuOr", "PuRd", "Blues", "PuBuGn"

m = folium.Map(location=[0, 0], zoom_start=2)
folium.Choropleth(
    geo_data=geojson,
    data = map_data,
    columns=['CountryCode', 'Value'],
    key_on='feature.id',
    fill_color='RdYlGn', 
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=indicator,
).add_to(m)

m.save('map.html')
