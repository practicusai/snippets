def to_numeric(df, some_col: str, result: str):
    """
    This function converts the values in a specified column to numeric type. If a value cannot be converted to a numeric type, it will be replaced with NaN (Not a Number).
    :param some_col: The name of the column containing the values to convert.
    :param result: Resulting column name to store the converted values.
    """
    import pandas as pd

    df[result] = pd.to_numeric(df[some_col], errors='coerce')

    return df
