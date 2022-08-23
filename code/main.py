from fastapi import *
from fastapi.security import *
from fastapi.middleware.cors import CORSMiddleware
from typing import *
from pydantic import *
import pyrebase
import sqlite3
import os

DATABASE_URL = os.path.join("sql/clientes.sqlite")

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

firebaseConfig = {
    'apiKey': "AIzaSyCqj3Z8irHli98I_1EMPTUdjYbk8PGbiGc",
    'authDomain': "fir-python-391af.firebaseapp.com",
    'databaseURL': "https://fir-python-391af-default-rtdb.firebaseio.com/",
    'projectId': "fir-python-391af",
    'storageBucket': "fir-python-391af.appspot.com",
    'messagingSenderId': "205184224915",
    'appId': "1:205184224915:web:d87b95f477140b0fe90766",
    'measurementId': "G-FMGNDZQH7X"
}

firebase = pyrebase.initialize_app(firebaseConfig)

securityBasic = HTTPBasic()
securityBearer = HTTPBearer()


class Cliente(BaseModel):
    id_cliente: int
    nombre: str
    email: str

@app.get('/')
async def get():
    mensaje = {"Hola": "Mundo"}
    return mensaje


@app.get('/user/token_value/', status_code=status.HTTP_202_ACCEPTED,
         summary="Mostrar token",
         description="Mostrar token por usuario registrado",
         tags=["auth"])
async def get_token(credentials: HTTPBasicCredentials = Depends(securityBasic)):
    try:
        email = credentials.username
        password = credentials.password
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        response = {
            'token': user["idToken"]
        }
        return response
    except Exception as error:
        print(error)
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@app.post("/registro/{email}/{password}",
          status_code=status.HTTP_202_ACCEPTED,
          summary="Registro",
          description="Registro",
          tags=["auth"]
          )
async def nuevo_usuario(email: str, password:str):
    try:
        auth = firebase.auth()
        data = auth.create_user_with_email_and_password(email, password)
        datos = {
            "email" : email,
            "level" : 1
        }
        db = firebase.database()
        db.child("users").child(data["localId"]).set(datos)
        mensaje = {"registro": "completo"}
        return mensaje
    except:
        mensaje = {"registro":"fallido"}
        return mensaje

@app.get("/clientes", response_model=List[Cliente],
         status_code=status.HTTP_202_ACCEPTED
         )
         
async def list_clientes(credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        response = cursor.fetchall()
        return response

@app.post('/insertar/{nombre}/{email}')
async def Insertar(nombre: str, email: str, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO clientes (nombre,email) VALUES (?,?)', (nombre, email))
        cursor.fetchall()
        return {"mensaje": "Cliente agregado"}

@app.delete('/eliminar/{id}')
async def eliminar(id: int, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(
            'DELETE FROM clientes WHERE id_cliente= {}'.format(int(id)))
        cursor.fetchall()
        return {"mensaje": "Cliente borrado"}

@app.put('/actulizar/{id}/{nombre}/{email}')
async def actulizar(id: str, nombre: str, email: str, credentials: HTTPAuthorizationCredentials = Depends(securityBearer)):
    with sqlite3.connect(DATABASE_URL) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE clientes SET nombre = ?, email = ? WHERE id_cliente = ?', (nombre, email, id))
        cursor.fetchall()
        return {"mensaje": "Cliente Actualizado"}