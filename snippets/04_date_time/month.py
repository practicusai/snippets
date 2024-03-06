def month(df, datetime_col: str, result: str):
    """
    Returns the month of the selected date column
    :param datetime_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[datetime_col].dt.month

    return df
