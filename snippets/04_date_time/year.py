def year(df, some_col: str, result: str):
    """
    Returns the year of the selected date column
    :param some_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_col].dt.year

    return df
