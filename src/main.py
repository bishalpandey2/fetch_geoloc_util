import argparse
from geolocation import get_geolocation_by_city, get_geolocation_by_zip

def get_geolocation(location):
    if ',' in location:
        city, state = location.split(',', 1)
        return get_geolocation_by_city(city.strip(), state.strip())
    else:
        return get_geolocation_by_zip(location.strip())

def main():
    parser = argparse.ArgumentParser(description="Fetch geolocation details for city/state or zip code.")
    parser.add_argument("--locations", nargs='+', help="List of locations (city,state or zip code)")
    args = parser.parse_args()

    for location in args.locations:
        result = get_geolocation(location)
        if result:
            print(result)

if __name__ == "__main__":
    main()
