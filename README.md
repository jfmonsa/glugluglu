# API RESTful con FastAPI

Este proyecto implementa una API RESTful utilizando FastAPI que realiza operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un recurso `item`. Los datos se almacenan en un diccionario en memoria, simulando una base de datos.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instrucciones para ejecutar localmente

Para ejecutar la API de forma local, sigue los siguientes pasos:

1. **Clona este repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Instala las dependencias:**

   Puedes instalar las dependencias necesarias utilizando `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   O si no tienes un archivo `requirements.txt`, instala `fastapi` y `uvicorn` manualmente:

   ```bash
   pip install fastapi uvicorn
   ```

3. **Ejecuta la aplicación:**

   Una vez que tengas todo instalado, puedes ejecutar el servidor con `uvicorn`:

   ```bash
   uvicorn main:app --reload
   ```

4. La API estará corriendo en `http://127.0.0.1:8000`.

5. **Accede a la documentación interactiva de la API:**

   La documentación generada automáticamente está disponible en:

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

La API cuenta con los siguientes endpoints:

### 1. **POST /items/**
Crea un nuevo `item`.

- **URL:** `/items/`
- **Método:** `POST`
- **Payload (Ejemplo):**
  ```json
  {
    "name": "Laptop",
    "description": "Laptop de última generación con pantalla de 15 pulgadas",
    "price": 1200.99,
    "stock": 10
  }
  ```
- **Respuesta (Ejemplo):**
  ```json
  {
    "name": "Laptop",
    "description": "Laptop de última generación con pantalla de 15 pulgadas",
    "price": 1200.99,
    "stock": 10
  }
  ```

- **Descripción:** Crea un nuevo `item` con la información proporcionada.

#### Cómo probar con `curl`:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Laptop",
  "description": "Laptop de última generación con pantalla de 15 pulgadas",
  "price": 1200.99,
  "stock": 10
}'
```

### 2. **GET /items/**
Obtiene todos los `items`.

- **URL:** `/items/`
- **Método:** `GET`
- **Respuesta (Ejemplo):**
  ```json
  [
    {
      "name": "Laptop",
      "description": "Laptop de última generación con pantalla de 15 pulgadas",
      "price": 1200.99,
      "stock": 10
    }
  ]
  ```

- **Descripción:** Devuelve una lista de todos los `items` almacenados en la base de datos simulada.

#### Cómo probar con `curl`:

```bash
curl -X 'GET' 'http://127.0.0.1:8000/items/'
```

### 3. **GET /items/{item_id}**
Obtiene un `item` específico por su `id`.

- **URL:** `/items/{item_id}`
- **Método:** `GET`
- **Ejemplo de URL:** `/items/1`
- **Respuesta (Ejemplo):**
  ```json
  {
    "name": "Laptop",
    "description": "Laptop de última generación con pantalla de 15 pulgadas",
    "price": 1200.99,
    "stock": 10
  }
  ```

- **Descripción:** Devuelve un `item` específico basado en el `id` proporcionado.

#### Cómo probar con `curl`:

```bash
curl -X 'GET' 'http://127.0.0.1:8000/items/1'
```

### 4. **PUT /items/{item_id}**
Actualiza un `item` por su `id`.

- **URL:** `/items/{item_id}`
- **Método:** `PUT`
- **Ejemplo de URL:** `/items/1`
- **Payload (Ejemplo):**
  ```json
  {
    "name": "Laptop Pro",
    "description": "Laptop de última generación con pantalla de 16 pulgadas",
    "price": 1500.99,
    "stock": 8
  }
  ```

- **Respuesta (Ejemplo):**
  ```json
  {
    "name": "Laptop Pro",
    "description": "Laptop de última generación con pantalla de 16 pulgadas",
    "price": 1500.99,
    "stock": 8
  }
  ```

- **Descripción:** Actualiza un `item` existente con el `id` proporcionado.

#### Cómo probar con `curl`:

```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/items/1' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Laptop Pro",
  "description": "Laptop de última generación con pantalla de 16 pulgadas",
  "price": 1500.99,
  "stock": 8
}'
```

### 5. **DELETE /items/{item_id}**
Elimina un `item` por su `id`.

- **URL:** `/items/{item_id}`
- **Método:** `DELETE`
- **Ejemplo de URL:** `/items/1`
- **Respuesta (Ejemplo):**
  ```json
  {
    "detail": "Item deleted successfully"
  }
  ```

- **Descripción:** Elimina un `item` de la base de datos simulada.

#### Cómo probar con `curl`:

```bash
curl -X 'DELETE' 'http://127.0.0.1:8000/items/1'
```

## Despliegue en la Nube

La API está desplegada en [Render](https://render.com/), un servicio gratuito de alojamiento de aplicaciones web. Puedes acceder a la API desplegada a través del siguiente enlace:

[Enlace a la API desplegada](https://tu-app.onrender.com)

### Documentación interactiva

Una vez desplegada, la documentación interactiva está disponible en:

- [Swagger UI](https://tu-app.onrender.com/docs)
- [Redoc](https://tu-app.onrender.com/redoc)

## Conclusión

Este proyecto demuestra cómo crear una API RESTful sencilla utilizando FastAPI con funcionalidades CRUD y almacenamiento en memoria. Además, la API está completamente documentada con Swagger UI y Redoc para facilitar su prueba y uso. Puedes probar la API tanto de manera local como en la nube.