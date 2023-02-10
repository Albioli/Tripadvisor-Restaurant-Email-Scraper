import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

email_address = []
urls = [
    'https://www.tripadvisor.it/Restaurants-g187849-Milan_Lombardy.html',
    'https://www.tripadvisor.it/Restaurants-g187791-Rome_Lazio.html'
]

for url in urls:
    try:
        response = requests.get(url, headers={'User-Agent': "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, 'html.parser')
        restaurants = soup.find_all(class_="zqsLh")
        restaurant_links = [restaurant.find(class_="Lwqic Cj b").get("href") for restaurant in restaurants]
        for link in restaurant_links:
            correct_restaurant_links = "https://www.tripadvisor.it" + link
            response1 = requests.get(correct_restaurant_links, headers={'User-Agent': "Mozilla/5.0"})
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            email_element = soup1.find_all(class_="IdiaP Me sNsFa")
            for element in email_element:
                match = re.search(r'mailto:(.*?)\?', str(element))
                if match:
                    email_address.append(match.group(1))
    except:
        pass

df = pd.DataFrame({
    "Email Address": email_address,
})

df.to_csv('', index=False)
