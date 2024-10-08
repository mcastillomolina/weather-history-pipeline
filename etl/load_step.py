import os
import logging
import mysql.connector

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_connection(config):

    try:
        connection = mysql.connector.connect(
            user=config['user'],
            password=config['password'],
            host=config['host'],
            database=config['database']
        )
    except mysql.connector.Error as err:
        raise err
    
    return connection

def load_step(data):
    '''
    Loads records into weather historical table
    '''
    if not data:
        raise ValueError('No data to load')
    connection_config = {
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'host': os.getenv('MYSQL_HOST'),
        'database': os.getenv('MYSQL_DATABASE')
    }

    connection = get_connection(connection_config)
    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS weather_historical (
        station_id VARCHAR(10) NOT NULL,
        station_name VARCHAR(255),
        station_timezone VARCHAR(255),
        latitude DECIMAL(10, 8),
        longitude DECIMAL(11, 8),
        obs_timestamp DATETIME,
        temperature DECIMAL(5, 2),
        wind_speed DECIMAL(5, 2),
        humidity DECIMAL(5, 2),
        PRIMARY KEY (station_id, obs_timestamp)
    )
    ''' 

    cursor.execute(create_table_query)
    logging.info('Created weather_historical table')

    upsert_query = '''
    INSERT INTO weather_historical (station_id, station_name, station_timezone, latitude, longitude, obs_timestamp, temperature, wind_speed, humidity)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    station_name=VALUES(station_name),
    station_timezone=VALUES(station_timezone),
    latitude=VALUES(latitude),
    longitude=VALUES(longitude),
    obs_timestamp=VALUES(obs_timestamp),
    temperature=VALUES(temperature),
    wind_speed=VALUES(wind_speed),
    humidity=VALUES(humidity)
    '''

    try:
        cursor.executemany(upsert_query, data)
        connection.commit()
        logging.info(f'Loaded {cursor.rowcount} records into weather_historical table')
    except mysql.connector.Error as err:
        logging.error(f'Error loading data: {err}')
        connection.rollback()
        raise err
    finally:
        cursor.close()
        connection.close()



