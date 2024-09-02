from pathlib import Path
import pandas as pd


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
    # Construct the full output file path
    output_path = target_dir / base_filename
    df.to_csv(output_path, index=False)


def split_and_clean_columns(
    df: pd.DataFrame, column: str, new_columns: list, delimiter: str = ","
) -> pd.DataFrame:
    """
    Splits a specified column into multiple columns and cleans column names.
    args:
        df: DataFrame to modify.
        column: Name of the column to split.
        new_columns: List of new column names after splitting.
        delimiter: Delimiter used for splitting (default is ',').
    returns:
        Modified DataFrame with new columns and cleaned names.
    """
    # Split the column
    df[new_columns] = df[column].str.split(delimiter, expand=True)
    df.drop(columns=[column], inplace=True)

    # Clean column names
    df.columns = df.columns.str.strip()
    return df


def clean_and_unpivot_data(
    df: pd.DataFrame, id_vars: list, value_var: str, column_types: dict
) -> pd.DataFrame:
    """
    Cleans the data by enforcing types and converting to long format.
    args:
        df: DataFrame to modify.
        id_vars: List of columns to keep as identifier variables.
        value_var: Name of the new value column.
        column_types: Dictionary specifying the desired data types for columns.
    returns:
        Cleaned and unpivoted DataFrame.
    """
    # Unpivot the dataframe
    df = df.melt(id_vars=id_vars, var_name="year", value_name=value_var)

    # Enforce data types
    for column, dtype in column_types.items():
        if dtype == "float":
            df[column] = df[column].str.extract(r"(\d+\.\d+)").astype(float)
        else:
            df[column] = df[column].astype(dtype)
    df.dropna(inplace=True)

    return df


def clean_data(
    input_dir: Path, output_dir: Path, filename: str, sep: str, country: str
) -> pd.DataFrame:
    """
    Loads, cleans, and saves the data.
    args:
        input_dir: Path to the input data directory.
        output_dir: Path to the output data directory.
        filename: Name of the file with extension.
        sep: The separator used in the file (e.g., ',' for CSV).
        country: Two-letter country code in caps.
    returns:
        Cleaned DataFrame.
    """
    # Load the data
    df = load_data(input_dir, filename, sep)

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

    # Filter dataframe by the specified country directly
    df = df[df["region"] == country]

    # Prepare output filename
    base_filename = f"{country.lower()}_life_expectancy.csv"

    # Save cleaned data to the output directory
    save_data(output_dir, base_filename, df)

    return df
