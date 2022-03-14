### kperezr-test-gmodelo

# API search
API que permite el filtrado y búsqueda de información basada en los datos de "https://download.geonames.org/"

### Pre-requisitos 📋
Contar con algun agente que nos permita hacer peticiones HTTPS. _Se sugiere el uso de postman._

### Detalles técnicos de la API ⚙️

| Método | Endpoint/Request | 
| --- | --- | 
| GET | ```https://kvufjplkf4.execute-api.us-east-1.amazonaws.com/dev/search?q="big e"&latitude="5"&longitude="7"``` | 

### Donde:
_q: Nombre de la ciudad a buscar_

_latitude: latitud a buscar_

_longitude: longitude a buscar_

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
            "score": 1.0
        },
    ]
}
```  

## Tecnologías utilizadas e infraestructura 🔍
### AWS
Se utilizan servicios de la nube para la solución:
- Lambda: Código en la nube, contiene la lógica de la API
- API Gateway: Expone un endpoint final
- Elasticsearch (OpenSearch): Guarda la información en formato json
- S3: Almacena el código del Lambda creado
- CloudFormation: Ejecuta los procesos necesarios para crear el lambda (Orquestado por Serverless Framework)
- IAM: Roles y permisos para cada servicio

### Serverless Framework
Framework utilizado para la creación de algunos servicios de AWS

A continuación se muestra diagrama con la funcionalidad:

![Diagrama_API](https://user-images.githubusercontent.com/101559613/158156716-52bde859-4546-44d8-8b34-19c740b6b1b7.png)


### Mejoras a cosiderar
- El uso de alarmas en AWS Cloudwatch para monitorear el correcto funcionamiento de la API.
- En API Gateway, utilizar el apartado de _Documentación_ para cada API creada.
- Desde archivo .yml de serverless crear el endpoint de Elasticsearch.
- En Elasticsearch, utilizar una instancia con mayor capacidad para una respuesta más eficiente.
- Agregar desde API Gateway, un paso de autenticación para consultar la API creada.
- Query de eslasticsearch, investigar respecto al score automático asignado por la misma herramienta.


### Accesos para visualizar los servicios creados
_Permisos limitados a sólo lectura_

user: invitado_kperez

password: TestInvitado#

Url consola: https://351551922524.signin.aws.amazon.com/console


### Autora
- Karla Itzel Pérez Reyes 
