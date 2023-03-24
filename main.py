import pandas as pd
import numpy as np
import networkx as nx

if __name__ == '__main__':
    fromPlace = input('Ingrese el estación de origen: ')
    toPlace = input('Ingrese el estación de destino: ')
    print('-------------------------------------------')

    df = pd.read_excel('metro.xlsx')
    df.head()

    try:
        METRO = nx.from_pandas_edgelist(
            df, source="Origen", target="Destino", edge_attr='Longitud de interestación')
        djk_path = nx.dijkstra_path(
            METRO, source=fromPlace, target=toPlace, weight='Longitud de interestación')
    except:
        print('No existe alguna de las estaciones ingresadas')

    try:
        metros = nx.dijkstra_path_length(
            METRO, fromPlace, toPlace, 'Longitud de interestación')
    except:
        print('No existe una ruta entre las estaciones ingresadas')
    else:
        print("Cantidad de estaciones por las que debe pasar: ", len(djk_path))
        print('-------------------------------------------')
        print("Ruta: ")
        for i in range(len(djk_path)-1):
            print("Parada: ", djk_path[i], " -> ", djk_path[i+1])
        print('-------------------------------------------')
        print("Metros a recorrer: ", metros)
