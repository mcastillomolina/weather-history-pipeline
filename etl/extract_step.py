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

    observations_endpoint = f'{api_url}/stations/{station_id}/observations'

    session = create_request_session()
    try:
        logging.info(f'Extracting data from {observations_endpoint}')
        observations = session.get(observations_endpoint)
        observations.raise_for_status()
        logging.debug(f'Response status code: {observations.status_code}')
        observations_data = observations.json()['features']
        logging.debug(f'Observations data: {observations_data}')
        return observations_data
    except requests.exceptions.Timeout as e:
        logging.error(f'Timeout error occured: {e}')
        time.sleep(30)
        raise
    except requests.exceptions.RequestException as e:
        logging.error(f'A request error occured: {e}')
        raise
    finally:
        session.close()

if __name__ == '__main__':
    api_url = 'https://api.weather.gov'
    station_id = '000PG'
    data = extract_data(api_url, station_id)
    logging.info(f'Extracted data: {data}')

 