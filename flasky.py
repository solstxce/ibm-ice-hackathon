from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import csv
import json
app = Flask(__name__)
csv_file_path = './output.csv'
def scrape_data(page_url):
    response = requests.get(page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = []
        for product in soup.find_all('div', class_='prdC bgF br4 fs12 fg2t dIb vT pR taC bs bd2E m6'):
            try:
                name_element = product.find('a', class_='c9 dB fs11 wp96 oH tdN ttC wsN pt4')
                orig_price_element = product.find('div', class_='tdS dIb vM fs12 c9')
                disc_price_element = product.find('div', class_='dIb vM c3 fs14')
                rating_element = product.find('div', class_='dIb vM lh12 fwB fs11')
                image_element = product.find('img', class_='prdI')  # Update the class based on your HTML structure
                image_url = image_element['data-src'] if image_element and 'data-src' in image_element.attrs else None

                if name_element and orig_price_element:
                    name = name_element.find('span').text.strip()
                    original_price = orig_price_element.text.strip()

                    # Check if discount price exists, otherwise set current price as original price
                    if disc_price_element:
                        current_price = disc_price_element.text.strip()
                    else:
                        current_price = original_price

                    # Extract rating or set as None if not available
                    rating = rating_element.text.strip() if rating_element else "None"

                    items.append({'Name': name, 'Original Price': original_price, 'Current Price': current_price, 'Rating': rating, 'Image URL': image_url})
                else:
                    print("Missing data for a product")
            except Exception as e:
                print(f"Error: {e}")
        return items
    else:
        print(f"Failed to fetch {page_url}")
        return []

# Route to trigger scraping and return CSV data
@app.route('/scrape_data_men_footwear', methods=['GET'])
def scrape_data_route1():
    # URL for the initial page
    url = "https://www.limeroad.com/men-footwear"

    all_items = []

    # Send an HTTP request to the initial URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the data you need using BeautifulSoup methods
        pagination_container = soup.find('div', id='pagination')

        # Extract links from pagination container
        if pagination_container:
            pagination_links = pagination_container.find_all('a', href=True)  # Find all <a> elements with href attribute

            # Extracting URLs of all pages
            page_urls = [link['href'] for link in pagination_links]
            page_urls.insert(0, url)  # Insert the initial URL to scrape the first page as well

            # Loop through each pagination link to scrape data
            for page_url in page_urls:
                page_items = scrape_data(page_url)
                all_items.extend(page_items)

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name','Image URL', 'Original Price', 'Current Price', 'Rating']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in all_items:
            csv_writer.writerow(item)
    # Write the data to a JSON file
    json_file_path = './men_footwear.json'  # JSON file path

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(all_items, json_file, indent=4)
    with open(json_file_path,'r') as jfile:
        dat = json.load(jfile)
    return jsonify({"response": dat})
@app.route('/scrape_data_men_shirts', methods=['GET'])
def scrape_data_route2():
    # URL for the initial page
    url = "https://www.limeroad.com/clothing/ethnic-wear/sarees?src_id=navdeskSarees__001"

    all_items = []

    # Send an HTTP request to the initial URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the data you need using BeautifulSoup methods
        pagination_container = soup.find('div', id='pagination')

        # Extract links from pagination container
        if pagination_container:
            pagination_links = pagination_container.find_all('a', href=True)  # Find all <a> elements with href attribute

            # Extracting URLs of all pages
            page_urls = [link['href'] for link in pagination_links]
            page_urls.insert(0, url)  # Insert the initial URL to scrape the first page as well

            # Loop through each pagination link to scrape data
            for page_url in page_urls:
                page_items = scrape_data(page_url)
                all_items.extend(page_items)

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name','Image URL', 'Original Price', 'Current Price', 'Rating']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in all_items:
            csv_writer.writerow(item)
    # Write the data to a JSON file
    json_file_path = './men_shirts.json'  # JSON file path

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(all_items, json_file, indent=4)
    with open(json_file_path,'r') as jfile:
        dat = json.load(jfile)
    return jsonify({"response": dat})
@app.route('/scrape_data_women_sarees', methods=['GET'])
def scrape_data_route3():
    # URL for the initial page
    url = "https://www.limeroad.com/clothing/ethnic-wear/sarees?src_id=navdeskSarees__001"

    all_items = []

    # Send an HTTP request to the initial URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the data you need using BeautifulSoup methods
        pagination_container = soup.find('div', id='pagination')

        # Extract links from pagination container
        if pagination_container:
            pagination_links = pagination_container.find_all('a', href=True)  # Find all <a> elements with href attribute

            # Extracting URLs of all pages
            page_urls = [link['href'] for link in pagination_links]
            page_urls.insert(0, url)  # Insert the initial URL to scrape the first page as well

            # Loop through each pagination link to scrape data
            for page_url in page_urls:
                page_items = scrape_data(page_url)
                all_items.extend(page_items)

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name','Image URL', 'Original Price', 'Current Price', 'Rating']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in all_items:
            csv_writer.writerow(item)
    # Write the data to a JSON file
    json_file_path = './woman-sarees.json'  # JSON file path

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(all_items, json_file, indent=4)
    with open(json_file_path,'r') as jfile:
        dat = json.load(jfile)
    return jsonify({"response": dat})
@app.route('/scrape_data_women_skirts', methods=['GET'])
def scrape_data_route4():
    # URL for the initial page
    url = "https://www.limeroad.com/clothing/ethnic-wear/skirts?src_id=navdeskPalazzosSkirts__008"

    all_items = []

    # Send an HTTP request to the initial URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the data you need using BeautifulSoup methods
        pagination_container = soup.find('div', id='pagination')

        # Extract links from pagination container
        if pagination_container:
            pagination_links = pagination_container.find_all('a', href=True)  # Find all <a> elements with href attribute

            # Extracting URLs of all pages
            page_urls = [link['href'] for link in pagination_links]
            page_urls.insert(0, url)  # Insert the initial URL to scrape the first page as well

            # Loop through each pagination link to scrape data
            for page_url in page_urls:
                page_items = scrape_data(page_url)
                all_items.extend(page_items)

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name','Image URL', 'Original Price', 'Current Price', 'Rating']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in all_items:
            csv_writer.writerow(item)
    # Write the data to a JSON file
    json_file_path = './womem_skirts.json'  # JSON file path

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(all_items, json_file, indent=4)
    with open(json_file_path,'r') as jfile:
        dat = json.load(jfile)
    return jsonify({"response": dat})
@app.route('/scrape_data_boys_tshirts', methods=['GET'])
def scrape_data_route5():
    # URL for the initial page
    url = "https://www.limeroad.com/boys-tshirts?src_id=navdeskTShirts__000"

    all_items = []

    # Send an HTTP request to the initial URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the data you need using BeautifulSoup methods
        pagination_container = soup.find('div', id='pagination')

        # Extract links from pagination container
        if pagination_container:
            pagination_links = pagination_container.find_all('a', href=True)  # Find all <a> elements with href attribute

            # Extracting URLs of all pages
            page_urls = [link['href'] for link in pagination_links]
            page_urls.insert(0, url)  # Insert the initial URL to scrape the first page as well

            # Loop through each pagination link to scrape data
            for page_url in page_urls:
                page_items = scrape_data(page_url)
                all_items.extend(page_items)

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name','Image URL', 'Original Price', 'Current Price', 'Rating']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in all_items:
            csv_writer.writerow(item)
    # Write the data to a JSON file
    json_file_path = './boys_tshirts.json'  # JSON file path

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(all_items, json_file, indent=4)
    with open(json_file_path,'r') as jfile:
        dat = json.load(jfile)
    return jsonify({"response": dat})
@app.route('/scrape_data_girls_frocks', methods=['GET'])
def scrape_data_route6():
    # URL for the initial page
    url = "https://www.limeroad.com/girls-dresses?src_id=navdeskDressesFrocks__100"

    all_items = []

    # Send an HTTP request to the initial URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the data you need using BeautifulSoup methods
        pagination_container = soup.find('div', id='pagination')

        # Extract links from pagination container
        if pagination_container:
            pagination_links = pagination_container.find_all('a', href=True)  # Find all <a> elements with href attribute

            # Extracting URLs of all pages
            page_urls = [link['href'] for link in pagination_links]
            page_urls.insert(0, url)  # Insert the initial URL to scrape the first page as well

            # Loop through each pagination link to scrape data
            for page_url in page_urls:
                page_items = scrape_data(page_url)
                all_items.extend(page_items)

    # Write the data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Name','Image URL', 'Original Price', 'Current Price', 'Rating']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in all_items:
            csv_writer.writerow(item)
    # Write the data to a JSON file
    json_file_path = './girls-frocks.json'  # JSON file path

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(all_items, json_file, indent=4)
    with open(json_file_path,'r') as jfile:
        dat = json.load(jfile)
    return jsonify({"response": dat})

# Route to render the HTML page with the button
@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)