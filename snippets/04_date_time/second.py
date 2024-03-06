def second(df, datetime_col: str, result: str):
    """
    Returns the second of the selected date column
    :param datetime_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[datetime_col].dt.second

    return df
