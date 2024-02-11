def day_of_week(df, some_col: str, result: str):
    """
    Returns the day of the week of a date column
    Monday=0, Sunday=6
    :param some_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[some_col].dt.dayofweek

    return df
