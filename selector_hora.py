from bs4 import BeautifulSoup
import requests

url = 'https://deportesweb.madrid.es/DeportesWeb/Modulos/VentaServicios/Alquileres/ReservaEspacios?token=5F47B0942AD5C1AE9DE0E377925F4070D117CC30D6829322180F30ADED336291'  # Replace with the URL you want to scrape
response = requests.get(url)


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 2: Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 3: Find all tables
    tables = soup.find_all('table')
    
    # Print the number of tables found
    print(f'Number of tables found: {len(tables)}')
    
    # Optionally, print the content of each table
    for i, table in enumerate(tables):
        print(f'\nTable {i + 1}:')
        print(table.prettify())
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
