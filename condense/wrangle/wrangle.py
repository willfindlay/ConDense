from __future__ import annotations
import os

import numpy as np
import pandas as pd


class Wrangler:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    @staticmethod
    def from_csv(filename: str) -> Wrangler:
        """
        Initialize the wrangler from a saved scrape file.
        """
        with open(filename, 'r') as f:
            data = pd.read_csv(f, keep_default_na=False)

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
        self.data['Author Count'] = self.data['Authors'].map(
            lambda authors: len(authors.split(';'))
        )

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

    def to_csv(self, destination: str, overwrite: bool):
        """
        Export results to a CSV file.
        """
        if os.path.exists(destination) and not overwrite:
            print(f'Cowardly refusing to overwrite existing data {destination}')
            return
        with open(destination, 'w') as f:
            self.data.to_csv(f, index=False)
