def is_leap_year(df, some_date_col: str, result: str):
    """
    Returns true if the selected date column is a leap year
    :param some_date_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_date_col].dt.is_leap_year

    return df
