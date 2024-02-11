def to_numeric(df, some_col: str, result: str):
    """
    Convert to a numeric type.
    :param some_col: Column the calculate
    :param result: Resulting column name
    """
    import pandas as pd

    df[result] = pd.to_numeric(df[some_col], errors='coerce')

    return df
