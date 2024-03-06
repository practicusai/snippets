def year(df, datetime_col: str, result: str):
    """
    Returns the year of the selected date column
    :param datetime_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[datetime_col].dt.year

    return df
