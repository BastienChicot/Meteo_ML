# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:57:38 2022

@author: basti
"""

import os
os.getcwd()
os.chdir("OneDrive/Bureau/Programmes python/Meteo")
import requests
import pandas as pd


##WEATHERSTACK GRATUIT PAS DE DONNEES HISTORIQUES 
#Créer une variable api_key avec a clé d'accès dispo sur le site dans mon compte
r = requests.get(str("http://api.weatherstack.com/current?access_key="+str(api_key)+"&query=Mulhouse"))

data = r.json()

print(data)

temperature = data["current"]["temperature"] 
print(temperature)


data = pd.read_csv("bases/bases_ods.csv", sep=";")
full = pd.read_csv("bases/base_totale.csv", sep=";")

print(min(full["Date"]))

data.columns

data['communes (name)'].unique()

import matplotlib.pyplot as plt
from tqdm import tqdm

test = data.loc[data['communes (name)'] == 'Nice']

test = test.reset_index()

liste_ligne = []

for i in tqdm(test.index):
    if test['Date'][i][11:13] == '13':
        row = test.iloc[[i]]
        liste_ligne.append(row)

test2 =  pd.concat(liste_ligne)
test2 = test2.reset_index()

test = test.sort_values(by=["Date","communes (name)"])

plt.title("evo temp 2022")
plt.plot(test["Date"], test['Température'])
plt.xlabel('Date')
plt.ylabel('Température')
plt.show()


##Colonnes utiles :
    #Communes name
    #Température
    #Température en Celsius
    #Précipitations
    #'Humidité', 'Visibilité horizontale',
    #'Hauteur totale de la couche de neige, glace, autre au sol'
    
    ##ALLER VOIR LA DOC SUR LE SITE https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/information/?flg=fr&sort=date&q.from_date.date=date%3E%3D%222021-12-31T23:00:00Z%22
    
    ##Rechercher les normales saisonnières