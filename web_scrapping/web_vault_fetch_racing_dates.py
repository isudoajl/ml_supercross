import requests
from bs4 import BeautifulSoup
import json
import time

def convert_dates(json_data):
    # Load the JSON data
    data = json.loads(json_data)
    
    # Iterate over the list of dates and convert them
    converted_dates = []
    for date_str in data:
        # Convert the date format
        converted_date = "-".join([date_str.split()[2], 
                                   str("%02d" % (time.strptime(date_str.split()[0], "%B").tm_mon)), 
                                   str("%02d" % int(date_str.split()[1][:-1]))])
        converted_dates.append(converted_date)
    
    return converted_dates

# Send a GET request to the URL
url = "https://vault.racerxonline.com/2010/mx/races"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all <p> tags on the page
    p_tags = soup.find_all("p")
    
    # Extract only the first value for each <p> occurrence
    p_values = [p_tag.contents[0].strip() for p_tag in p_tags if p_tag.contents]
    
    # Convert the dates in the JSON data
    converted_dates = convert_dates(json.dumps(p_values))
    
    # Print the converted dates in JSON format
    print(json.dumps(converted_dates, indent=4))
else:
    print("Failed to retrieve data from the URL.")

