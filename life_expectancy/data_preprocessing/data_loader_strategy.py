from abc import ABC, abstractmethod
import pandas as pd
from pathlib import Path


class DataLoaderStrategy(ABC):
    @abstractmethod
    def load_data(self, data_dir: Path, filename: str) -> pd.DataFrame:
        """Abstract method to load data into a Dataframe."""
        pass
