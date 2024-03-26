import requests
import json

date_url = ["1974-04-08", "1974-04-14"]
cc = ["125mx", "250mx", "500mx"]
location = ["hangtown-motocross-classic", "baymare-cycle-park"]
base_url = "https://vault.racerxonline.com/{}/{}/{}"

def make_requests():
    urls_with_200_response = []
    
    for i in range(len(date_url)):
        for j in range(len(cc)):
            for k in range(len(location)):
                url = base_url.format(date_url[i], cc[j], location[k])
                response = requests.get(url)
                if response.status_code == 200:
                    urls_with_200_response.append(url)
    
    return urls_with_200_response

if __name__ == "__main__":
    urls_200 = make_requests()
    output_json = json.dumps({"urls_with_200_response": urls_200}, indent=4)
    print(output_json)

