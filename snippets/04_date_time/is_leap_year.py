def is_leap_year(df, some_col: str, result: str):
    """
    Returns true if the selected date column is a leap year
    :param some_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_col].dt.is_leap_year

    return df
