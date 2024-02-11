def week_of_year(df, some_col: str, result: str):
    """
    Returns the week of the year of a date column
    :param some_col: A date column
    :param result: Resulting column name
    """
    df[result] = df[some_col].dt.isocalendar().week.astype(int)

    return df
