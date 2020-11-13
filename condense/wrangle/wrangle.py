from __future__ import annotations

import numpy as np
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
        # Manual classification columns
        self.data['Classification'] = ''
        self.data['Area'] = ''
        self.data['Reference Count'] = np.NaN

        # Add an author count per paper
        self.data['Author Count'] = self.data['Authors'].map(len)

        # Stringify author lists
        self.data['Authors'] = self.data['Authors'].map(lambda ell: ', '.join(ell))
        # Rename venues
        self.data['Venue'] = self.data['Venue'].map(self._rename_venue)

    def _rename_venue(self, venue_name: str):
        if venue_name == 'usenix':
            return 'USENIX Security'
        if venue_name == 'oakland':
            return 'IEEE S&P'
        if venue_name == 'ndss':
            return 'NDSS'
        if venue_name == 'ccs':
            return 'ACM CCS'
        return venue_name

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
