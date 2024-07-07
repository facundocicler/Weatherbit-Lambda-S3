from datetime import datetime
import pytz

def convert_utc_to_buenos_aires(utc_time):
    try:
        utc_dt = datetime.strptime(utc_time, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            utc_dt = datetime.strptime(utc_time, '%Y-%m-%d %H:%M')
        except ValueError:
            return utc_time
        
    utc_dt = pytz.utc.localize(utc_dt) 
    buenos_aires_tz = pytz.timezone('America/Argentina/Buenos_Aires')
    buenos_aires_dt = utc_dt.astimezone(buenos_aires_tz)
    return buenos_aires_dt.strftime('%Y-%m-%d %H:%M:%S')

def get_current_time_buenos_aires():
    buenos_aires_tz = pytz.timezone('America/Argentina/Buenos_Aires')
    current_time_ba = datetime.now(buenos_aires_tz)
    return current_time_ba.strftime('%Y-%m-%d_%H-%M-%S')
