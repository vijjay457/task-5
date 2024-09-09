import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract product information from a single page
def extract_product_info(url):
    # Send a request to fetch the HTML content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all product containers (update the class name according to the website structure)
    products = soup.find_all(class_='product-class-name')  # Replace 'product-class-name' with the actual class

    product_data = []

    for product in products:
        # Extract the product name
        name = product.find(class_='name-class').text.strip()  # Replace 'name-class' with actual class

        # Extract the price
        price = product.find(class_='price-class').text.strip()  # Replace 'price-class' with actual class

        # Extract the rating
        rating = product.find(class_='rating-class').text.strip()  # Replace 'rating-class' with actual class

        product_data.append([name, price, rating])

    return product_data

# URL of the page you want to scrape
url = 'https://www.zoho.com/commerce/'  # Replace with the actual URL

# Extract product information
data = extract_product_info(url)

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(data, columns=['Name', 'Price', 'Rating'])
df.to_csv('products.csv', index=False)

print('Product information has been saved to products.csv')
