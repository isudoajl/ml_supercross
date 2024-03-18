import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://vault.racerxonline.com/2010/mx/races"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <li> tags
    li_tags = soup.find_all('li')
    
    # Extract text from each <li> tag
    for li in li_tags:
        print(li.text.strip())
else:
    print("Failed to retrieve webpage.")

