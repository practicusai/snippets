def is_blank(df, some_text_col: str, result: str):
    """
    This function checks whether each value in the specified column of the DataFrame is blank. A value is considered blank if it is NaN (Not a Number) or None.
    :param some_text_col: Name of the column to check for blank values.
    :param result: Name of the resulting column containing boolean values indicating whether each value in the column is blank.
    """
    import pandas as pd
    df[result] = pd.isna(df[some_text_col])

    return df
