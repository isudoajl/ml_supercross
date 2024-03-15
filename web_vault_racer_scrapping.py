import requests
from bs4 import BeautifulSoup
import json

# Function to scrape data from the provided URL
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <h3> tags with text '250' or '450'
        h3_tags = soup.find_all('h3', string=['250', '450'])
        
        # Initialize lists to store the table data for each value
        data_250 = []
        data_450 = []
        
        # Iterate through each <h3> tag
        for h3_tag in h3_tags:
            # Extract the text from the <h3> tag as the key for the output
            key = h3_tag.get_text(strip=True)
            
            # Find the nearest <table> tag after the <h3> tag
            table_tag = h3_tag.find_next('table')
            
            # Initialize an empty list to store the table data
            table_data = []
            
            # Extract data from the <table> tag
            if table_tag:
                rows = table_tag.find_all('tr')
                for row in rows:
                    columns = row.find_all('td')
                    row_data = [column.get_text(strip=True) for column in columns]
                    table_data.append(row_data)
            
            # Append the table data to the corresponding list
            if key == '250':
                data_250.extend(table_data)
            elif key == '450':
                data_450.extend(table_data)
        
        # Print reference labels for each output
        print("Output for value 250:")
        print("=" * 50)
        print(json.dumps(format_data(data_250), indent=2))
        print("=" * 50)
        
        print("Output for value 450:")
        print("=" * 50)
        print(json.dumps(format_data(data_450), indent=2))
        print("=" * 50)
    
    else:
        # Print an error message if the request was not successful
        print("Error: Unable to retrieve data from the website.")

# Function to format the data to match the provided syntax
def format_data(data):
    formatted_data = []
    for row in data:
        if len(row) == 4:  # Check if the row contains all elements
            formatted_data.append({
                "position": row[0],
                "rider": row[1],
                "location": row[2],
                "points": row[3]
            })
    return formatted_data

# Main function
if __name__ == "__main__":
    # URL to scrape
    url = "https://vault.racerxonline.com/2010/mx/points"
    
    # Scrape the website
    scrape_website(url)

