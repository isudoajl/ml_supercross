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
location = ["hangtown-motocross-classic", "baymare-cycle-park"]
base_url = "https://vault.racerxonline.com/{}/{}/{}"

def make_requests():
    urls_with_200_response = []
    
    for date_url in date_urls:
        for cc_value in cc:
            for loc in location:
                url = base_url.format(date_url, cc_value, loc)
                response = requests.get(url)
                if response.status_code == 200:
                    urls_with_200_response.append(url)
    
    return urls_with_200_response

if __name__ == "__main__":
    urls_200 = make_requests()
    output_json = json.dumps({"urls_with_200_response": urls_200}, indent=4)
    print(output_json)

