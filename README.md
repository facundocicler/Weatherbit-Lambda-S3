# Proyecto de Obtención de Datos Meteorológicos y Análisis con AWS

Este proyecto utiliza AWS Lambda, Docker, AWS Glue y AWS Athena para obtener datos meteorológicos de múltiples ubicaciones utilizando la API de Weatherbit, almacenarlos en un bucket de Amazon S3, cargarlos en una base de datos administrada por AWS Glue y realizar consultas utilizando AWS Athena.

## Configuración

### Variables de Entorno

Antes de comenzar, asegúrate de configurar las siguientes variables de entorno:

```bash
export WEATHERBIT_API_KEY='tu_clave_api_de_weatherbit'
export BUCKET_LOCATIONS='tu_bucket_de_ubicaciones_en_s3'
export FILE_LOCATIONS='ubicacion_del_archivo_en_el_bucket_de_ubicaciones'
export BUCKET_REGISTRY='tu_bucket_de_registro_en_s3'
export SNS_TOPIC_ARN='arn_del_tema_sns_para_notificaciones'
