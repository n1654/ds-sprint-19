import pandas as pd
from features import FEATURES


class DataPreprocessor:

    def preprocess(self, file) -> pd.DataFrame:
        df = self.read_csv(file)
        df = self.make_columns_snake_case(df)

        if not self.check_required_features(df):
            return df

        df = self.remove_extra_columns(df)

        return df

    def read_csv(self, file) -> pd.DataFrame:
        return pd.read_csv(file)

    def make_columns_snake_case(self, df: pd.DataFrame) -> pd.DataFrame:
        df_columns_snake_case = df.columns\
            .str.lower()\
            .str.replace(' ', '_')\
            .str.replace(',', '_')\
            .str.replace('__', '_')
        return df_columns_snake_case

    def check_required_features(self, df: pd.DataFrame) -> bool:
        if set(df.columns.tolist()).issubset(set(FEATURES)):
            return True
        else:
            return False

    def remove_extra_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        columns_to_remove = list(set(df.columns.tolist()) - set(FEATURES))
        df_no_extra_columns = df.drop(columns_to_remove, axis=1)
        return df_no_extra_columns