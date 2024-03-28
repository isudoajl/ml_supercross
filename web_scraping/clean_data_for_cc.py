import json

# Read data from file
file_path = "/ml_supercross/web_scraping/data_collection/generated_urls_450.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Remove URLs containing "/250/"
for year, urls in data.items():
    data[year] = [url for url in urls if "/250/" not in url]

# Beautify and print the filtered data
formatted_json = json.dumps(data, indent=4)
print(formatted_json)

