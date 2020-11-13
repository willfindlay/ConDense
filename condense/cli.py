import click


@click.group(help='A webscraper for top academic conferences.')
@click.help_option('-h', '--help')
def condense():
    pass


@condense.command(help='Scrape conference proceedings and save them as a CSV file')
@click.option(
    'venues',
    '-v',
    '--venue',
    type=str,
    multiple=True,
    help='Specific venue(s) to scrape',
)
@click.option(
    '-o', '--output', type=str, default='scraped_data.csv', help='Name of output CSV'
)
@click.option(
    '--overwrite/--no-overwrite', default=False, help='Overwrite an existing CSV'
)
def scrape(venues, overwrite, output):
    from condense.scrape.scraper import Scraper

    s = Scraper()
    s.scrape(venues=venues)
    s.to_csv(destination=output, overwrite=overwrite)


@condense.command(
    help='Transform scraped data into a full table and save it as a CSV file'
)
@click.argument('data_file', type=str)
@click.option(
    '-o', '--output', type=str, default='wrangled_data.csv', help='Name of output CSV'
)
@click.option(
    '--overwrite/--no-overwrite', default=False, help='Overwrite an existing CSV'
)
def wrangle(data_file, overwrite, output):
    from condense.wrangle.wrangle import Wrangler

    w = Wrangler.from_csv(data_file)
    w.wrangle()
    w.to_csv(destination=output, overwrite=overwrite)
