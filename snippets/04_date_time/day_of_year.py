def day_of_year(df, some_date_col: list[str], result: str):
    """
    Returns the ordinal day of the year
    :param some_date_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[some_date_col].dt.dayofyear

    return df
