"""Tests for the cleaning module"""

import pandas as pd

from life_expectancy.data_preprocessing.data_preprocessing import clean_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run `clean_data` and compare the output to the expected output"""
    print("This is the output path", OUTPUT_DIR)

    clean_data(
        input_dir=OUTPUT_DIR,
        output_dir=OUTPUT_DIR,
        country="PT",
        sep="\t",
        filename="eu_life_expectancy_raw.tsv",
    )
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
