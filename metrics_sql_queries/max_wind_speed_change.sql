WITH prev_wind_speeds AS (
   SELECT 
    wind_speed,
    LAG(wind_speed) OVER (PARTITION BY station_id ORDER BY obs_timestamp) as prev_wind_speed
FROM 
    weather_historical wh 
WHERE 
    station_id = '000PG'
    AND obs_timestamp >= DATE_SUB(NOW(), INTERVAL 7 DAY)
    )
    SELECT 
    	MAX(wind_speed - prev_wind_speed)
    FROM prev_wind_speeds
    ;