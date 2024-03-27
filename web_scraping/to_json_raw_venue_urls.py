import csv
import json

def extract_urls_from_csv(csv_file):
    urls = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                # Extract the URL from each line
                url = row[0].split()[0]
                urls.append(url)
    return urls

def main():
    csv_file = '/ml_supercross/web_scraping/data_collection/raw_venue_urls.csv'  # Replace 'example.csv' with the path to your CSV file
    urls = extract_urls_from_csv(csv_file)
    output = {'urls': urls}
    json_output = json.dumps(output, indent=4)
    print(json_output)

if __name__ == "__main__":
    main()

