import json
import subprocess
import requests

def construct_urls(data):
    try:
        # Loading location data from the JSON file
        with open('/ml_supercross/web_scraping/data_collection/json_venue_cut_urls.json', 'r') as file:
            location_data = json.load(file)
        
        # Extracting location values from JSON
        location = location_data["events"]
    except KeyError:
        print("Error: 'events' key not found in the JSON file.")
        return
    
    # Extracting date values from the input data
    date_urls = [date for year_dates in data.values() for date in year_dates]
    
    cc = ["450"]
    base_url = "https://vault.racerxonline.com/{}/{}/{}"

    urls_with_200_response = {}

    for year, year_dates in data.items():
        year_urls = []
        for date_url in year_dates:
            for cc_value in cc:
                for loc in location:
                    url = base_url.format(date_url, cc_value, loc)
                    response = requests.get(url)
                    if response.status_code == 200:
                        year_urls.append(url)
        urls_with_200_response[year] = year_urls

    return urls_with_200_response

def main():
    # Define the command to call the Python program
    command = ['python', '/ml_supercross/web_scraping/web_vault_fetch_racing_dates.py']
    
    try:
        # Execute the command and capture its output
        output = subprocess.check_output(command, universal_newlines=True)
        # Load the output JSON into the 'data' variable
        data = json.loads(output)
        
        # Now you can use the 'data' variable as needed
        valid_urls = construct_urls(data)
        
        if valid_urls:
            # Save the dictionary of valid URLs to a file
            file_path = '/ml_supercross/web_scraping/data_collection/generated_urls_450.json'
            with open(file_path, 'w') as file:
                json.dump(valid_urls, file, indent=4)
            print("Generated URLs saved to:", file_path)
        
    except subprocess.CalledProcessError as e:
        print("Error executing the command:", e)
    except json.JSONDecodeError as e:
        print("Error decoding JSON output:", e)

if __name__ == "__main__":
    main()

