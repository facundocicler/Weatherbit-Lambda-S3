# Proyecto de Obtención de Datos Meteorológicos y Análisis con AWS

Este proyecto utiliza AWS Lambda, Docker, AWS Glue y AWS Athena para obtener datos meteorológicos de múltiples ubicaciones utilizando la API de Weatherbit, almacenarlos en un bucket de Amazon S3, cargarlos en una base de datos administrada por AWS Glue y realizar consultas utilizando AWS Athena.

## Configuración Inicial

### Usuario IAM y Configuración de AWS CLI

Antes de comenzar, asegúrate de tener configurado un usuario en AWS IAM con los siguientes permisos mínimos:

- `AmazonEC2ContainerRegistryFullAccess`: Acceso completo a Amazon ECR para crear repositorios, subir y gestionar imágenes de contenedor.

Configura AWS CLI con las credenciales de este usuario ejecutando:

```bash
aws configure
