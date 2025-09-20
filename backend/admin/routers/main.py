from fastapi import FastAPI
from login import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

# Lista de orígenes permitidos
origins = [
    "http://127.0.0.1:5500"
]

# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,              # Solo estos orígenes pueden acceder
    allow_credentials=True,
    allow_methods=["*"],                # Puedes restringir si lo deseas
    allow_headers=["*"]                # Puedes especificar headerjs permitidos
)