def round_value(df, some_col: str, decimals: int, result: str):
    """
    Rounds values in a column to the specified number of decimal places.
    :param some_col: The name of the column to round.
    :param decimals: The number of decimal places to round to
    :param result: Resulting column name
    """

    df[result] = df[some_col].round(decimals)

    return df
