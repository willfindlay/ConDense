from __future__ import annotations
import os

import numpy as np
import pandas as pd


class Processor:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    @staticmethod
    def from_csv(filename: str) -> Processor:
        """
        Initialize the data processor from a saved wrangle file.
        """
        with open(filename, 'r') as f:
            data = pd.read_csv(f, keep_default_na=False)

        return Processor(data)

    def conference_stats(self):
        CS_COLUMNS = [
            'Venue',
            'Year',
            'Accepted Papers',
            'Authorship Stats',
            'Reference Stats',
            'Attack Rate',
            'Defense Rate',
            'Study Rate',
            'Analysis Rate',
            'Audit Rate',
        ]

        data = pd.DataFrame(columns=CS_COLUMNS)
        print(data)

        # TODO
