#imports

import httpx
import datetime
from config import api_key

#funciones
def setFecha():
    fechaStr=input("El formato de la fecha debe ser el siguiente: AAAA-MM-DDTHH:MM:SS")
    try:
        fecha=datetime.strptime(fechaStr,"%Y-%m-%dT%H:%M:%S")
        return fecha.strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError:
        raise ValueError("La fecha no tiene el formato AAAA-MM-DDTHH:MM:SS o no es válida")
#variables
fechaIniStr=setFecha()
fechaFinStr=setFecha()
identificacion=input("identificador de la estación")
endPoint= httpx.get("https://opendata.aemet.es/opendata/api/antartida/fechaini/{fechaIniStr}/fechafin/{fechaFinStr}/estacion/{identificacion}", headers={"api_key":api_key})
print (endPoint)