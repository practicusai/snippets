def minute(df, some_col: str, result: str):
    """
    Returns the minute of the selected date column
    :param some_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_col].dt.minute

    return df
