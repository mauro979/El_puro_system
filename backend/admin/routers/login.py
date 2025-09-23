from fastapi import HTTPException , status, APIRouter, Request, Response
from funciones import add_user
from user_admin import User_pass,User,Admin
from pymongo import MongoClient
from passlib.context import CryptContext 
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from datetime import datetime, timedelta
from jose import JWTError, jwt

router = APIRouter()

client = MongoClient("mongodb+srv://mauriziogomezvalle5_db_user:XK2Q43xwBqJFWkl6@cluster0.psqey37.mongodb.net/")
db = client.local
user_db = db.user

SECRET_KEY = "c2214cfd41cfe71ada8a20f3007b7b3b50eea2b9c20535475c1afb27e984bbab"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"])
token = OAuth2PasswordBearer(tokenUrl="/autentication")

EXP_TOKEN_DIAS = 15

@router.post("/CreateAccountAdmin",status_code=status.HTTP_201_CREATED)
async def CreateAccount(user : Admin, request: Request, response : Response):

    if not user_db.find_one({"email":user.email}):

        #try:
            #insertando la informacion del admin
            user.password = pwd_context.hash(str(user.password))
            user_db.insert_one(user.model_dump()).inserted_id

            #insertando la informacion de el negocio
            company_info = {
                    "company_name" : user.company_name,
                    "logo" : user.logo
            }
            print("test 1")
            db.company_info.insert_one(company_info).inserted_id

            payload = {
                "sub" : user.username,
                "role" : user.admin,
                "exp" : datetime.now() + timedelta(days=EXP_TOKEN_DIAS)
            }

            token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

            print("test 2")

            response.set_cookie(
                key="access_token",
                value=token,
                httponly=True,
                secure=False,  # True en producción con HTTPS
                samesite="lax"
            )

            
            print(request.cookies)
            return {"message": "Usuario creado correctamente","token" : token}
            
        
        # except Exception as e:
            
        #     raise HTTPException(
        #     status_code=status.HTTP_400_BAD_REQUEST,
        #     detail="ha habido un error de autenticacion"
        # )
        
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="el usuario ya existe"
    )

@router.get("/cookies")
async def obtener_cookies(request : Request, response : Response):


    print(request.cookies)
    return {"cookies":request.cookies}

@router.get("/a")
async def test():
    return {"status" : "ok"}

# from fastapi import Request

# @app.get("/perfil")
# def perfil(request: Request):
#     token = request.cookies.get("access_token")
#     if not token:
#         raise HTTPException(status_code=401, detail="No autenticado")

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token expirado")
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=401, detail="Token inválido")

#     return {"usuario": payload["sub"], "rol": payload["role"]}