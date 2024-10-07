import requests
import time
import logging

from requests.adapters import HTTPAdapter, Retry

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_request_session():
    '''
    This function creates a request session setting the retry logic and timeout.
    Retries will be executed if a timeout occurs or if HTTP return codes are 502, 503, 504.
    In case of timeout, the script will sleep for 30 seconds before retrying.
    '''
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session


def fetch_data(session, url):
    '''
    This function fetches data from a given URL using the provided session.
    It handles timeouts and request exceptions.
    '''
    try:
        logging.info(f'Fetching data from {url}')
        response = session.get(url)
        response.raise_for_status()
        logging.debug(f'Response status code: {response.status_code}')
        return response.json()
    except requests.exceptions.Timeout as e:
        logging.error(f'Timeout error occurred: {e}')
        time.sleep(30)
        raise
    except requests.exceptions.RequestException as e:
        logging.error(f'A request error occurred: {e}')
        raise

def extract_data(api_url, station_id):
    '''
    This function extracts weather data for a station id from the weather API.
    A station_id is required to get the data.
    The endpoint to extract the data is /stations/{station_id}/observations.
    '''
    if not api_url:
        raise ValueError('API URL is required')
    if not station_id:
        raise ValueError('Station ID is required')

    station_endpoint = f'{api_url}/stations/{station_id}'
    observations_endpoint = f'{api_url}/stations/{station_id}/observations'

    with create_request_session() as session:
        station_data = fetch_data(session, station_endpoint).get('properties', {})
        observations_data = fetch_data(session, observations_endpoint).get('features', [])

    return station_data, observations_data

if __name__ == '__main__':
    api_url = 'https://api.weather.gov'
    station_id = '000PG'
    station_data, observations_data = extract_data(api_url, station_id)
    logging.info(f'Station data: {station_data}')
    logging.info(f'Observation data: {observations_data[0]}')

 