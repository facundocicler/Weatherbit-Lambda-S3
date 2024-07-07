# Proyecto de Obtención de Datos Meteorológicos y Análisis con AWS

Este proyecto utiliza AWS Lambda, Docker, AWS SNS, AWS Glue y AWS Athena para obtener datos meteorológicos de múltiples ubicaciones utilizando la API de Weatherbit, almacenarlos en un bucket de Amazon S3, cargarlos en una base de datos administrada por AWS Glue y realizar consultas utilizando AWS Athena.

## Requisitos
Para trabajar con este proyecto, asegúrate de tener instalado lo siguiente:
* Docker: Versión 19.03 o superior.
* Python: Versión 3.6 o superior.
* Acceso a AWS: Una cuenta de AWS con permisos para configurar servicios como Lambda, ECR, S3, etc.
* AWS CLI: Herramienta necesaria para configurar y gestionar servicios de AWS.

## Configuración Inicial

### Usuario IAM y Configuración de AWS CLI
1. Antes de comenzar, asegúrate de tener configurado un usuario en AWS IAM con los siguientes permisos mínimos:
   - `AmazonEC2ContainerRegistryFullAccess`: Acceso completo a Amazon ECR para crear repositorios, subir y gestionar imágenes de contenedor.

2. Configura AWS CLI con las credenciales de este usuario ejecutando:
```bash
aws configure
```

### Docker
1. Construye la imagen del contenedor Docker:
```bash
cd /mnt/path/to/project_directory
```
```bash
docker build -t your_image_name -f docker/Dockerfile .
```

2. Etiqueta y sube la imagen a AWS ECR:
```bash
aws ecr get-login-password --region your_region | docker login --username AWS --password-stdin your_account_id.dkr.ecr.your_region.amazonaws.com
```
```bash
docker tag your_image_name:latest your_account_id.dkr.ecr.your_region.amazonaws.com/your_repository_name:latest
```
```bash
docker push your_account_id.dkr.ecr.your_region.amazonaws.com/your_repository_name:latest
```

### Amazon S3
1. Crea dos buckets en Amazon S3:

   - **Bucket de Ubicaciones**: Utilizado para almacenar el archivo `locations.csv` y cualquier otro archivo relacionado con las ubicaciones.
   - **Bucket de Registro**: Utilizado para almacenar los archivos CSV generados por la función Lambda con los datos meteorológicos.

2. Sube el archivo `locations.csv` al bucket de ubicaciones en Amazon S3:

   - Accede al bucket de ubicaciones a través de la consola de AWS S3.
   - Haz clic en "Cargar" y selecciona el archivo `locations.csv` desde tu sistema local.

### AWS Lambda
1. Crea un rol IAM para la función Lambda:
   - Crea un nuevo rol IAM en la consola de IAM de AWS.
   - Asigna la política `AWSLambdaBasicExecutionRole` para permitir a la función Lambda escribir registros en CloudWatch Logs.
   - Asigna políticas adicionales según sea necesario, como acceso a S3, SNS, etc.

2. Crea una función Lambda en la consola de AWS Lambda:
   - Nombre de la función: Especifica un nombre para tu función Lambda.
   - Entorno de ejecución: Selecciona Use container image y especifica la imagen que subiste a AWS ECR.
   - Rol de ejecución: Selecciona el rol IAM que creaste anteriormente con los permisos necesarios.

3. Configura las variables de entorno en la función Lambda:
   - Después de crear la función Lambda, configura las siguientes variables de entorno en la consola de AWS Lambda:
     ```bash
     WEATHERBIT_API_KEY: Tu clave API de Weatherbit.
     BUCKET_LOCATIONS: Nombre de tu bucket de S3 para ubicaciones.
     FILE_LOCATIONS: Ruta del archivo en el bucket de ubicaciones.
     BUCKET_REGISTRY: Nombre de tu bucket de S3 para registro.
     SNS_TOPIC_ARN: ARN del tema SNS para notificaciones.
     ```
     
### AWS Glue y Athena
1. Configura AWS Glue para cargar datos desde S3:
- Crea una base de datos y tablas en AWS Glue para almacenar los datos meteorológicos.
- Define un Crawler en AWS Glue para descubrir y cargar los datos desde el bucket BUCKET_REGISTRY.

2. Configura AWS Athena para realizar consultas:
- Crea tablas externas en AWS Athena para consultar los datos almacenados en AWS Glue.
- Ejecuta consultas SQL en AWS Athena para analizar los datos meteorológicos almacenados.



            
