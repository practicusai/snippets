def is_leap_year(df, datetime_col: str, result: str):
    """
    Returns true if the selected date column is a leap year
    :param datetime_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[datetime_col].dt.is_leap_year

    return df
