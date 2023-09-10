import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract product details from the page
    product_name_elem = soup.find('span', class_='a-size-medium')
    product_name = product_name_elem.text.strip() if product_name_elem else ""

    product_price_elem = soup.find('span', class_='a-price-whole')
    product_price = product_price_elem.text.strip() if product_price_elem else ""

    product_rating_elem = soup.find('span', class_='a-icon-alt')
    product_rating = product_rating_elem.text.strip() if product_rating_elem else ""

    num_reviews_elem = soup.find('span', class_='a-size-base')
    num_reviews = num_reviews_elem.text.strip() if num_reviews_elem else ""

    # Extract additional information from the product page
    description = soup.find('div', {'id': 'productDescription'})
    product_description = description.get_text(strip=True) if description else ""

    asin = soup.find('th', string='ASIN')  # Change 'text' to 'string' here
    asin = asin.find_next('td').get_text(strip=True) if asin else ""

    manufacturer = soup.find('a', {'id': 'bylineInfo'})
    manufacturer = manufacturer.get_text(strip=True) if manufacturer else ""

    return {
        'Product URL': url,
        'Product Name': product_name,
        'Product Price': product_price,
        'Rating': product_rating,
        'Number of Reviews': num_reviews,
        'Description': description,
        'ASIN': asin,
        'Product Description': product_description,
        'Manufacturer': manufacturer
    }

def scrape_amazon_product_listings(base_url, search_query, pages_to_scrape):
    data_list = []

    for page_number in range(1, pages_to_scrape + 1):
        params = {
            'k': search_query,
            'crid': '2M096C61O4MLT',
            'qid': 1653308124,
            'sprefix': 'ba%2Caps%2C283',
            'page': page_number
        }
        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.content, 'html.parser')

        for product in soup.find_all('div', class_='sg-col-inner'):
            product_url = product.find('a', class_='a-link-normal')
            if product_url:
                product_url = 'https://www.flipkart.com' + product_url['href']
                data_list.append(get_product_details(product_url))

    # Create a pandas DataFrame with the scraped data
    df = pd.DataFrame(data_list)

    # Export the DataFrame to a CSV file
    df.to_csv('amazon_product_data_iphone_fk.csv', index=False)

if __name__ == "__main__":
    base_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    search_query = 'iphone'
    pages_to_scrape = 20

    scrape_amazon_product_listings(base_url, search_query, pages_to_scrape)
