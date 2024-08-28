import argparse
from pathlib import Path

from life_expectancy.data_preprocessing.data_preprocessing import (
    load_data,
    save_data,
)


def clean_data(country: str) -> None:
    """Cleans the data and saves to target
    args:
        country: Two-letter country code in caps.
    """
    data_dir = Path(__file__).resolve().parent / "data"
    input_file = "eu_life_expectancy_raw.tsv"
    output_file = f"{country.lower()}_life_expectancy.csv"

    # Load data
    df = load_data(data_dir=data_dir, filename=input_file, sep="\t")

    # Split columns
    df[["unit", "sex", "age", "region"]] = df[
        "unit,sex,age,geo\\time"
    ].str.split(",", expand=True)
    # Drop
    df.drop(columns=["unit,sex,age,geo\\time"], inplace=True)

    # Strip any trailing spaces in the year columns
    df.columns = df.columns.str.strip()
    # Unpivot the data (convert from wide to long format)
    df_long = df.melt(
        id_vars=["unit", "sex", "age", "region"],
        var_name="year",
        value_name="value",
    )
    del df

    # Enforce data types
    df_long["year"] = df_long["year"].astype(int)

    df_long["value"] = (
        df_long["value"].str.extract(r"(\d+\.\d+)").astype(float)
    )  # remove non numeric
    df_long.dropna(subset="value", inplace=True)

    # Filter
    df_long = df_long.loc[df_long["region"] == country]

    # Save cleaned data
    save_data(data_dir, filename=output_file, df=df_long)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean life expectancy data")
    parser.add_argument(
        "--country",
        type=str,
        default="PT",
        help="Specify the country code to filter by (default: PT).",
    )

    args = parser.parse_args()

    clean_data(args.country)
