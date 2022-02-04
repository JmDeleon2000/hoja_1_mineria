import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
# este archivo de python responde las preguntas e incisos 3, 4.3, 4.6, 4.9, 4.12 y 4.15

datafr = pd.read_csv('movies.csv', ',')

#inicio de pregunta 3
# cuantitativas = datafr.filter(items=['popularity', 'budget', 'revenue',
#                          'runtime', 'productionCoAmount',  'voteAvg',
#                          'genresAmount', 'productionCountriesAmount', 'voteCount',
#                          'actorsAmount', 'castWomenAmount', 'castMenAmount'])
# 
# cualitativas = datafr.filter(items=['actors', 'actorsPopularity', 'actorsCharacter',
#                                      'releaseDate', 'ProductionCountry', 'productionCompanyCountry',
#                                      'productionCompany', 'genres', 'director',
#                                      'video', 'homePage', 'title',
#                                      'original Language', 'original title',])
# 
# tabla_frec = {}
# 
# infodump = ''
# alpha = 1e-3
# 
# 
# for i in cuantitativas:
#     print(f"testing {i}...")
#     try:
#         k2, p = stats.normaltest(cuantitativas[i])
#         if p < alpha:
#             infodump += f"Columna: {i} no es normal" + '\n'
#         else:
#             infodump += f"Columna: {i} es normal" + '\n'
#     except:
#         pass
# 
# 
# for i in cualitativas:
#     print(f"Counting frecuencies for {i}...")
#     tabla_frec[i] = cualitativas[i].value_counts()
# 
# infodump += '\n' + str(tabla_frec) + '\n' 
# 
# with open('datadump.txt', 'w', encoding = 'utf-8') as f:
#     f.write(infodump)
    
#fin de pregunta 3
    
#inicio pregunta 4.3
#sorted_by_votes = datafr.filter(["title", "voteCount"]).sort_values("voteCount", ascending=False)
#print(str(sorted_by_votes["title"]) + str(sorted_by_votes["voteCount"]))
#fin pregunta 4.3

#inicio pregunta 4.6
#top_20_most_recent = datafr.filter(["genres", "releaseDate"]).sort_values("releaseDate", ascending=False).head(20)
#print(top_20_most_recent)
#plt.pie(top_20_most_recent["genres"].value_counts(), labels = top_20_most_recent['releaseDate'])
#plt.show()
#fin  pregunta 4.6

#inicio pregunta 4.9
#revenue_by_actors_sex = datafr.filter(['revenue', 'castWomenAmount', 'castMenAmount'])
#revenue_by_actors_sex = revenue_by_actors_sex.sort_values('revenue', ascending=False)
#fig, axs = plt.subplots(2)
#fig.suptitle('Scatter plots for men amount and women amount VS revenue')
#axs[0].plot(revenue_by_actors_sex["castMenAmount"], revenue_by_actors_sex["revenue"])
#axs[1].plot(revenue_by_actors_sex["castWomenAmount"], revenue_by_actors_sex["revenue"])
#axs[0].get_xaxis().set_visible(False)
#axs[1].get_xaxis().set_visible(False)
#plt.show()
#fin pregunta 4.9

#inicio pregunta 4.12
revenue_by_month = datafr.filter(["revenue"])
revenue_by_month["month"] = pd.DatetimeIndex(datafr["releaseDate"]).month
revenue_by_month = revenue_by_month.groupby("month").revenue.agg(
    ["sum", "min", "max"]).head(12).sort_values('sum', ascending=False)
print(revenue_by_month)
#fin pregunta 4.12

#inicio pregunta 4.14
#runtime_by_genre = datafr.filter(["genres", "runtime"]).sort_values("runtime", ascending = False).groupby("genres")
#print(runtime_by_genre.head(1))
#fin pregunta 4.14
