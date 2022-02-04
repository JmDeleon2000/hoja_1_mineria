import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
# este archivo de python responde las preguntas e incisos 3, 4.3, 4.6, 4.9, 4.12 y 4.15

datafr = pd.read_csv('movies.csv', ',')


cuantitativas = datafr.filter(items=['popularity', 'budget', 'revenue',
                         'runtime', 'productionCoAmount',  'voteAvg',
                         'genresAmount', 'productionCountriesAmount', 'voteCount',
                         'actorsAmount', 'castWomenAmount', 'castMenAmount'])

cualitativas = datafr.filter(items=['actors', 'actorsPopularity', 'actorsCharacter',
                                     'releaseDate', 'ProductionCountry', 'productionCompanyCountry',
                                     'productionCompany', 'genres', 'director',
                                     'video', 'homePage', 'title',
                                     'original Language', 'original title',])

tabla_frec = {}

infodump = ''
alpha = 1e-3


for i in cuantitativas:
    print(f"testing {i}...")
    try:
        k2, p = stats.normaltest(cuantitativas[i])
        if p < alpha:
            infodump += f"Columna: {i} no es normal" + '\n'
        else:
            infodump += f"Columna: {i} es normal" + '\n'
    except:
        pass


for i in cualitativas:
    print(f"Counting frecuencies for {i}...")
    tabla_frec[i] = cualitativas[i].value_counts()

infodump += '\n' + str(tabla_frec) + '\n' 

with open('datadump.txt', 'w', encoding = 'utf-8') as f:
    f.write(infodump)