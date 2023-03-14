# Restaurant Email Scraper

This Python program scrapes the email addresses and names of restaurants listed on TripAdvisor for a given city. The program takes in the base URL for the city's restaurant page and the number of pages to scrape.

## Installation
To run this program, you need to have Python 3 installed on your machine, as well as the following libraries:

- requests
- beautifulsoup4
- pandas

You can install them via pip:

```python
pip install requests beautifulsoup4 pandas
```

Copy code
pip install requests beautifulsoup4 pandas
Usage
To use the program, simply run the script in a Python environment.

python
Copy code
python tripadvisor_scraper.py
By default, the program will scrape the first two pages of restaurant listings for Rome, Italy. You can change the base_url variable to the URL of the restaurant page for a different city and the pages variable to the number of pages to scrape.

### The program will output a Pandas DataFrame containing the email addresses and names of the scraped restaurants.

### License
This program is released under the MIT License.
