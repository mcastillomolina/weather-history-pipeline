import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform_step(station_data, observations_data, lookback_days=7):
    '''
    This function transforms the extracted data.
    It filters the observations data to keep only the relevant fields and seven days of data.
    It also adds the station data to the observations data.
    Will return prepared data to be inserted into the database. 
    '''
    if not station_data:
        raise ValueError('No station data provided')
    if not observations_data:
        raise ValueError('No observations data provided')

    station_id = station_data['stationIdentifier']
    station_name = station_data['name']
    station_timezone = station_data['timeZone']
    
    seven_days_ago = datetime.datetime.now() - datetime.timedelta(days=lookback_days)
    logging.info(f'Filtering observations from {seven_days_ago} to present')

    prep_data = []

    for obs in observations_data:
        properties = obs.get('properties', {})
        geometry = obs.get('geometry', {})
        obs_timestamp = properties['timestamp']
        if obs_timestamp < seven_days_ago.isoformat():
            # If observation older than seven days, skip
            continue

        obs_timestamp = datetime.datetime.fromisoformat(obs_timestamp)
        latitude = geometry['coordinates'][1]
        longitude = geometry['coordinates'][0]

        temp = properties['temperature'].get('value')
        temperature = round(temp, 2) if temp else None

        ws = properties['windSpeed'].get('value')
        wind_speed = round(ws, 2) if ws else None
        
        hum = properties['relativeHumidity'].get('value')
        humidity = round(hum, 2) if hum else None

        prep_data.append((station_id, station_name, station_timezone, latitude, longitude, obs_timestamp, temperature, wind_speed, humidity))

    logging.info(f'Prepared data for station {station_id}: {len(prep_data)} records')
    
    return prep_data

if __name__ == '__main__':
    from sample_data.sample_data_000PG import station_data, obs_data
    prepared_data = transform_step(station_data, obs_data)
    logging.info(f'Prepared data: {prepared_data[0]}')
    
