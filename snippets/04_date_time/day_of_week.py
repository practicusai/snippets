def day_of_week(df, some_date_col: str, result: str):
    """
    Returns the day of the week of a date column
    Monday=0, Sunday=6
    :param some_date_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[some_date_col].dt.dayofweek

    return df
