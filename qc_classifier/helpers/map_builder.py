import pandas as pd


class MapBuilder:
    def __init__(self, df):
        self.df = df

    def hybrid_map(self):
        return {
            hybrid: index for index, hybrid in enumerate(self.df["hybrid"].unique())
        }

    def storage_map(self):
        return {
            storage: index for index, storage in enumerate(self.df["storage"].unique())
        }

    def plant_map(self):
        return {plant: index for index, plant in enumerate(self.df["plant"].unique())}

    def treatment_map(self):
        return {
            treatment: index
            for index, treatment in enumerate(self.df["treatment"].unique())
        }

    def location_map(self):
        return {
            location: index
            for index, location in enumerate(self.df["location"].unique())
        }

    def group_map(self):
        return {
            group: index
            for index, group in enumerate(self.df["problem_group"].unique())
        }
