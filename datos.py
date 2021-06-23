from datetime import datetime
from flask.json import loads


import matplotlib.pyplot as plt
import pandas as pd
import csv
import json

from pandas.core.frame import DataFrame

with open('Monitoring_report.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
with open('Monitoring_report.json','w') as f:
    json.dump(rows, f)

with open('Monitoring_report.json') as file:
    data = json.load(file)


#PRUEBAS Graficos 

df = pd.DataFrame(data)
x = df.iloc[:,0] # X dias selecionados
y = df.iloc[:,1] # Datos a mostrar 1 = ENERGIA;  2 = Reactive_energy.....etc.

#cogemos los 30 primero a falta de filtro que acote dias
x = x.head(30)
y = y.head(30) 


plt.bar(x, y)  
plt.title('Grafica de Datos Electricos')
plt.xticks(rotation = 90) #Evitar superposición etiquetas x
ax = plt.subplot() 
ax.set_xlabel('Dias')  #Nombre del eje x
ax.set_ylabel('Energia')  #Ejemplo grafico energia
plt.show()

