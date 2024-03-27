import json
import requests

def construct_urls(data):
    # Your JSON data in a more concise format
    date_urls = [date for year_dates in data.values() for date in year_dates]
    cc = ["125mx", "250mx", "500mx"]
    location = ["hangtown-motocross-classic", "baymare-cycle-park"]
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

# Example usage:
data = {
    "1974": ["1974-04-08"],
    "1975": ["1975-04-06"]
}

valid_urls = construct_urls(data)

# Convert the dictionary of valid URLs to JSON
json_output = json.dumps(valid_urls, indent=4)

# Print the JSON output
#print(json_output)

