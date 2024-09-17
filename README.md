IP Geolocation Lookup and Mapping
This Python script retrieves geolocation information for the public IP address making the request using the IPinfo API. It then displays this information, including the IP address, city, region, country, and carrier, and creates an interactive map marking the location.

Features
Fetches the public IP address geolocation data.
Retrieves details such as city, region, country, latitude, longitude, and carrier.
Creates and saves an interactive map with the location marker using Folium.
Requirements
Python 3.x
requests library
folium library
Installation
Clone the repository (if applicable) or save the script to a file, e.g., geo_map_no_key.py.

Install required libraries: You can install the required libraries using pip:

bash
pip install requests folium
Usage
Run the Script: Execute the script using Python:

bash
python geo_map_no_key.py
Output:

The script will print the following information to the console:
IP Address
City
Region
Country
Carrier
It will generate a file named map.html in the script's directory, which contains an interactive map centered on the location associated with the IP address.
Code Overview
get_geolocation_info(): Fetches geolocation information for the public IP address making the request using the IPinfo API. Extracts and returns details including IP address, city, region, country, latitude, longitude, and carrier.

create_map(latitude, longitude): Creates a Folium map centered on the provided latitude and longitude, adds a marker at the location, and saves the map as map.html.

main(): Calls the get_geolocation_info() function to retrieve data, prints the information, and then calls create_map() to generate the map.

Example Output
When you run the script, you will see output similar to:

yaml
IP Address: 123.123.123.123
City: Example City
Region: Example Region
Country: Example Country
Carrier: Example ISP
A map file named map.html will be created, showing the location associated with the IP address.

Notes
The script uses the free public IPinfo endpoint and does not require an API key for basic geolocation lookups.
Accuracy and detail of the data may vary, and there might be usage limits on the free endpoint.
Ensure you have permission to use and look up the IP address information.
