import pandas as pd

from helpers.constants import COLUMNS, DF_PATH


class MapBuilder:
    def __init__(self):
        self.df = pd.read_csv(DF_PATH, sep=";", usecols=COLUMNS)

    def hybrid_map(self):
        return {
            hybrid: index for index, hybrid in enumerate(self.df["hybrid"].unique())
        }

    def batch_map(self):
        return {batch: index for index, batch in enumerate(self.df["batch"].unique())}

    def brand_map(self):
        return {brand: index for index, brand in enumerate(self.df["brand"].unique())}

    def sieve_map(self):
        return {sieve: index for index, sieve in enumerate(self.df["sive"].unique())}

    def treatment_map(self):
        return {
            treatment: index
            for index, treatment in enumerate(self.df["treatment"].unique())
        }

    def city_map(self):
        return {city: index for index, city in enumerate(self.df["city"].unique())}


map_builder = MapBuilder()

HYBRID_MAP = map_builder.hybrid_map()
BATCH_MAP = map_builder.batch_map()
BRAND_MAP = map_builder.brand_map()
SIEVE_MAP = map_builder.sieve_map()
TREATMENT_MAP = map_builder.treatment_map()
CITY_MAP = map_builder.city_map()
