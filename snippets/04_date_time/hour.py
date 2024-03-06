def hour(df, datetime_col: str, result: str):
    """
    Returns the hour of the selected date column
    :param datetime_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[datetime_col].dt.hour

    return df
