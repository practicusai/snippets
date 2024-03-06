def day_name(df, datetime_col: str, result: str):
    """
    Returns the day name of the selected date column
    :param datetime_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[datetime_col].dt.day_name()

    return df
