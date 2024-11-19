from pathlib import Path
from .data_loader_strategy import DataLoaderStrategy
import pandas as pd


class TSVDataLoader(DataLoaderStrategy):
    def __init__(self, sep: str):
        self.sep = sep

    def load_data(self, data_dir: Path, filename: str) -> pd.DataFrame:
        file_path = data_dir / filename
        return pd.read_csv(file_path, sep=self.sep)


class JSONDataLoader(DataLoaderStrategy):
    def load_data(self, data_dir: Path, filename: str) -> pd.DataFrame:
        file_path = data_dir / filename
        return pd.read_json(file_path)


def load_data(data_dir: Path, filename: str, sep: str) -> pd.DataFrame:
    """Loads the data into a dataframe.
    args:
        data_dir: Path to the data directory.
        filename: Name of the file with extension.
        sep: The separator used in the file (e.g., ',' for CSV).
    returns:
        pd.DataFrame
    """
    file_path = data_dir / filename
    df = pd.read_csv(file_path, sep=sep)
    return df


def save_data(target_dir: Path, base_filename: str, df: pd.DataFrame) -> None:
    """Saves the dataframe to a file in the target directory.
    args:
        target_dir: Path to the target directory.
        base_filename: Base name for the output file (without directory path).
        df: Dataframe to be saved.
    """
    output_path = target_dir / base_filename
    df.to_csv(output_path, index=False)
