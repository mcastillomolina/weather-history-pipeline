station_data = {'@id': 'https://api.weather.gov/stations/000PG',
                '@type': 'wx:ObservationStation', 
                'elevation': {'unitCode': 'wmoUnit:m', 'value': 129.2352}, 
                'stationIdentifier': '000PG', 
                'name': 'Southside Road', 
                'timeZone': 'America/Los_Angeles', 
                'forecast': 'https://api.weather.gov/zones/forecast/CAZ528', 
                'county': 'https://api.weather.gov/zones/county/CAC069', 
                'fireWeatherZone': 'https://api.weather.gov/zones/fire/CAZ528'
                }

obs_data = [
{'id': 'https://api.weather.gov/stations/000PG/observations/2024-10-06T20:40:00+00:00',
  'type': 'Feature',
  'geometry': {'type': 'Point', 'coordinates': [-121.34, 36.79]},
  'properties': {'@id': 'https://api.weather.gov/stations/000PG/observations/2024-10-06T20:40:00+00:00',
   '@type': 'wx:ObservationStation',
   'elevation': {'unitCode': 'wmoUnit:m', 'value': 129.2},
   'station': 'https://api.weather.gov/stations/000PG',
   'timestamp': '2024-10-06T20:40:00+00:00',
   'rawMessage': '',
   'textDescription': '',
   'icon': None,
   'presentWeather': [],
   'temperature': {'unitCode': 'wmoUnit:degC',
    'value': 35.5,
    'qualityControl': 'V'},
   'dewpoint': {'unitCode': 'wmoUnit:degC',
    'value': 9.63,
    'qualityControl': 'V'},
   'windDirection': {'unitCode': 'wmoUnit:degree_(angle)',
    'value': 295.7,
    'qualityControl': 'V'},
   'windSpeed': {'unitCode': 'wmoUnit:km_h-1',
    'value': 6.012,
    'qualityControl': 'V'},
   'windGust': {'unitCode': 'wmoUnit:km_h-1',
    'value': None,
    'qualityControl': 'Z'},
   'barometricPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'seaLevelPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'visibility': {'unitCode': 'wmoUnit:m',
    'value': None,
    'qualityControl': 'Z'},
   'maxTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'minTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'precipitationLast3Hours': {'unitCode': 'wmoUnit:mm',
    'value': None,
    'qualityControl': 'Z'},
   'relativeHumidity': {'unitCode': 'wmoUnit:percent',
    'value': 20.709652001795,
    'qualityControl': 'V'},
   'windChill': {'unitCode': 'wmoUnit:degC',
    'value': None,
    'qualityControl': 'V'},
   'heatIndex': {'unitCode': 'wmoUnit:degC',
    'value': 33.70536336424278,
    'qualityControl': 'V'},
   'cloudLayers': []}},
 {'id': 'https://api.weather.gov/stations/000PG/observations/2024-10-06T20:30:00+00:00',
  'type': 'Feature',
  'geometry': {'type': 'Point', 'coordinates': [-121.34, 36.79]},
  'properties': {'@id': 'https://api.weather.gov/stations/000PG/observations/2024-10-06T20:30:00+00:00',
   '@type': 'wx:ObservationStation',
   'elevation': {'unitCode': 'wmoUnit:m', 'value': 129.2},
   'station': 'https://api.weather.gov/stations/000PG',
   'timestamp': '2024-10-06T20:30:00+00:00',
   'rawMessage': '',
   'textDescription': '',
   'icon': None,
   'presentWeather': [],
   'temperature': {'unitCode': 'wmoUnit:degC',
    'value': 35.44,
    'qualityControl': 'V'},
   'dewpoint': {'unitCode': 'wmoUnit:degC',
    'value': 8.99,
    'qualityControl': 'V'},
   'windDirection': {'unitCode': 'wmoUnit:degree_(angle)',
    'value': 296.5,
    'qualityControl': 'V'},
   'windSpeed': {'unitCode': 'wmoUnit:km_h-1',
    'value': 5.4,
    'qualityControl': 'V'},
   'windGust': {'unitCode': 'wmoUnit:km_h-1',
    'value': None,
    'qualityControl': 'Z'},
   'barometricPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'seaLevelPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'visibility': {'unitCode': 'wmoUnit:m',
    'value': None,
    'qualityControl': 'Z'},
   'maxTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'minTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'precipitationLast3Hours': {'unitCode': 'wmoUnit:mm',
    'value': None,
    'qualityControl': 'Z'},
   'relativeHumidity': {'unitCode': 'wmoUnit:percent',
    'value': 19.902841710907,
    'qualityControl': 'V'},
   'windChill': {'unitCode': 'wmoUnit:degC',
    'value': None,
    'qualityControl': 'V'},
   'heatIndex': {'unitCode': 'wmoUnit:degC',
    'value': 33.52862836205778,
    'qualityControl': 'V'},
   'cloudLayers': []}},
 {'id': 'https://api.weather.gov/stations/000PG/observations/2024-10-06T20:00:00+00:00',
  'type': 'Feature',
  'geometry': {'type': 'Point', 'coordinates': [-121.34, 36.79]},
  'properties': {'@id': 'https://api.weather.gov/stations/000PG/observations/2024-10-06T20:00:00+00:00',
   '@type': 'wx:ObservationStation',
   'elevation': {'unitCode': 'wmoUnit:m', 'value': 129.2},
   'station': 'https://api.weather.gov/stations/000PG',
   'timestamp': '2024-10-06T20:00:00+00:00',
   'rawMessage': '',
   'textDescription': '',
   'icon': None,
   'presentWeather': [],
   'temperature': {'unitCode': 'wmoUnit:degC',
    'value': 34.56,
    'qualityControl': 'V'},
   'dewpoint': {'unitCode': 'wmoUnit:degC',
    'value': 9.12,
    'qualityControl': 'V'},
   'windDirection': {'unitCode': 'wmoUnit:degree_(angle)',
    'value': 303.4,
    'qualityControl': 'V'},
   'windSpeed': {'unitCode': 'wmoUnit:km_h-1',
    'value': 6.66,
    'qualityControl': 'V'},
   'windGust': {'unitCode': 'wmoUnit:km_h-1',
    'value': None,
    'qualityControl': 'Z'},
   'barometricPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'seaLevelPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'visibility': {'unitCode': 'wmoUnit:m',
    'value': None,
    'qualityControl': 'Z'},
   'maxTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'minTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'precipitationLast3Hours': {'unitCode': 'wmoUnit:mm',
    'value': None,
    'qualityControl': 'Z'},
   'relativeHumidity': {'unitCode': 'wmoUnit:percent',
    'value': 21.081297772034,
    'qualityControl': 'V'},
   'windChill': {'unitCode': 'wmoUnit:degC',
    'value': None,
    'qualityControl': 'V'},
   'heatIndex': {'unitCode': 'wmoUnit:degC',
    'value': 32.679879512050555,
    'qualityControl': 'V'},
   'cloudLayers': []}},
 {'id': 'https://api.weather.gov/stations/000PG/observations/2024-10-06T19:10:00+00:00',
  'type': 'Feature',
  'geometry': {'type': 'Point', 'coordinates': [-121.34, 36.79]},
  'properties': {'@id': 'https://api.weather.gov/stations/000PG/observations/2024-10-06T19:10:00+00:00',
   '@type': 'wx:ObservationStation',
   'elevation': {'unitCode': 'wmoUnit:m', 'value': 129.2},
   'station': 'https://api.weather.gov/stations/000PG',
   'timestamp': '2024-10-06T19:10:00+00:00',
   'rawMessage': '',
   'textDescription': '',
   'icon': None,
   'presentWeather': [],
   'temperature': {'unitCode': 'wmoUnit:degC',
    'value': 32.72,
    'qualityControl': 'V'},
   'dewpoint': {'unitCode': 'wmoUnit:degC',
    'value': 8.54,
    'qualityControl': 'V'},
   'windDirection': {'unitCode': 'wmoUnit:degree_(angle)',
    'value': 297.4,
    'qualityControl': 'V'},
   'windSpeed': {'unitCode': 'wmoUnit:km_h-1',
    'value': 4.464,
    'qualityControl': 'V'},
   'windGust': {'unitCode': 'wmoUnit:km_h-1',
    'value': None,
    'qualityControl': 'Z'},
   'barometricPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'seaLevelPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'visibility': {'unitCode': 'wmoUnit:m',
    'value': None,
    'qualityControl': 'Z'},
   'maxTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'minTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'precipitationLast3Hours': {'unitCode': 'wmoUnit:mm',
    'value': None,
    'qualityControl': 'Z'},
   'relativeHumidity': {'unitCode': 'wmoUnit:percent',
    'value': 22.470064999601,
    'qualityControl': 'V'},
   'windChill': {'unitCode': 'wmoUnit:degC',
    'value': None,
    'qualityControl': 'V'},
   'heatIndex': {'unitCode': 'wmoUnit:degC',
    'value': 30.844986439919445,
    'qualityControl': 'V'},
   'cloudLayers': []}},
{'id': 'https://api.weather.gov/stations/000PG/observations/2024-09-29T21:10:00+00:00',
  'type': 'Feature',
  'geometry': {'type': 'Point', 'coordinates': [-121.34, 36.79]},
  'properties': {'@id': 'https://api.weather.gov/stations/000PG/observations/2024-09-29T21:10:00+00:00',
   '@type': 'wx:ObservationStation',
   'elevation': {'unitCode': 'wmoUnit:m', 'value': 129.2},
   'station': 'https://api.weather.gov/stations/000PG',
   'timestamp': '2024-09-29T21:10:00+00:00',
   'rawMessage': '',
   'textDescription': '',
   'icon': None,
   'presentWeather': [],
   'temperature': {'unitCode': 'wmoUnit:degC',
    'value': 22.49,
    'qualityControl': 'V'},
   'dewpoint': {'unitCode': 'wmoUnit:degC',
    'value': 13.57,
    'qualityControl': 'V'},
   'windDirection': {'unitCode': 'wmoUnit:degree_(angle)',
    'value': 284.9,
    'qualityControl': 'V'},
   'windSpeed': {'unitCode': 'wmoUnit:km_h-1',
    'value': 8.064,
    'qualityControl': 'V'},
   'windGust': {'unitCode': 'wmoUnit:km_h-1',
    'value': None,
    'qualityControl': 'Z'},
   'barometricPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'seaLevelPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'visibility': {'unitCode': 'wmoUnit:m',
    'value': None,
    'qualityControl': 'Z'},
   'maxTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'minTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'precipitationLast3Hours': {'unitCode': 'wmoUnit:mm',
    'value': None,
    'qualityControl': 'Z'},
   'relativeHumidity': {'unitCode': 'wmoUnit:percent',
    'value': 57.076955496107,
    'qualityControl': 'V'},
   'windChill': {'unitCode': 'wmoUnit:degC',
    'value': None,
    'qualityControl': 'V'},
   'heatIndex': {'unitCode': 'wmoUnit:degC',
    'value': 22.284898282398334,
    'qualityControl': 'V'},
   'cloudLayers': []}},
 {'id': 'https://api.weather.gov/stations/000PG/observations/2024-09-29T21:00:00+00:00',
  'type': 'Feature',
  'geometry': {'type': 'Point', 'coordinates': [-121.34, 36.79]},
  'properties': {'@id': 'https://api.weather.gov/stations/000PG/observations/2024-09-29T21:00:00+00:00',
   '@type': 'wx:ObservationStation',
   'elevation': {'unitCode': 'wmoUnit:m', 'value': 129.2},
   'station': 'https://api.weather.gov/stations/000PG',
   'timestamp': '2024-09-29T21:00:00+00:00',
   'rawMessage': '',
   'textDescription': '',
   'icon': None,
   'presentWeather': [],
   'temperature': {'unitCode': 'wmoUnit:degC',
    'value': 22.39,
    'qualityControl': 'V'},
   'dewpoint': {'unitCode': 'wmoUnit:degC',
    'value': 13.61,
    'qualityControl': 'V'},
   'windDirection': {'unitCode': 'wmoUnit:degree_(angle)',
    'value': 290.1,
    'qualityControl': 'V'},
   'windSpeed': {'unitCode': 'wmoUnit:km_h-1',
    'value': 8.1,
    'qualityControl': 'V'},
   'windGust': {'unitCode': 'wmoUnit:km_h-1',
    'value': None,
    'qualityControl': 'Z'},
   'barometricPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'seaLevelPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'visibility': {'unitCode': 'wmoUnit:m',
    'value': None,
    'qualityControl': 'Z'},
   'maxTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'minTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'precipitationLast3Hours': {'unitCode': 'wmoUnit:mm',
    'value': None,
    'qualityControl': 'Z'},
   'relativeHumidity': {'unitCode': 'wmoUnit:percent',
    'value': 57.574506766944,
    'qualityControl': 'V'},
   'windChill': {'unitCode': 'wmoUnit:degC',
    'value': None,
    'qualityControl': 'V'},
   'heatIndex': {'unitCode': 'wmoUnit:degC',
    'value': 22.187889898914445,
    'qualityControl': 'V'},
   'cloudLayers': []}},
 {'id': 'https://api.weather.gov/stations/000PG/observations/2024-09-09T13:40:00+00:00',
  'type': 'Feature',
  'geometry': {'type': 'Point', 'coordinates': [-121.34, 36.79]},
  'properties': {'@id': 'https://api.weather.gov/stations/000PG/observations/2024-09-09T13:40:00+00:00',
   '@type': 'wx:ObservationStation',
   'elevation': {'unitCode': 'wmoUnit:m', 'value': 129.2},
   'station': 'https://api.weather.gov/stations/000PG',
   'timestamp': '2024-09-09T13:40:00+00:00',
   'rawMessage': '',
   'textDescription': '',
   'icon': None,
   'presentWeather': [],
   'temperature': {'unitCode': 'wmoUnit:degC',
    'value': 10.14,
    'qualityControl': 'V'},
   'dewpoint': {'unitCode': 'wmoUnit:degC',
    'value': 8.85,
    'qualityControl': 'V'},
   'windDirection': {'unitCode': 'wmoUnit:degree_(angle)',
    'value': 305.4,
    'qualityControl': 'V'},
   'windSpeed': {'unitCode': 'wmoUnit:km_h-1',
    'value': 0.54,
    'qualityControl': 'V'},
   'windGust': {'unitCode': 'wmoUnit:km_h-1',
    'value': None,
    'qualityControl': 'Z'},
   'barometricPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'seaLevelPressure': {'unitCode': 'wmoUnit:Pa',
    'value': None,
    'qualityControl': 'Z'},
   'visibility': {'unitCode': 'wmoUnit:m',
    'value': None,
    'qualityControl': 'Z'},
   'maxTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'minTemperatureLast24Hours': {'unitCode': 'wmoUnit:degC', 'value': None},
   'precipitationLast3Hours': {'unitCode': 'wmoUnit:mm',
    'value': None,
    'qualityControl': 'Z'},
   'relativeHumidity': {'unitCode': 'wmoUnit:percent',
    'value': 91.70002384907,
    'qualityControl': 'V'},
   'windChill': {'unitCode': 'wmoUnit:degC',
    'value': None,
    'qualityControl': 'V'},
   'heatIndex': {'unitCode': 'wmoUnit:degC',
    'value': None,
    'qualityControl': 'V'},
   'cloudLayers': []}}
]