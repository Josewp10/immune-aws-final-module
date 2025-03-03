### Documentación del Template de CloudFormation

Esta plantilla de **AWS CloudFormation** está diseñada para crear un **bucket de S3** con configuraciones específicas para **cifrado**, **controles de propiedad**, **versionado** y **configuraciones de acceso público**. Además, incluye una **Política de Bucket** que permite el acceso público de solo lectura a los objetos almacenados en el bucket.

## Características de la Plantilla

- **Creación del Bucket**: Crea un bucket de S3 con el nombre y la configuración especificados.
- **Cifrado**: El bucket está configurado para usar **cifrado del lado del servidor AES-256** para todos los objetos almacenados.
- **Controles de Propiedad**: Permite configurar el modelo de propiedad del bucket (puede ser `BucketOwnerPreferred`, `ObjectWriter` o `BucketOwnerEnforced`).
- **Versionado**: La plantilla permite habilitar o suspender el versionado para el bucket.
- **Alojamiento de Sitios Web**: Configura el bucket para servir un documento `index.html` para el alojamiento de sitios web estáticos.
- **Acceso Público**: La plantilla no bloquea el acceso público, permitiendo que los objetos sean accesibles públicamente a través de sus URLs.
- **Política de Bucket**: Se aplica una política al bucket que otorga **acceso público de solo lectura** a los objetos dentro del bucket.

## Parámetros

- **bucketName** (String): El nombre del bucket de S3 que se creará.
- **ownershipControls** (String): Define el modelo de propiedad de los objetos. Puede ser uno de los siguientes:
  - `BucketOwnerPreferred` (valor predeterminado)
  - `ObjectWriter`
  - `BucketOwnerEnforced`
- **versioning** (String): Especifica si el versionado está habilitado o suspendido para el bucket. Valores permitidos:
  - `Enabled` (valor predeterminado)
  - `Suspended`

## Recursos Creado

1. **S3 Bucket**:
   - El bucket se creará con el nombre y las configuraciones especificadas:
     - **Cifrado**: Habilitado con cifrado AES-256.
     - **Controles de Propiedad**: Configurados según el parámetro proporcionado.
     - **Versionado**: Configurado según el parámetro proporcionado (ya sea habilitado o suspendido).
     - **Alojamiento de Sitio Web**: Se configura `index.html` como el documento principal para el alojamiento de un sitio web estático.
     - **Bloqueo de Acceso Público**: El acceso público no está bloqueado, permitiendo el acceso público a los objetos.

2. **Política de Bucket**:
   - Se aplica una política de bucket para permitir el acceso público de solo lectura (`s3:GetObject`) a todos los objetos dentro del bucket.

## Salidas

- **S3DomainName**: El nombre de dominio del bucket de S3 creado (por ejemplo, `nombre-del-bucket.s3.amazonaws.com`).
- **BucketName**: El nombre del bucket de S3 creado.
