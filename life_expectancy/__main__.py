import argparse
from pathlib import Path

from life_expectancy.data_preprocessing.data_preprocessing import (
    process_data_file,
)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean life expectancy data")
    parser.add_argument(
        "--country",
        type=str,
        default="PT",
        help="Specify the country code to filter by (default: PT).",
    )

    args = parser.parse_args()
    input_data_dir = Path(__file__).resolve().parent / "data"
    output_data_dir = Path(__file__).resolve().parent / "data"
    input_file = "eu_life_expectancy_raw.tsv"

    process_data_file(
        input_dir=input_data_dir,
        output_dir=output_data_dir,
        filename=input_file,
        sep="\t",
        country=None,
    )
