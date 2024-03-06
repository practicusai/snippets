def round_value(df, some_col: str, decimals: int, result: str):
    """
    Rounds values in a column to the specified number of decimal places.
    :param some_col: The name of the column to round.
    :param decimals: The number of decimal places to round to. Must be an integer.
    :param result: Name of the resulting column where the rounded values will be stored.
    """
    if not isinstance(decimals, int):
        raise ValueError("Decimals must be an integer.")

    df[result] = df[some_col].round(decimals)

    return df

