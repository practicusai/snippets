def day_of_year(df, some_col: str, result: str):
    """
    Returns the ordinal day of the year
    :param some_col: A date column
    :param result: Resulting column name
    """

    df[result] = df[some_col].dt.dayofyear

    return df
