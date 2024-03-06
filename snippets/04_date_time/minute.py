def minute(df, datetime_col: str, result: str):
    """
    Returns the minute of the selected date column
    :param datetime_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[datetime_col].dt.minute

    return df
