def power(df, some_col: str, power_num: int, result: str):
    """
    Raises values in a column to a specified power.
    :param some_col: The name of the column containing the values to raise to a power.
    :param power_num: The exponent to which the values will be raised.
    :param result: Resulting column name
    """

    df[result] = df[some_col] ** power_num

    return df
