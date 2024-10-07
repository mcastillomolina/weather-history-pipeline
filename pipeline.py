from etl.extract_step import extract_step
from etl.transform_step import transform_step
from etl.load_step import load_step
import logging
import os

log_level = os.getenv('LOG_LEVEL', 'INFO').upper()

logging.basicConfig(level=getattr(logging, log_level), format='%(asctime)s - %(levelname)s - %(message)s')

if os.getenv('WEATHER_API_URL'):
    api_url = os.getenv('WEATHER_API_URL')
else:
    api_url = 'https://api.weather.gov'

if os.getenv('STATION_ID'):
    station_id = os.getenv('STATION_ID')
else:    
    station_id = '000PG'

station_data, observations_data = extract_step(api_url, station_id)
prepared_data = transform_step(station_data, observations_data)
load_step(prepared_data)
