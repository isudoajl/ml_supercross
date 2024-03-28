import requests
from bs4 import BeautifulSoup
import json

# JSON object containing URLs for different years and categories
urls = {
    "2010": [
        "https://vault.racerxonline.com/2010-05-22/250/hangtown-motocross-classic",
        "https://vault.racerxonline.com/2010-05-22/450/hangtown-motocross-classic"
    ],
    "2023": [
        "https://vault.racerxonline.com/2023-05-27/250/pala-raceway",
        "https://vault.racerxonline.com/2023-05-27/450/pala-raceway"
    ]
}

# Initialize a dictionary to store the organized data
organized_data = {}

# Iterate over each year and its corresponding URLs
for year, year_urls in urls.items():
    # Initialize a list to store the data for the current year
    year_data = []
    
    # Iterate over each URL for the current year
    for url in year_urls:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table you're interested in
        table = soup.find('table')
        
        # Check if the table is found
        if table:
            # Find all table rows
            rows = table.find_all('tr')
            
            # Loop through each row skipping the header row
            for row in rows[1:]:
                # Find all table data cells in the row
                cells = row.find_all('td')
                
                # Extract the text from each cell and add to the data list
                row_data = {
                    "position": cells[0].text.strip(),
                    "pilot": cells[1].text.strip(),
                    "hometown": cells[2].text.strip(),
                    "moto_1": cells[3].text.strip(),
                    "moto_2": cells[4].text.strip(),
                    "team": cells[5].text.strip(),
                    "winner": "true" if cells[0].text.strip() == "1" else "false"
                }
                
                # Append the row data to the year data
                year_data.append(row_data)
    
    # Add the data for the current year to the organized data dictionary
    organized_data[year] = year_data

# Convert the organized data dictionary to JSON format
json_organized_data = json.dumps(organized_data, indent=4)

# Print the JSON output
print(json_organized_data)

