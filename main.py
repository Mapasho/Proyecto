from typing import Union

import unicodedata as unicodedata

from fastapi import FastAPI

from pandas import read_csv

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import linear_kernel



app = FastAPI()

df = read_csv('df_arreglado.csv')

ml=df.sample(n=1000, random_state=42) # limita el ML

tfidf= TfidfVectorizer(stop_words = 'english') # esta  funcion hace que no se detenga el codigo por algun tipo de error
ml['overview'] = ml['overview'].fillna('') # este codigo rellena los nullos con espacios vacios
tfidf_matrix = tfidf.fit_transform(ml['overview']) # entrena el modelo overwiew
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
ml.drop_duplicates(inplace=True)
ml = ml.reset_index(drop=True)
indices = pd.Series(ml.index, index=ml['title'])




@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes: str) -> dict:
    

    months_translated= {
    'enero': 'January',
    'febrero': 'February',
    'marzo': 'March',
    'abril': 'April',
    'mayo': 'May',
    'junio': 'June',
    'julio': 'July',
    'agosto': 'August',
    'septiembre': 'September',
    'octubre': 'October',
    'noviembre': 'November',
    'diciembre': 'December'}  
    fechas = pd.to_datetime(df['release_date'], format= '%Y-%m-%d')
    n_mes = fechas[fechas.dt.strftime('%B').str.capitalize() == months_translated[str(mes).lower()]]
    respuesta = n_mes.shape[0]
    print(n_mes)
    return {'mes':mes, 'cantidad':respuesta}

@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia: str) -> dict:

    day_translated= {
    'lunes': 'Monday',
    'martes': 'Tuesday',
    'miercoles': 'Wednesday',
    'jueves': 'Thursday',
    'viernes': 'Friday',
    'sabado': 'Saturday',
    'domingo': 'Sunday'}   
    fechas = pd.to_datetime(df['release_date'], format= '%Y-%m-%d')
    n_dia = fechas[fechas.dt.strftime('%A').str.capitalize() == day_translated[str(dia).lower()]]
    respuesta = n_dia.shape[0]
    return {'mes':dia, 'cantidad':respuesta}


@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    f_bajo= franquicia.lower()
    fran= df[['name_collection','budget','revenue',]].dropna(subset=['name_collection'])
    fran= fran[fran['name_collection'].map(str.lower).apply(lambda x: f_bajo in x)]
    cantidad = fran.shape[0]
    gananciat= (fran['revenue']- fran['budget']).sum()
    gananciap= (fran['revenue']- fran['budget']).mean()
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total':gananciat, 'ganancia_promedio': gananciap}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais):
    m1 = df[['title', 'name_countrie']]
    if isinstance(pais, str):
        pais = pais.lower()
        pais = unicodedata.normalize('NFKD', pais).encode('ascii', 'ignore').decode('utf-8','ignore')
        cantidad = m1['title'][m1['name_countrie'].str.contains(pais)==True]
        cantidad = df['name_countrie'].apply(lambda x: str(x).lower()).map(str.lower).apply(lambda x: pais in x)
        respuesta = cantidad.shape[0]
    return {'pais': pais, 'cantidad': respuesta}

@app.get('/productoras/{productora}')
def productoras(productora:str):
    prod = df[['name_production', 'budget', 'revenue']].dropna()
    prod ['name_production'] = prod['name_production'].map(str.lower)
    cantidad = prod.shape[0]
    gtotal= (prod['revenue'] - prod['budget']).sum()
    return {'productora':productora, 'ganancia_total': gtotal, 'cantidad': cantidad }

@app.get('/retorno/{pelicula}')
def retorno(pelicula: str) -> dict:
    pelicula_df = df.loc[df['title'] == pelicula.title()]
    inversion = pelicula_df['budget'].iloc[0].item()
    ganancia = pelicula_df['revenue'].iloc[0].item()
    retorno= pelicula_df['return'].iloc[0].item()
    anio = pelicula_df['release_year'].iloc[0].item()
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio }

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo):
    idx = indices[titulo]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key= lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    recommendations=list(ml['title'].iloc[movie_indices].str.title())
    return {'lista recomendada': recommendations}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}