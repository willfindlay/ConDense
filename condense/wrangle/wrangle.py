from __future__ import annotations

import pandas as pd


class Wrangler:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    @staticmethod
    def from_scrape_file(filename: str) -> Wrangler:
        """
        Initialize the wrangler from a saved scrape file.
        """
        from pickle import load

        with open(filename, 'rb') as f:
            data = load(f)

        return Wrangler(data)

    def wrangle(self):
        """
        Perform additional computations on the data.
        """
        # Add an author count per paper
        self.data['Author Count'] = self.data['Authors'].map(len)

    def to_csv(self, destination: str = 'wrangled_data.csv'):
        """
        Export results to a CSV file.
        """
        with open(destination, 'w') as f:
            self.data.to_csv(f, index=False)

    # def save_data(self, destination: str = 'wrangled_data.pickle'):
    #    """
    #    Save wrangled data to destination.
    #    """
    #    from pickle import dump

    #    with open(destination, 'wb') as f:
    #        dump(self.data, f)
