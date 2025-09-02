#imports

import httpx
import datetime
from config import api_key

#funciones
def setFecha():
    fechaStr=input("El formato de la fecha debe ser el siguiente: AAAA-MM-DDTHH:MM:SS")
    try:
        fecha=datetime.datetime.strptime(fechaStr,"%Y-%m-%dT%H:%M:%S")
        return fecha.strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError:
        raise ValueError("La fecha no tiene el formato AAAA-MM-DDTHH:MM:SS o no es válida")
def setUrl():
    fechaIniStr=setFecha()
    fechaFinStr=setFecha()
    identificacion=input("identificador de la estación")
    return f"https://opendata.aemet.es/opendata/api/antartida/datos/fechaini/{fechaIniStr}/fechafin/{fechaFinStr}/estacion/{identificacion}"
#variables
url=setUrl()
endPoint= httpx.get(f"{url}?api_key={api_key}")
print (endPoint.json())