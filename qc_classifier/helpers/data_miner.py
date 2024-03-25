from helpers.constants import TREATMENTS


class DataMiner:
    def __init__(self, df):
        self.df = df

    def get_treatment(self, text):
        for treatment in TREATMENTS:
            if treatment in text:
                return treatment
        return None

    def get_reason(self, code, group):
        return self.df[(self.df["code"] == code) & (self.df["group"] == group)][
            "text"
        ].values[0]

    def remove_bag_bigbag(self, text):
        return text.replace("BIGBAG", "").replace("BAG", "").strip()
