import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_restaurant_links(url):
    response = requests.get(url, headers={'User-Agent': "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    restaurants = soup.find_all(class_="roxNU Vt o")
    return [restaurant.find(class_="Lwqic Cj b").get("href") for restaurant in restaurants]

def get_email_and_name(link):
    correct_restaurant_links = "https://www.tripadvisor.it" + link
    response = requests.get(correct_restaurant_links, headers={'User-Agent': "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    email_element = soup.find_all(class_="IdiaP Me sNsFa")
    name_element = soup.find(class_="HjBfq")
    email = None
    name = None
    for e in email_element:
        match = re.search(r'mailto:(.*?)\?', str(e))
        if match:
            email = match.group(1)
            break
    if name_element:
        name = name_element.text.strip()
    return email, name

def scrape_restaurant_data(base_url, pages):
    email_address = []
    names = []
    for page_num in range(pages):
        url = base_url.format(page_num=page_num)
        try:
            restaurant_links = get_restaurant_links(url)
            for link in restaurant_links:
                email, name = get_email_and_name(link)
                email_address.append(email)
                names.append(name)
        except:
            pass

    df = pd.DataFrame({
        "Email Address": email_address,
        "Name": names,
    })

    return df

base_url = 'https://www.tripadvisor.it/Restaurants-g187791-oa{page_num}-Rome_Lazio.html'
pages = 2

df = scrape_restaurant_data(base_url, pages)

df.to_csv('Your_path', index=False)
