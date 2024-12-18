import requests


def get_humidity(lat, lon, api_key):
    """
    Fetch the current humidity for a given coordinate using OpenWeatherMap API.
    """
    # API Endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    # Make the API request
    response = requests.get(url)

    # Check for errors
    if response.status_code != 200:
        return f"Error: Unable to fetch data (Status code: {response.status_code})"

    # Parse the JSON response
    data = response.json()

    # Extract humidity
    humidity = data["main"]["humidity"]
    location = data["name"]
    return f"Location: {location}, Humidity: {humidity}%"


# Main program
if __name__ == "__main__":
    # Input coordinates
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    # Your OpenWeatherMap API key
    api_key = "your_api_key_here"

    # Get and display humidity
    print(get_humidity(latitude, longitude, api_key))
