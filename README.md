# IBM Stock Price Prediction API

Proyecto final del curso Machine Learning Operations.

Este proyecto implementa una API de predicción del precio de cierre de la acción de IBM utilizando un modelo de Machine Learning entrenado con datos históricos de precios.

## Servicio desplegado

La API se encuentra desplegada en una instancia EC2 de AWS utilizando Docker.

URL pública de documentación:

```text
http://54.162.215.165:8000/docs
```

Endpoint de salud:

```text
http://54.162.215.165:8000/health
```

## Dataset

Fuente: IBM Stock Prices 1980-2025, Kaggle.

Archivo utilizado:

```text
data/IBM_Stock_1980_2025.csv
```

## Modelo

Tipo de problema: Regresión.

Variable objetivo:

```text
Close
```

Variables predictoras:

```text
Open
High
Low
Volume
```

Modelo utilizado:

```text
RandomForestRegressor
```

## Endpoints

```text
GET /
GET /health
POST /predict
```

## Ejecutar localmente

```bash
python -m uvicorn api.main:app --reload
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/docs
```

## Ejecutar con Docker

Construir imagen:

```bash
docker build -t ibm-stock-api:v1.0 .
```

Ejecutar contenedor:

```bash
docker run -d -p 8000:8000 --name ibm-stock-container ibm-stock-api:v1.0
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/docs
```

Detener contenedor:

```bash
docker stop ibm-stock-container
docker rm ibm-stock-container
```

## Pruebas

```bash
pytest
```

## Métricas

Las métricas del modelo se guardan en:

```text
models/metrics.json
```

## Arquitectura

```mermaid
flowchart LR
    A[Desarrollador] --> B[GitHub]
    B --> C[GitHub Actions CI/CD]
    C --> D[Docker Build]
    D --> E[Servicio desplegado]
    C --> F[Reentrenamiento]
    F --> G[Modelo entrenado]
    G --> H[API FastAPI]
    F --> I[metrics.json]
    F --> J[S3 + DVC]
```

## Estado actual

- API creada con FastAPI.
- Modelo entrenado con RandomForestRegressor.
- Pruebas con Pytest.
- Dockerfile funcional.
- Métricas guardadas en JSON.

## Versionamiento de datos y modelos con DVC + S3

El proyecto utiliza DVC para versionar los datos y el modelo entrenado.  
Los archivos pesados no se almacenan directamente en GitHub, sino que se gestionan mediante archivos `.dvc`.

Bucket S3 utilizado:

```text
s3://mlops-orlich-final
```

Archivos versionados con DVC:

```text
data/IBM_Stock_1980_2025.csv.dvc
models/model.pkl.dvc
```

Comandos utilizados:

```bash
dvc init
dvc remote add -d storage s3://mlops-orlich-final
dvc add data/IBM_Stock_1980_2025.csv
dvc add models/model.pkl
dvc push
```

Para recuperar los datos y el modelo desde S3:

```bash
dvc pull
```