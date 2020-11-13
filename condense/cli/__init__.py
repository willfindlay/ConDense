import click

from condense.cli.scrape import scrape


@click.group(help='A webscraper for top academic conferences.')
@click.help_option('-h', '--help')
def condense():
    pass


condense.add_command(scrape)
