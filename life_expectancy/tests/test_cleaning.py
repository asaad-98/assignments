"""Tests for the cleaning module"""

import pandas as pd
from pathlib import Path

from life_expectancy.data_preprocessing.data_cleaning import clean_data
from life_expectancy.data_preprocessing.data_cleaning import (
    save_data,
)


def test_clean_data(life_expectancy_raw, life_expectancy_expected):
    """Run `clean_data` and compare the output to the expected output"""
    life_expectancy_actual = clean_data(
        df=life_expectancy_raw,
        country=None,
    )
    pd.testing.assert_frame_equal(
        life_expectancy_actual, life_expectancy_expected, check_exact=False
    )


def test_save_data(monkeypatch):
    """Test `save_data` function with MonkeyPatch."""

    # Arrange
    df = pd.DataFrame({"column1": [1, 2, 3]})
    target_dir = Path("/fake/path")
    base_filename = "output.csv"

    def mock_to_csv(self, file_path, index):
        # This mock simulates the behavior of `DataFrame.to_csv`
        assert file_path == target_dir / base_filename
        assert index is False

    # Use monkeypatch to replace `DataFrame.to_csv` with the mock function
    monkeypatch.setattr(pd.DataFrame, "to_csv", mock_to_csv)

    # Act
    save_data(target_dir, base_filename, df)
