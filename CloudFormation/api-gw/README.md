## Documentación del Template de CloudFormation

Este template de CloudFormation crea una API RESTful en Amazon API Gateway que se integra con una función Lambda existente. El objetivo es exponer la función Lambda a través de un endpoint HTTP POST en la API Gateway, permitiendo que se invoque cuando se realicen solicitudes HTTP. Este template también configura los roles y permisos necesarios para que API Gateway pueda invocar la Lambda.

#### **Parámetros:**

- **LambdaFunction**: El ARN de la función Lambda que se integrará con la API Gateway. Este parámetro es obligatorio para configurar la integración.

#### **Recursos:**

1. **RestApiIMMUNE**:
   - Crea una API RESTful en Amazon API Gateway con el nombre `api-IMMUNE`.

2. **Method**:
   - Define un método HTTP POST en el recurso raíz de la API Gateway. La API no utiliza autenticación (`AuthorizationType: NONE`). Este método invoca la función Lambda proporcionada a través de la URI configurada, y el tipo de integración es `AWS` (invocación de la Lambda).

3. **ApiGatewayResource**:
   - Crea un recurso llamado `/lambda` dentro de la API RESTful. Este recurso es utilizado para mapear la invocación de la Lambda.

4. **ApiGatewayModel**:
   - Define un modelo de entrada y salida para el API, especificando que se utiliza el tipo de contenido `application/json`. Este modelo está asociado con la API.

5. **ApiGatewayStage**:
   - Crea una etapa de despliegue (`Stage`) para la API, con el nombre `v0`. La etapa está asociada con un despliegue que se realiza mediante `ApiGatewayDeployment`.

6. **ApiGatewayDeployment**:
   - Despliega la API y la asocia con la etapa `v0`. Este recurso depende de la configuración del método y los recursos de la API.

7. **ApiGatewayIamRole**:
   - Crea un rol IAM que le da a API Gateway permisos para invocar la Lambda. El rol también se configura con una política que permite todas las acciones de Lambda (`lambda:*`) sobre el recurso de la Lambda proporcionado.

8. **lambdaApiGatewayInvoke**:
   - Configura los permisos necesarios para que API Gateway pueda invocar la función Lambda mediante el recurso creado. Se asigna el permiso `lambda:InvokeFunction` a la Lambda, permitiendo que se ejecute cuando se realicen solicitudes POST en el endpoint configurado de la API.

#### **Permisos Generales:**

- **API Gateway Role Permissions**:
  - Se crea un rol IAM con permisos para que API Gateway pueda asumir el rol y ejecutar las acciones necesarias para invocar la Lambda. Los permisos incluyen la capacidad de ejecutar cualquier acción de Lambda sobre el recurso de la función proporcionada (a través de `lambda:*`).
  
- **Lambda Permissions**:
  - La función Lambda tiene habilitada la capacidad de ser invocada por API Gateway. Se le concede el permiso `lambda:InvokeFunction`, permitiendo que las solicitudes HTTP que lleguen al endpoint configurado invocan la Lambda.

#### **Monitoreo con CloudWatch**:

Aunque no se configura explícitamente en este template, API Gateway y Lambda automáticamente envían logs a **Amazon CloudWatch Logs**. Esto incluye:
- **Lambda Logs**: La salida de ejecución de la Lambda (tanto errores como respuestas) se registra en CloudWatch Logs.
- **API Gateway Logs**: Las solicitudes y respuestas a través de API Gateway también se registran en CloudWatch, lo que permite monitorizar las métricas de rendimiento y los errores de la API.
  
Para habilitar los logs en CloudWatch para API Gateway y Lambda, es posible que sea necesario habilitar configuraciones adicionales, como habilitar el registro de acceso y errores de API Gateway.

#### **Acceso al Bucket S3**:

Este template no configura acceso directo a S3, ya que está enfocado en integrar la función Lambda con API Gateway para invocaciones HTTP. Sin embargo, si la Lambda necesita acceder a recursos en S3, sería necesario agregar permisos adicionales al rol IAM de la Lambda.

#### **Salidas:**

- **RootResourceId**:
   - Exporta el `RootResourceId` de la API Gateway, que es útil para referenciar el recurso raíz de la API en otros templates o stacks. El nombre de la exportación está configurado para incluir el nombre del stack actual, lo que garantiza que sea único.

