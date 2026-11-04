# Backend Aliados Travel

Este es el backend de la prueba de Aliados Travel, hecho con Flask.

## Levantar sin Docker

Necesitas tener Python 3.12 instalado. Desde la carpeta del proyecto, crea y activa un entorno virtual:

```bash
python -m venv venv
```

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instala las dependencias y levanta el servidor:

```bash
pip install -r requirements.txt
flask --app wsgi run --host 0.0.0.0 --port 5000
```

El backend queda disponible en `http://localhost:5000`.

## Levantar con Docker

Con Docker en ejecución, crea la imagen y levanta el contenedor:

```bash
docker build -t backend-aliados-travel .
docker run --rm -p 5000:5000 backend-aliados-travel
```

El backend también queda disponible en `http://localhost:5000`.

## Ejecutar los tests

Activa el entorno virtual e instala las dependencias, si todavía no lo hiciste. Luego ejecuta:

```bash
python -m pytest
```

Para correr los tests desde Docker:

```bash
docker build -t backend-aliados-travel .
docker run --rm backend-aliados-travel python -m pytest
```

## Endpoints

- `POST /api/sort`: ordena una lista de números enviada como JSON.
- `POST /api/uppercase`: recibe un archivo `.txt` y cuenta sus letras mayúsculas.
