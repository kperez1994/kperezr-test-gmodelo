### kperezr-test-gmodelo

# API search
API que permite el filtrado y b煤squeda de informaci贸n basada en los datos de "https://download.geonames.org/"

### Pre-requisitos 馃搵
Contar con algun agente que nos permita hacer peticiones HTTPS. _Se sugiere el uso de postman._

### Detalles t茅cnicos de la API 鈿欙笍

| M茅todo | Endpoint/Request | 
| --- | --- | 
| GET | ```https://11kyqx45f1.execute-api.us-east-1.amazonaws.com/dev/search?q=otti&latitude=5&longitude=7``` | 

### Donde:
_q: Nombre de la ciudad a buscar_

_latitude: latitud a buscar_

_longitude: longitud a buscar_

### Response
```
{
    "search": [
        {
            "name": "Big Eddy",
            "latitude": "51",
            "longitude": "-118.21667",
            "score": 2.0
        },
        {
            "name": "Big Creek National Wildlife Area",
            "latitude": "42.5834",
            "longitude": "-118.21667",
            "score": 1.0
        },
    ]
}
```  

## Tecnolog铆as utilizadas e infraestructura 馃攳
### AWS
Se utilizan servicios de la nube para la soluci贸n:
- Lambda: C贸digo en la nube, contiene la l贸gica de la API
- API Gateway: Expone un endpoint final
- Elasticsearch (OpenSearch): Guarda la informaci贸n en formato json
- S3: Almacena el c贸digo del Lambda creado
- CloudFormation: Ejecuta los procesos necesarios para crear el lambda (Orquestado por Serverless Framework)
- IAM: Roles y permisos para cada servicio

### Serverless Framework
Framework utilizado para la creaci贸n de algunos servicios de AWS

A continuaci贸n se muestra diagrama con la funcionalidad:

![Diagrama_API](https://user-images.githubusercontent.com/101559613/158156716-52bde859-4546-44d8-8b34-19c740b6b1b7.png)


### APIS Elasticsearch
El servicio de Elastisearch no permite gestionar desde el tipo de datos a guardar hasta la forma en c贸mo son consultados, los principales m茅todos para la creaci贸n de 铆ndices, creaci贸n de documentos, obtener b煤squedas, etc. listados a continuaci贸n

CREAR 脥NDICE
| M茅todo | Endpoint/Request | 
| --- | --- | 
| PUT | ```https://{elasticsearch_endpoint}/{index_name}``` | 

CREAR DOCUMENTO
| M茅todo | Endpoint/Request | 
| --- | --- | 
| PUT | ```https://{elasticsearch_endpoint}/{index_name}/{type}/{id}``` | 

BORRAR 脥NDICE
| M茅todo | Endpoint/Request | 
| --- | --- | 
| DEL | ```https://{elasticsearch_endpoint}/{index_name}``` | 

BUSCAR DOCUMENTOS
| M茅todo | Endpoint/Request | 
| --- | --- | 
| GET | ```https://{elasticsearch_endpoint}/{index_name}/{type}/_search``` | 

Response:

```
{
    "query": {
        "bool": {
            "should": [
                {
                    "wildcard": {
                        "name": "otter*"
                    }
                },
                {
                    "wildcard": {
                        "latitude": "48"
                    }
                },
                {
                    "wildcard": {
                        "longitude": "-72"
                    }
                }
            ]
        }
    },
    "sort": {
        "name": {
            "order": "asc"
        },
        "_score": {
            "order": "desc"
        }
    },
    "from": 0,
    "size": 15
}
```

En la carpeta ra铆z se encuentra una collecci贸n de postman que contiene las principales operaciones a los documentos de Elasticsearch:
_Elasticsearch.postman_collection.json_

### Mejoras a cosiderar
- El uso de alarmas en AWS Cloudwatch para monitorear el correcto funcionamiento de la API.
- En API Gateway, utilizar el apartado de _Documentaci贸n_ para cada API creada.
- Desde archivo .yml de serverless crear el endpoint de Elasticsearch.
- En Elasticsearch, utilizar una instancia con mayor capacidad para una respuesta m谩s eficiente.
- Agregar desde API Gateway, un paso de autenticaci贸n para consultar la API creada.
- Query de eslasticsearch, investigar respecto al score autom谩tico asignado por la misma herramienta y adem谩s investigar m谩s a fondo los tipos de querys posibles.


### Accesos para visualizar los servicios creados
_Permisos limitados a s贸lo lectura_

Url consola: https://351551922524.signin.aws.amazon.com/console

user: invitado_kperez

password: TestInvitado#

### Autora
- Karla Itzel P茅rez Reyes 
