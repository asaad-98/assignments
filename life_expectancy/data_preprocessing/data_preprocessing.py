import os
from pathlib import Path

import pandas as pd


def load_data(data_dir: Path, filename: str, sep: str) -> pd.DataFrame:
    """Loads the data into dataframe
    args:
        data_dir: Path to data directory.
        filename: name of the file with extension.
    returns:
        pd.DataFrame
    """
    file_path = data_dir / filename  # resolve file path
    df = pd.read_csv(file_path, sep=sep)

    return df


def save_data(target_dir, filename, df) -> None:
    """Saves file at target directory
    args:
        target_dir: Path.
        filename: Desired output name with extension.
        df: Dataframe to be saved.
    """
    df.to_csv(os.path.join(target_dir, filename), index=False)
