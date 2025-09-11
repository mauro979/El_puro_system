from fastapi import FastAPI , HTTPException , status
from pydantic import BaseModel
from funciones import add_user

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Lista de orígenes permitidos
origins = [
    "*"
]

# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # Solo estos orígenes pueden acceder
    allow_credentials=False,
    allow_methods=["*"],                # Puedes restringir si lo deseas
    allow_headers=["*"]                # Puedes especificar headers permitidos
)


class User(BaseModel):
    username : str
    company_name : str
    logo : str

class User_pass(User):
    password : str

@app.post("/autentication")
async def autenticar_cliente(client : User_pass):
    try:

        add_user("data/data.json",client)
        return {"status":"ok"}
    
    except Exception as e:
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ha habido un error de autenticacion"
        )