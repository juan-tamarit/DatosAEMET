#imports

import httpx
import datetime
from config import api_key

#funciones
def setFecha():
    fechaStr=input("El formato de la fecha debe ser el siguiente: AAAA-MM-DDTHH:MM:SS")
    try:
        fecha=datetime.datetime.strptime(fechaStr,"%Y-%m-%dT%H:%M:%S")
        return fecha.strftime("%Y-%m-%dT%H:%M:%SUTC")
    except ValueError:
        raise ValueError("La fecha no tiene el formato AAAA-MM-DDTHH:MM:SS o no es válida")
def setIdentificacion():
    x=int(input("Seleccione estación \n 1. Gabriel de Castilla \n 2. Juan Carlos I"))
    if x==1:
        return 89070
    elif x==2:
        return 89064
def setUrl():
    fechaIniStr=setFecha()
    fechaFinStr=setFecha()
    identificacion= setIdentificacion()
    return f"https://opendata.aemet.es/opendata/api/antartida/datos/fechaini/{fechaIniStr}/fechafin/{fechaFinStr}/estacion/{identificacion}"
#variables
url=setUrl()
endPoint= httpx.get(f"{url}?api_key={api_key}",timeout=30.0)
url_datos=endPoint.json()["datos"]
datos= httpx.get(f"{url_datos}?api_key={api_key}")
print(datos.json())