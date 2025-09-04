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
def getData():
    try:
        url=setUrl()
        endPoint= httpx.get(f"{url}?api_key={api_key}",timeout=30.0)
        endPoint.raise_for_status()
        url_datos=endPoint.json()["datos"]
        datos= httpx.get(f"{url_datos}?api_key={api_key}")
        datos.raise_for_status()
        return datos.json()
    except httpx.RequestError as exc:
        print (f"Error en la conexión al intentar acceder a {exc.request.url}->{exc}")
    except httpx.HTTPStatusError as exc:
        print(f"Error HTTP {exc.status_code} en la url {exc.request.url}")
    except ValueError:
        print(f"La respuesta no tiene un formato JSON válido")
#variables
data=getData()