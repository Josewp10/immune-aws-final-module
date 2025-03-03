## Documentación del Template de CloudFormation

Este template de CloudFormation despliega una función AWS Lambda que se configura con un rol IAM asociado. Este rol tiene permisos para interactuar con varios servicios de AWS, tales como EC2, DynamoDB, CloudWatch y S3. Además, permite la creación de políticas para controlar el acceso de la Lambda a los recursos especificados.

La Lambda que se crea en este template está configurada para poder:
- Realizar operaciones en DynamoDB.
- Gestionar instancias y recursos de EC2.
- Registrar y visualizar logs en CloudWatch.
- Interactuar con un bucket de S3 para cargar y almacenar archivos.

#### **Parámetros:**
- **LambdaName**: El nombre asignado a la función Lambda.
- **LambdaRuntime**: El runtime que se usará para la Lambda (por ejemplo, `python3.8`, `nodejs14.x`).
- **LambdaBucket**: El nombre del bucket de S3 donde se encuentra el archivo `.zip` con el código de la Lambda.
- **ZipName**: El nombre del archivo `.zip` que contiene el código fuente de la Lambda.

#### **Recursos:**

1. **LambdaFunction**: 
   - Crea la función Lambda con los parámetros proporcionados, configurando el nombre, el runtime y el archivo de código desde S3. Además, se le asignan los permisos definidos en las políticas IAM asociadas.

2. **LambdaPolicyEC2**: 
   - Esta política proporciona a la Lambda permisos para interactuar con recursos de Amazon EC2. Los permisos incluyen acciones como iniciar, detener, crear y describir instancias EC2, entre otras operaciones en redes y subredes VPC, interfaces de red y más.

3. **LambdaPolicyDynamo**: 
   - Permite que la Lambda interactúe con DynamoDB, realizando operaciones de lectura, escritura y actualización de elementos en la tabla DynamoDB especificada. La Lambda tendrá acceso total (`dynamodb:*`) a los recursos de DynamoDB.

4. **LambdaPolicyCW**: 
   - Permite a la Lambda acceder a los recursos de monitoreo de CloudWatch, incluyendo la capacidad de escribir logs y realizar trazabilidad con AWS X-Ray. Además, proporciona acceso completo a CloudWatch Logs y métricas.

5. **LambdaPolicyS3**:
   - Proporciona a la Lambda permisos para acceder y gestionar objetos en S3. Esto incluye acciones como listar los buckets, acceder a los objetos dentro del bucket especificado, y realizar operaciones de escritura en S3.

6. **LambdaRole**:
   - Define un rol IAM que se asocia con la Lambda y le asigna las políticas previamente definidas. Este rol permite que la Lambda asuma los permisos necesarios para interactuar con EC2, DynamoDB, S3, CloudWatch, y X-Ray.

#### **Permisos a Nivel General:**

1. **EC2**:
   - La Lambda puede ejecutar acciones como `ec2:StartInstances`, `ec2:StopInstances`, `ec2:TerminateInstances`, `ec2:RunInstances`, entre otras. También puede modificar las interfaces de red, crear y asociar VPCs, gestionar rutas y subredes, entre otros.

2. **DynamoDB**:
   - Se otorgan permisos completos de lectura y escritura en DynamoDB, permitiendo a la Lambda ejecutar acciones como `dynamodb:PutItem`, `dynamodb:UpdateItem`, `dynamodb:GetItem`, y otros accesos relacionados.

3. **CloudWatch**:
   - La Lambda tiene acceso completo a los servicios de monitoreo de CloudWatch, lo que incluye la capacidad de escribir logs (`logs:*`), acceder a métricas (`cloudwatch:*`), y realizar trazabilidad de las funciones Lambda a través de X-Ray (`xray:*`).

4. **S3**:
   - La Lambda obtiene permisos de lectura y escritura sobre S3. Esto incluye poder listar los buckets (`s3:ListAllMyBuckets`), acceder a los objetos (`s3:ListObjects` y `s3:HeadBucket`), y realizar operaciones de escritura sobre los objetos del bucket (`s3:*`).

#### **Monitoreo con CloudWatch:**

- **Logs**: 
  - El servicio de CloudWatch Logs es utilizado para registrar los eventos de la Lambda. Cada vez que la Lambda es invocada, se generan logs detallados con la salida de la ejecución. Esto permite monitorear el comportamiento de la Lambda, identificar errores y tener una trazabilidad de su funcionamiento.

- **Métricas**:
  - CloudWatch también proporciona métricas sobre la ejecución de la Lambda, tales como el número de invocaciones, el tiempo de ejecución y la cantidad de memoria utilizada. Estas métricas son esenciales para detectar cuellos de botella y mejorar el rendimiento de la función Lambda.

- **Trazabilidad (X-Ray)**:
  - AWS X-Ray está habilitado para la función Lambda, lo que permite hacer un análisis de trazabilidad de las solicitudes que procesan las Lambdas, lo que facilita la identificación de errores y latencias en el flujo de ejecución de la aplicación.

#### **Acceso al Bucket S3:**

- **Lectura de Objetos**: 
  - La Lambda tiene permisos para listar y acceder a los objetos dentro de un bucket S3, lo que le permite leer datos almacenados en S3.

- **Escritura en el Bucket**: 
  - La Lambda también tiene permisos para realizar operaciones de escritura, lo que le permite cargar nuevos archivos o actualizar los existentes en el bucket de S3 especificado.

#### **Salidas:**
- **LambdaPolicyDynamo**: 
  - Exporta el ARN de la política de DynamoDB, que otorga los permisos necesarios para la Lambda interactuar con DynamoDB.
  
- **LambdaPolicyEC2**: 
  - Exporta el ARN de la política de EC2, que permite a la Lambda interactuar con recursos de EC2.

- **LambdaPolicyCW**: 
  - Exporta el ARN de la política de CloudWatch, que otorga acceso completo para escribir logs, acceder a métricas y realizar trazabilidad con X-Ray.

- **LambdaFunction**: 
  - Exporta el ARN de la función Lambda, para ser utilizado en otras partes de la infraestructura o como referencia en otros templates de CloudFormation.
