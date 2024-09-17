import requests
import folium

# Publicly accessible IPinfo URL (no API key required for basic lookups)
IP_GEOLOCATION_API_URL = 'https://ipinfo.io/json'

def get_geolocation_info():
    try:
        response = requests.get(IP_GEOLOCATION_API_URL)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        
        # Extract details
        ip_address = data.get('ip', 'N/A')
        city = data.get('city', 'N/A')
        region = data.get('region', 'N/A')
        country = data.get('country', 'N/A')
        location = data.get('loc', '0,0').split(',')
        latitude = float(location[0])
        longitude = float(location[1])
        carrier = data.get('org', 'N/A')  # Carrier information is often in 'org'

        return {
            'ip_address': ip_address,
            'city': city,
            'region': region,
            'country': country,
            'latitude': latitude,
            'longitude': longitude,
            'carrier': carrier
        }
    except requests.RequestException as e:
        print(f"Error fetching geolocation data: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def create_map(latitude, longitude):
    # Create a folium map centered at the given latitude and longitude
    m = folium.Map(location=[latitude, longitude], zoom_start=12)
    
    # Add a marker for the location
    folium.Marker([latitude, longitude], tooltip='Your Location').add_to(m)
    
    # Save the map to an HTML file
    m.save('map.html')
    print("Map has been saved to map.html")

def main():
    info = get_geolocation_info()
    if info:
        print("IP Address:", info['ip_address'])
        print("City:", info['city'])
        print("Region:", info['region'])
        print("Country:", info['country'])
        print("Carrier:", info['carrier'])
        
        # Display the location on a map
        create_map(info['latitude'], info['longitude'])

if __name__ == '__main__':
    main()
