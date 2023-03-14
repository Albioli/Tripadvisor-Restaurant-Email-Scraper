# Tripadvisor Restaurant Email Scraper

This Python program scrapes the email addresses and names of restaurants listed on TripAdvisor for a given city within the pages: "Top 10 Restaurants in {Your city}". The program takes in the base URL for the city's restaurant page and the number of pages to scrape.

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
To use this program, you need to do the following:

1. Open the script file and edit the '__pages__' variable to indicate how many pages you want to scrape.
2. Edit the '__base_url__' variable to include the URL of the city you want to scrape.
3. In the '__base_url__' variable, replace "oa{page_num}" with the string that corresponds to the pagination parameter in the website's URL structure.
4. Run the script.

The output will be a Pandas DataFrame containing the email addresses and names of restaurants scraped from the TripAdvisor website for the specified city and number of pages.

Credits
This program was created by Albioli as a demonstration of web scraping techniques using Python. It is intended for educational purposes only.
