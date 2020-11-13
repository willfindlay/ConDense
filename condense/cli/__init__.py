import click

from condense.cli.scrape import scrape
from condense.cli.wrangle import wrangle


@click.group(help='A webscraper for top academic conferences.')
@click.help_option('-h', '--help')
def condense():
    pass


condense.add_command(scrape)
condense.add_command(wrangle)
