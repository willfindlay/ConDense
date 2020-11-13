import click

from condense.scrape.scraper import Scraper


@click.command(help='Scrape conference proceedings')
@click.option('venues', '-v', '--venue', type=str, multiple=True)
def scrape(venues):
    s = Scraper()
    s.scrape(venues=venues)
    s.save_data()
