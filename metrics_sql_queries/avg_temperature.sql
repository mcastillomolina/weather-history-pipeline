SELECT 
    AVG(temperature) AS avg_temperature
FROM 
    weather_historical
WHERE 
    station_id = '000PG' 
    AND obs_timestamp >= DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) + 7 DAY)
    AND obs_timestamp < DATE_SUB(CURDATE(), INTERVAL WEEKDAY(CURDATE()) DAY);