def day(df, some_col: str, result: str):
    """
    Returns the day of the selected date column
    :param some_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[some_col].dt.day

    return df
