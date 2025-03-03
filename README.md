# Documentación del Proyecto

## Descripción General
Este proyecto implementa una arquitectura en AWS utilizando CloudFormation para desplegar una aplicación web estática con integración a DynamoDB a través de una función Lambda y API Gateway.

## Arquitectura
El proyecto está compuesto por los siguientes servicios de AWS:

- **Amazon S3**: Aloja una página web estática.
- **Amazon DynamoDB**: Base de datos NoSQL para almacenamiento de datos.
- **AWS Lambda**: Funciones serverless que interactúan con DynamoDB.
- **Amazon API Gateway**: Expone la función Lambda como un servicio web accesible.

### Diagrama de Arquitectura



## Estructura del Repositorio
El código del proyecto se organiza en la siguiente estructura:

```
--- web/             # Contiene el index.html del sitio web
--- function/        # Contiene el código de la función Lambda
--- CloudFormation/  # Plantillas de CloudFormation
    --- api-gw/      # Definiciones para API Gateway
    --- dynamo/      # Definiciones para DynamoDB
    --- S3/          # Definiciones para S3
    --- Lambda/      # Definiciones para Lambda
    --- master.yml   # Plantilla principal para nested stacks
```

## Justificación del Diseño
Se han seleccionado estos servicios por las siguientes razones:

- **S3**: Permite alojar la página web de forma económica y escalable.
- **DynamoDB**: Ofrece alta disponibilidad y escalabilidad automática para almacenamiento de datos.
- **Lambda**: Permite procesar peticiones sin necesidad de gestionar servidores.
- **API Gateway**: Facilita la exposición de la función Lambda como una API REST.

## Pasos de Despliegue
1. Subir las plantillas de CloudFormation al bucket S3 `jdmo-immune-cloudformation-templates`. Este se usa como punto central para las plantillas, lo que facilita su llamado desde CloudFormation como nested stacks.
2. Subir el código de la función Lambda al bucket S3 de demo.
3. Desplegar la plantilla principal (`master.yml`) a través de AWS CloudFormation.
4. Acceder a la página web en S3 y probar la API.

## Buenas Prácticas Implementadas
- **Seguridad**: Uso de permisos IAM restrictivos para Lambda y DynamoDB.
- **Gestín de credenciales**: Uso de AWS IAM en lugar de credenciales embebidas.
- **Escalabilidad**: Uso de servicios serverless y almacenamiento dinámico.
- **Costos optimizados**: Uso de S3 para hosting web y Lambda para cálculo sin servidores.

## Demostración de Funcionamiento


