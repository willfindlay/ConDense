from collections import defaultdict
from typing import Optional, List
import re

from pprint import pprint

import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd


class Scraper:
    COLUMNS = ['Venue', 'Year', 'Authors', 'Title']
    PARSER = 'lxml'

    def __init__(self):
        self.data = pd.DataFrame(columns=self.COLUMNS)

    def scrape(
        self, venues: Optional[List[str]] = None,
    ):
        """
        Scrape a venue, a set of venues, or all venues.
        """
        from condense.scrape.venue import VENUE_URLS

        # Determine target venue(s) from arguments
        if not venues:
            venues = VENUE_URLS.keys()

        print('Scraping venue data...')

        # Scrape each venue
        for venue in venues:
            self.do_venue(venue, VENUE_URLS[venue])

        print('All done!')

    def do_venue(self, venue: str, url: str):
        """
        Scrape a venue.
        """
        print(f'Scraping venue {venue} ({url})...')

        result = requests.get(url, timeout=10)
        if not result.ok:
            raise Exception(f'Failed to fetch data for {url}')
        soup = BeautifulSoup(result.text, features=self.PARSER)

        for paper in soup.select('.inproceedings cite.data'):
            title, authors = self.do_paper(paper)
            match = re.match(r'([^0-9]*)([0-9]*)', venue)
            venue_name, year = match[1], match[2]
            self.data = self.data.append(
                {'Venue': venue_name, 'Year': year, 'Authors': authors, 'Title': title},
                ignore_index=True,
            )

    def do_paper(self, paper: BeautifulSoup):
        """
        Parse a paper title and authors.
        """
        # Parse title
        title = paper.select_one('span.title').text

        # Parse authors
        authors = []
        for author_div in paper.find_all(recursive=True, attrs={'itemprop': 'author'}):
            authors.append(author_div.text)

        return (title, authors)

    def save_data(self, destination: str = 'scraped_data.pickle'):
        """
        Save scraped data to destination.
        """
        from pickle import dump

        with open(destination, 'wb') as f:
            dump(self.data, f)
