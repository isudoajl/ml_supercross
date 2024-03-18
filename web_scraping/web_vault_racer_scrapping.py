import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = "https://vault.racerxonline.com/2010-05-22/250/hangtown-motocross-classic"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table you're interested in
table = soup.find('table')

# Initialize a list to store the data
data = []

# Check if the table is found
if table:
    # Find all table rows
    rows = table.find_all('tr')
    
    # Loop through each row
    for row in rows:
        # Find all table data cells in the row
        cells = row.find_all('td')
        
        # Extract the text from each cell and add to the data list
        row_data = [cell.text.strip() for cell in cells]
        
        # Check if the row data is not empty
        if any(row_data):
            data.append(row_data)

# Convert the data list to JSON format
json_data = json.dumps(data, indent=4)

# Print the JSON output
print(json_data)

