"""Tests for the cleaning module"""

import pandas as pd

from life_expectancy.__main__ import clean_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run `clean_data` and compare the output to the expected output"""
    clean_data(country="PT")
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
