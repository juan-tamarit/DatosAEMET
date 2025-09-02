from dotenv import load_dotenv
import os
#localización del .env
load_dotenv()
#carga de keys
api_key=os.getenv("AEMET_API_KEY")