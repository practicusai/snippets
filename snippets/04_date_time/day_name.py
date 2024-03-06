def day_name(df, some_date_col: str, result: str):
    """
    Returns the day name of the selected date column
    :param some_date_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[some_date_col].dt.day_name()

    return df
