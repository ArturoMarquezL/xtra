# xtra
# ver todos los repositorios 
docker ps -a

# iniciar un repositorio
docker start -i PRIMEROS TRES NUMEROS DE ID DE REPOSITORIO

# crear imagen con dockerfile
docker buid -t nombre_de_la_imagen .

# crear el repositorio con carpeta 
docker run -it -v /workspace/xtra/code:/home/xtra/code --net=host --name apix -h arturo api_extra

# crear base de datos con archivo sql 
sqlite3 clientes.sqlite < clientes.sql

# correr api
cd home/xtra/code
uvicorn main:app --reload