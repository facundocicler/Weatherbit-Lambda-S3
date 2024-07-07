import requests

def get_weather_data(api_key, lat, lon):
    try:
        url = f'https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={api_key}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for lat: {lat}, lon: {lon} - {e}")
        return None

def get_weather_data_multiple(api_key, locations):
    data = []
    for loc in locations:
        city = loc['city']
        lat = loc['lat']
        lon = loc['lon']
        weather_data = get_weather_data(api_key, lat, lon)
        if weather_data and 'data' in weather_data:
            weather_info = weather_data['data'][0]
            data.append({
                'city': city,
                'area': loc['area'],
                'temp': weather_info['temp'],
                'description': weather_info['weather']['description'],
                'humidity': weather_info['rh'],
                'wind_speed': weather_info['wind_spd'],
                'feels_like': weather_info['app_temp'],
                'pressure': weather_info['pres'],
                'visibility': weather_info['vis'],
                'dew_point': weather_info['dewpt'],
                'uv_index': weather_info['uv'],
                'precipitation': weather_info['precip'],
                'ob_time': weather_info['ob_time']
            })
    return data
