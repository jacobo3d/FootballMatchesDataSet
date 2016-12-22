# -*- coding: utf-8 -*-

import time
import ScrapBDFutbol as bdFutbol
# import ScrapTemporada2015 as thisTemporada

# Guardo los partidos de futbol en un diccionario
partidos = dict()

# Obtengo los partidos de futbol de las temporadas anteriores
partidos = bdFutbol.getPartidos()

# Obtengo los partidos de futbol de la temporada presente
# partidos2015_16 = thisTemporada.getPartidos(bdFutbol.getContador())

file_name = 'DataSetPartidos_%s.csv' % time.strftime("%d-%m-%Y")
file = open(file_name,'w')
file.write('Partido,Temporada,Jornada,Local,Visitante,Goles Local,Goles Visitante,Fecha,Timestamp\n')

for key,value in partidos.items():
    file.write('%s\n' % str(value))

# for key,value in partidos2015_16.items():
#     file.write('%s\n' % str(value))

file.close()