import json
import pandas as pd
from io import StringIO
from config import API_KEY, BUCKET_LOCATIONS, FILE_LOCATIONS, BUCKET_REGISTRY, SNS_TOPIC_ARN
from weatherbit_client import get_weather_data_multiple
from utils import convert_utc_to_buenos_aires, get_current_time_buenos_aires
from s3_client import download_csv_from_s3, upload_csv_to_s3
from sns_client import send_sns_notification

def lambda_handler(event, context):
    try:
        # Descarga el archivo CSV desde S3
        locations_csv = download_csv_from_s3(BUCKET_LOCATIONS, FILE_LOCATIONS)
        
        # Lee el archivo CSV usando pandas desde el flujo de bytes
        locations_df = pd.read_csv(StringIO(locations_csv))
        
        # Convierte DataFrame a lista de diccionarios
        locations = locations_df.to_dict(orient='records')
        
        # Obtiene los datos para todas las ubicaciones
        data_all = get_weather_data_multiple(API_KEY, locations)
        
        # Crea DataFrame
        df = pd.DataFrame(data_all)
        
        # Verifica y convierte la columna 'ob_time' si es necesario
        if 'ob_time' in df.columns and pd.api.types.is_string_dtype(df['ob_time']):
            df['ob_time'] = df['ob_time'].apply(lambda x: convert_utc_to_buenos_aires(x))
        
        # Obtiene la hora actual en Buenos Aires
        current_time_str = get_current_time_buenos_aires()
        
        # Genera nombre de archivo con la fecha y hora actual de Buenos Aires
        file_key_output = f'weather_data_{current_time_str}.csv'
        
        # Convierte el DataFrame a formato CSV
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, encoding='utf-8-sig', index=False)
        
        # Guarda el DataFrame en un bucket S3
        try:
            upload_csv_to_s3(BUCKET_REGISTRY, file_key_output, csv_buffer.getvalue())
            
            # Enviar notificación a través de SNS solo si se guarda con éxito en S3
            message = f'Se ha guardado un nuevo archivo CSV en el bucket S3: {file_key_output}'
            subject = 'Notificación de AWS Lambda: Guardado de CSV completado'
            send_sns_notification(SNS_TOPIC_ARN, message, subject)
        
        except Exception as s3_error:
            print(f"Error uploading to S3: {s3_error}")
            return {
                'statusCode': 500,
                'body': json.dumps('Error uploading to S3')
            }

        return {
            'statusCode': 200,
            'body': json.dumps('Datos guardados en S3 y notificación enviada correctamente')
        }
    
    except Exception as e:
        print(f"Error in lambda_handler: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing request')
        }
