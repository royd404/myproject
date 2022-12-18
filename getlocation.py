#! /usr/bin/python3

import requests

def get_location(ip_address):
	url = f"http://ipapi.com/{ip_address}/json/"
	response = requests.get(url)
	data = response.json()
	city = data["city"]
	region = data["region"]
	country = data["country_name"]
	location = f"{city},{region}, {country}"

	return location

ip_address = "8.8.8.8" # Replace this with the IP address you want to look up

location = get_location(ip_address)
print(location)
