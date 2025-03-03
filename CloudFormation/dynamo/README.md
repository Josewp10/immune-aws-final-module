### Documentación del Template de CloudFormation

Este template de CloudFormation crea una tabla en DynamoDB con una clave primaria especificada por el parámetro `DynamoKey` y un nombre de tabla determinado por el parámetro `DynamoName`. La tabla se configura con facturación por demanda (`PAY_PER_REQUEST`) y con cifrado de datos habilitado.

#### Parámetros:
- **DynamoName**: El nombre de la tabla DynamoDB que se va a crear.
- **DynamoKey**: El nombre de la clave primaria que se utilizará en la tabla.

#### Recursos:
- **DynamoPlatzi** (cambiado a **DynamoIMMUNE**): Una tabla DynamoDB que se configura con la clave primaria especificada, y habilita el cifrado de datos en reposo.

#### Salidas:
- **DynamoPlatzi**: El nombre de la tabla creada, exportado con el nombre del stack.
- **DynamoPlatziArn**: El ARN de la tabla creada, exportado con el nombre del stack.

