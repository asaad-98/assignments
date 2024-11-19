from pathlib import Path
import pandas as pd
from typing import Optional
from .data_loading import save_data
from .data_loader_strategy import DataLoaderStrategy


def split_and_clean_columns(
    df: pd.DataFrame, column: str, new_columns: list, delimiter: str = ","
) -> pd.DataFrame:
    """Splits a specified column into multiple columns."""
    df[new_columns] = df[column].str.split(delimiter, expand=True)
    df.drop(columns=[column], inplace=True)
    df.columns = df.columns.str.strip()
    return df


def clean_and_unpivot_data(
    df: pd.DataFrame, id_vars: list, value_var: str, column_types: dict
) -> pd.DataFrame:
    """Cleans the data by enforcing types and converting to long format."""
    df = df.melt(id_vars=id_vars, var_name="year", value_name=value_var)

    for column, dtype in column_types.items():
        if dtype == "float":
            df[column] = df[column].str.extract(r"(\d+\.\d+)").astype(float)
        else:
            df[column] = df[column].astype(dtype)
    df.dropna(inplace=True)
    return df


def clean_data(
    df: pd.DataFrame, country: Optional[str] = None
) -> pd.DataFrame:
    """
    Cleans the DataFrame and returns the cleaned data.
    args:
        df: The input DataFrame to clean.
        country: Two-letter country code in caps.
    returns:
        Cleaned DataFrame.
    """
    # Apply cleaning steps
    df = split_and_clean_columns(
        df,
        column="unit,sex,age,geo\\time",
        new_columns=["unit", "sex", "age", "region"],
    )
    df = clean_and_unpivot_data(
        df,
        id_vars=["unit", "sex", "age", "region"],
        value_var="value",
        column_types={"year": "int", "value": "float"},
    )

    if country:
        df = df[df["region"] == country]

    # Reset the index to ensure it starts from 0
    df = df.reset_index(drop=True)

    return df


def process_data_file(
    input_dir: Path,
    output_dir: Path,
    filename: str,
    loader_strategy: DataLoaderStrategy,
    country: Optional[str] = None,
) -> None:
    """
    Loads, cleans, and saves the data.
    args:
        input_dir: Path to the input data directory.
        output_dir: Path to the output data directory.
        filename: Name of the file with extension.
        sep: The separator used in the file (e.g., ',' for CSV).
        country: Two-letter country code in caps.
    """
    # Load the data
    df = loader_strategy.load_data(input_dir, filename)

    # Clean the data
    cleaned_df = clean_data(df, country)

    # Define the output filename
    base_filename = (
        f"{country.lower()}_life_expectancy.csv"
        if country
        else "eu_life_expectancy_expected.csv"
    )

    # Save cleaned data to the output directory
    save_data(output_dir, base_filename, cleaned_df)
