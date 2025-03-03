# Función Lambda para Registro y Consulta de Estudiantes en DynamoDB

Este proyecto contiene una función AWS Lambda que interactúa con DynamoDB para registrar y consultar la información de los estudiantes del curso **DevOps & CloudComputing-2410**, utilizando el DNI como identificador único.

## Descripción

La función Lambda permite realizar dos operaciones principales sobre DynamoDB:

1. **Consultar un Estudiante**: Recupera los registros de un estudiante mediante su DNI.
2. **Registrar un Estudiante**: Almacena un nuevo registro de estudiante en DynamoDB, utilizando el DNI como clave primaria.

## Requisitos

- **AWS Lambda**: Para ejecutar la función de manera serverless.
- **DynamoDB**: Para almacenar los registros de los estudiantes.
  
Se debe configurar la variable de entorno `DYNAMO_IMMUNE` con el nombre de la tabla de DynamoDB.

## Funcionamiento

### Clase `DynamoAccessor`

- **`get_data_from_dynamo(dni)`**: Consulta DynamoDB para obtener el registro de un estudiante según su DNI.
- **`save_data_to_dynamo(dni, data)`**: Guarda un nuevo registro en DynamoDB, asegurándose de que el campo `dni` esté incluido en los datos.

### Función `lambda_handler`

- Si el evento contiene solo el campo `dni`, se realiza una consulta para recuperar el registro del estudiante.
- Si el evento contiene tanto `dni` como `data`, se guarda un nuevo registro en la base de datos.

### Variables de Entorno

- **`DYNAMO_IMMUNE`**: Nombre de la tabla de DynamoDB.

## Ejemplos

### 1. Consultar un Estudiante

Para consultar un estudiante utilizando su DNI, el evento debe tener el siguiente formato:

```json
{
  "dni": "12345678"
}
```

Esto hará que la función Lambda recupere el registro del estudiante con el DNI `12345678` de la base de datos DynamoDB.

### 2. Guardar un Estudiante

Para guardar un nuevo estudiante, el evento debe tener el siguiente formato:

```json
{
  "dni": "12345678",
  "data": {
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "telefono": "123-456-7890"
  }
}
```

Esto guardará un nuevo registro en DynamoDB con el DNI `12345678` y los datos asociados (nombre, correo electrónico y teléfono).

## Propósito

Este código está diseñado para gestionar los registros de los estudiantes del curso **DevOps & CloudComputing-2410**. Los estudiantes se registran utilizando su DNI y se pueden consultar posteriormente con el mismo identificador.

## Consideraciones

- La tabla DynamoDB debe tener el campo `dni` como clave primaria.
- La función Lambda debe tener permisos adecuados para acceder a DynamoDB.

