import argparse
from pathlib import Path
import os
from life_expectancy.data_preprocessing.data_cleaning import (
    process_data_file,
)
from .region import Region
from life_expectancy.data_preprocessing.data_loading import (
    JSONDataLoader,
    TSVDataLoader,
)


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Clean life expectancy data")
    parser.add_argument(
        "--country",
        type=str,
        default=os.environ.get("country", "PT"),
        help="Specify the country code to filter by (default: PT).",
    )
    parser.add_argument(
        "--source_filename",
        type=str,
        default=os.environ.get("source_filename", "data_file.tsv"),
        help="Specify raw data file.",
    )
    return parser.parse_args()


def run():
    """Main execution logic."""
    try:
        args = parse_arguments()

        # Validate arguments
        if not args.country:
            raise ValueError("Country must be specified.")
        if not args.source_filename:
            raise ValueError("Source filename must be specified.")

        # Resolve file paths
        input_data_dir = Path(__file__).resolve().parent / "data"
        output_data_dir = Path(__file__).resolve().parent / "data"
        input_file = args.source_filename

        # Determine loader strategy based on file extension
        file_extension = Path(input_file).suffix.lower()
        if file_extension == ".tsv":
            loader_strategy = TSVDataLoader(sep="\t")
        elif file_extension == ".json":
            loader_strategy = JSONDataLoader()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}.")

        # Ensure valid country
        country = Region.get(args.country)  # Validate against Region enum

        # Process data
        process_data_file(
            input_dir=input_data_dir,
            output_dir=output_data_dir,
            loader_strategy=loader_strategy,
            filename=input_file,
            country=country,
        )

    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)


if __name__ == "__main__":
    run()
