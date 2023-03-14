# Restaurant Email Scraper

This Python program scrapes the email addresses and names of restaurants listed on TripAdvisor for a given city. The program takes in the base URL for the city's restaurant page and the number of pages to scrape.

## Installation
To run this program, you need to have Python 3 installed on your machine, as well as the following libraries:

- requests
- beautifulsoup4
- pandas

You can install these libraries using pip, for example:

```python
pip install requests
pip install beautifulsoup4
pip install pandas
```

## Usage
To use the program, simply run the script using Python from your command line interface. The script takes two inputs:

1. The base URL of the TripAdvisor restaurant listings, with a placeholder for the page number: 'https://www.tripadvisor.it/Restaurants-g187791-oa{page_num}-Rome_Lazio.html'
2. The number of pages of listings to scrape
