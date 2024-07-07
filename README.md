# Proyecto de Obtención de Datos Meteorológicos y Análisis con AWS

Este proyecto utiliza AWS Lambda, Docker, AWS Glue y AWS Athena para obtener datos meteorológicos de múltiples ubicaciones utilizando la API de Weatherbit, almacenarlos en un bucket de Amazon S3, cargarlos en una base de datos administrada por AWS Glue y realizar consultas utilizando AWS Athena.

## Configuración Inicial

### Usuario IAM y Configuración de AWS CLI

Antes de comenzar, asegúrate de tener configurado un usuario en AWS IAM con los siguientes permisos mínimos:

- `AmazonEC2ContainerRegistryFullAccess`: Acceso completo a Amazon ECR para crear repositorios, subir y gestionar imágenes de contenedor.

Configura AWS CLI con las credenciales de este usuario ejecutando:

```bash
aws configure
```

### Docker
Construye la imagen del contenedor Docker:
```bash
docker build -t nombre_de_tu_imagen .
```
Etiqueta y sube la imagen a AWS ECR:
```bash
aws ecr get-login-password --region tu_region | docker login --username AWS --password-stdin tu_id_de_cuenta.dkr.ecr.tu_region.amazonaws.com
```
```bash
docker tag nombre_de_tu_imagen:latest tu_id_de_cuenta.dkr.ecr.tu_region.amazonaws.com/nombre_de_tu_repositorio:latest
```
```bash
docker push tu_id_de_cuenta.dkr.ecr.tu_region.amazonaws.com/nombre_de_tu_repositorio:latest
```

### AWS Lambda

Crea un rol IAM para la función Lambda:
- Crea un nuevo rol IAM en la consola de IAM de AWS.
- Asigna la política `AWSLambdaBasicExecutionRole` para permitir a la función Lambda escribir registros en CloudWatch Logs.
- Asigna políticas adicionales según sea necesario, como acceso a S3, SNS, etc.

Crea una función Lambda en la consola de AWS Lambda:
- Nombre de la función: Especifica un nombre para tu función Lambda.
- Entorno de ejecución: Selecciona Use container image y especifica la imagen que subiste a AWS ECR.
- Rol de ejecución: Selecciona el rol IAM que creaste anteriormente con los permisos necesarios.

Configura las variables de entorno en la función Lambda:
- Después de crear la función Lambda, configura las siguientes variables de entorno en la consola de AWS Lambda:
```bash
WEATHERBIT_API_KEY: Tu clave API de Weatherbit.
BUCKET_LOCATIONS: Nombre de tu bucket de S3 para ubicaciones.
FILE_LOCATIONS: Ruta del archivo en el bucket de ubicaciones.
BUCKET_REGISTRY: Nombre de tu bucket de S3 para registro.
SNS_TOPIC_ARN: ARN del tema SNS para notificaciones.
```




            
