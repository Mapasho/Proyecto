# Readme del proyecto de películas
## Descripción:
Este proyecto se enfoca en la limpieza y análisis de datos relacionados con películas. Se realizaron tareas de limpieza de datos, desinadación y eliminación de columnas para dejar los datos en un formato consumible por una API. También se desarrolló una API utilizando el framework FastAPI. La API tiene seis funciones para endpoints que permiten hacer consultas sobre la cantidad de películas que se estrenaron en un mes o día específico, la cantidad de películas producidas en un país determinado, la cantidad de películas y la ganancia total y promedio de una franquicia, la ganancia total y cantidad de películas producidas por una productora específica, y la información financiera y de lanzamiento de una película específica.

Además, se realizó un análisis exploratorio de datos (EDA) para entender mejor la información a la que se tiene acceso y se preparó un sistema de recomendación de películas. El sistema de recomendación de películas se basa en encontrar la similitud de puntuación entre una película y el resto de películas, ordenarlas según el score de similaridad y devolver una lista de las 5 películas con mayor puntaje, en orden descendente. La función de recomendación se implementó como una función adicional de la API y se puede llamar a través de la misma.


## Funciones de la API:
Las funciones de la API son las siguientes:

### peliculas_mes(mes):
Esta función recibe el mes como parámetro y devuelve la cantidad de películas que se estrenaron históricamente en ese mes. El mes debe ingresarse en formato de cadena de caracteres, por ejemplo 'enero'. La respuesta es un diccionario con el nombre del mes y la cantidad de películas que se estrenaron.

### peliculas_dia(dia):
Esta función recibe el día de la semana como parámetro y devuelve la cantidad de películas que se estrenaron históricamente en ese día. El día de la semana debe ingresarse en formato de cadena de caracteres, por ejemplo 'lunes'. La respuesta es un diccionario con el nombre del día y la cantidad de películas que se estrenaron.

### franquicia(franquicia):
Esta función recibe el nombre de una franquicia como parámetro y devuelve la cantidad de películas de esa franquicia, así como su ganancia total y promedio. El nombre de la franquicia debe ingresarse en formato de cadena de caracteres. La respuesta es un diccionario con el nombre de la franquicia, la cantidad de películas, la ganancia total y la ganancia promedio.

### peliculas_pais(pais):
Esta función recibe el nombre de un país como parámetro y devuelve la cantidad de películas producidas en ese país. El nombre del país debe ingresarse en formato de cadena de caracteres. La respuesta es un diccionario con el nombre del país y la cantidad de películas producidas.

### productoras(productora):
Esta función recibe el nombre de una productora como parámetro y devuelve la ganancia total y la cantidad de películas que produjo. El nombre de la productora debe ingresarse en formato de cadena de caracteres. La respuesta es un diccionario con el nombre de la productora, la ganancia total y la cantidad de películas producidas.

### retorno(pelicula):
Esta función recibe el nombre de una película como parámetro y devuelve la información financiera y de lanzamiento de la película. El nombre de la película debe ingresarse en formato de cadena de caracteres. La respuesta es un diccionario con el nombre de la película, el presupuesto de producción, la ganancia en taquilla, la fecha de lanzamiento y el idioma original.

### recomendar(pelicula):
Esta función recibe el nombre de una película como parámetro y devuelve una lista con las 5 películas con mayor similitud de puntuación, en orden descendente. La función utiliza un modelo de aprendizaje automático previamente entrenado para calcular la similitud de las películas. El nombre de la película debe ingresarse en formato de cadena de caracteres. La respuesta es una lista de diccionarios con el nombre de la película, su puntaje de similitud y su género.

# Prueba de Funciones:
Una vez realizado todo esto se utilizará [Render] a fin de comprobar que las consultas funcionen correctamente en el siguiente Link
https://ariel-proyecto.onrender.com/docs


# Conclusion:
El modelo de aprendizaje automático utilizado en la función de recomendación es un modelo de filtrado colaborativo basado en memoria que utiliza la matriz de valoraciones de las películas para calcular la similitud entre ellas.