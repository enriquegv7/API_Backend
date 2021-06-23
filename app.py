from flask import Flask, jsonify
app = Flask(__name__)

import pandas as pd
from datos import data

@app.route('/datos', methods=['GET']) #GET simple, muestra datos  
def getdatos():
    return jsonify(data)


@app.route('/datos/star=<String:start_date>&end=<String:end_date>') #Busqueda por intervalo de fecha
def getDatosDate(start_date, end_date):
    #deberia implementarse comprobando las variables start_date y end_date

    return


@app.route('/datos/<String:specific_data>') #Busqueda por columna de datos especificas(energia, power, voltage, etc..)
def getDatosDate(specific_data):
    #debe implementarse mostar columna == specific_data

    return


if __name__ =='__main__':
    app.run(debug=True, port=4000)
