import pandas as pd
from features import FEATURES
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

class DataPreprocessor:

    def preprocess(self, file) -> tuple:
        df  = self.read_csv(file)
        df  = self.make_columns_snake_case(df)
        ids = self.get_ids(df)
        logger.info(f"Найденны признаки: {df.columns.tolist()}")
        if not self.check_required_features(df):
            logger.info(f"Необходимые признаки не найдены: {FEATURES}")
        df = self.remove_extra_columns(df)
        return df, ids

    def read_csv(self, file) -> pd.DataFrame:
        return pd.read_csv(file)

    def make_columns_snake_case(self, df: pd.DataFrame) -> pd.DataFrame:
        df.columns = df.columns\
            .str.lower()\
            .str.replace(' ', '_')\
            .str.replace(',', '_')\
            .str.replace('__', '_')
        return df

    def check_required_features(self, df: pd.DataFrame) -> bool:
        return set(set(FEATURES)).issubset(df.columns.tolist())

    def get_ids(self, df) -> pd.Series:
        ids = df['id']
        return ids

    def remove_extra_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        columns_to_remove = list(set(df.columns.tolist()) - set(FEATURES))
        logger.info(f"Признаки будут удалены: {columns_to_remove}")
        df_no_extra_columns = df.drop(columns_to_remove, axis=1)
        return df_no_extra_columns