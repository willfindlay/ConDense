import click

from condense.wrangle.wrangle import Wrangler


@click.command(help='Wrangle data from conference proceedings')
@click.argument('data_file', type=str)
def wrangle(data_file):
    w = Wrangler.from_scrape_file(data_file)
    w.wrangle()
    w.to_csv()
