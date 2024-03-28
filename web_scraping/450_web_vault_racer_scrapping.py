import requests
from bs4 import BeautifulSoup
import json

# Load the URLs from the JSON file
with open('/ml_supercross/web_scraping/data_collection/generated_urls_450.json', 'r') as file:
    urls = json.load(file)

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
        
        # Add the data for the current URL to the list of data for the current year
        year_data.append(data)
    
    # Add the data for the current year to the organized data dictionary
    organized_data[year] = year_data

# Convert the organized data dictionary to JSON format
json_organized_data = json.dumps(organized_data, indent=4)

# Write the JSON output to a file
output_file_path = '/ml_supercross/web_scraping/data_collection/450_races.json'
with open(output_file_path, 'w') as output_file:
    output_file.write(json_organized_data)

print(f"Output saved to: {output_file_path}")

