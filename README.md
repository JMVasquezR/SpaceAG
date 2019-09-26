Este comando inicia el contenedor de postgres

`docker-compose up db`

Este comando inicia el contenedor de aplicación

`docker-compose up app`

Este comando entra al contenedor de la aplicacion, con este aplica el makemigration y el migrate

```
docker exec -it spacead-app sh
python3 manage.py makemigrations
python3 manage.py migrate
```
 
