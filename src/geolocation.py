import requests
from src.config import API_KEY, BASE_URL_CITY, BASE_URL_ZIP
from logger import logger

def get_geolocation_by_city(city, state, country="US"):
    """Fetches geolocation data using city and state."""
    url = f"{BASE_URL_CITY}?q={city},{state},{country}&limit=1&appid={API_KEY}"
    return fetch_geolocation(url, location_type="city")

def get_geolocation_by_zip(zip_code, country="US"):
    """Fetches geolocation data using zip code."""
    url = f"{BASE_URL_ZIP}?zip={zip_code},{country}&appid={API_KEY}"
    return fetch_geolocation(url, location_type="zip", zip_code=zip_code)

def fetch_geolocation(url, location_type, zip_code=None):
    """Helper function to fetch and process geolocation data."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if location_type == "city":
            return process_city_data(data[0])
        elif location_type == "zip":
            return process_zip_data(data, zip_code)
        else:
            logger.error(f"Invalid location type: {location_type}")
            return None

    except requests.exceptions.RequestException as err:
        logger.error(f"API request failed: {err}")
        return None
    except (KeyError, IndexError) as err:
        logger.error(f"Error processing API response: {err}")
        return None

def process_city_data(data):
    """Process city geolocation data."""
    return {
        "city": data["name"],
        "latitude": data["lat"],
        "longitude": data["lon"],
        "state": data.get("state", "Unknown")
    }

def process_zip_data(data, zip_code):
    """Process zip code geolocation data."""
    return {
        "zip": zip_code,
        "latitude": data["lat"],
        "longitude": data["lon"],
        "city": data["name"]
    }
