CREATE TABLE IF NOT EXISTS weather_data (
    station_id VARCHAR(10) NOT NULL,
    station_name VARCHAR(255),
    timezone VARCHAR(50),
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6),
    observation_timestamp DATETIME NOT NULL,
    temperature DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    wind_speed DECIMAL(5, 2),
    etl_update_timestamp DATETIME,
    PRIMARY KEY (station_id, observation_timestamp)
);