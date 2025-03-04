# Gastos API

¡Bienvenido al Gastos API! Esta API está diseñada para gestionar gastos y proporciona funcionalidades para crear, leer, actualizar y eliminar gastos.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu entorno de desarrollo:

- [Python](https://www.python.org/downloads/) (Versión 3.9 o superior)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea y activa un entorno virtual para el proyecto.
3. Instala las dependencias del proyecto ejecutando el siguiente comando:
```
pip install -r requirements.txt

```
4. Realiza las migraciones de la base de datos:
```
python manage.py migrate

```
## Uso

Para iniciar el servidor de desarrollo, ejecuta el siguiente comando:

```
python manage.py runserver


```
O puedes Utilizar Docker 

```
docker build -t nombre-de-la-imagen .
docker run -p 8000:8000 nombre-de-la-imagen

```
Esto creará un contenedor y lo ejecutará, mapeando el puerto 8000 del contenedor al puerto 8000 de tu máquina local. Puedes acceder a tu aplicación en http://localhost:8000.


La API estará disponible en `http://localhost:8000`.

## Endpoints

- `GET /gastos/`: Obtiene la lista de todos los gastos.
- `POST /gastos/`: Crea un nuevo gasto.
- `GET /gastos/<id>/`: Obtiene los detalles de un gasto específico.
- `PUT /gastos/<id>/`: Actualiza un gasto específico.
- `DELETE /gastos/<id>/`: Elimina un gasto específico.
Tambien puedes importar en postman el archivo 

```
PruebaTecnica.postman_collection.json

```
## Autenticación

La autenticación para esta API se realiza utilizando JWT (JSON Web Tokens). Para obtener un token JWT, envía una solicitud POST al endpoint `/api/token/` con los siguientes datos:

```json
{
  "username": "user_api",
  "password": "P4sw0rd#.2025"
}
```
El token JWT generado se debe incluir en la cabecera de autorización de todas las solicitudes posteriores utilizando el siguiente formato:



```
Authorization: JWT <tu_token_jwt>

```
