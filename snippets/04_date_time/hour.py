def hour(df, some_col: str, result: str):
    """
    Returns the hour of the selected date column
    :param some_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_col].dt.hour

    return df
