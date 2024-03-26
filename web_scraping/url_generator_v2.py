import requests
import json

date_urls = [
    "1974-04-08",
    "1974-04-14",
    "1974-04-28",
    "1974-05-05",
    "1974-05-19",
    "1974-06-30",
    "1974-07-06",
    "1974-07-21",
    "1974-08-11",
    "1974-08-18",
    "1974-08-25",
    "1974-09-02"
]
cc = ["125mx", "250mx", "500mx"]
location_file = "/ml_supercross/web_scraping/data_collection/json_venue_urls.json"
base_url = "https://vault.racerxonline.com/{}/{}/{}"

def load_location_from_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data['urls']

def make_requests():
    urls_with_200_response = []
    locations = load_location_from_file(location_file)
    
    for date_url in date_urls:
        print(f"Processing date_url: {date_url}")
        for cc_value in cc:
            print(f"\tProcessing cc_value: {cc_value}")
            for loc in locations:
                print(f"\t\tProcessing location: {loc}")
                url = base_url.format(date_url, cc_value, loc)
                response = requests.get(url)
                if response.status_code == 200:
                    urls_with_200_response.append(url)
    
    return urls_with_200_response

if __name__ == "__main__":
    urls_200 = make_requests()
    output_json = json.dumps({"urls_with_200_response": urls_200}, indent=4)
    print(output_json)

