def power(df, some_numeric_col: str, power_num: int, result: str):
    """
    Raises values in a column to a specified power.
    :param some_numeric_col: Name of the column containing the values to raise to a power.
    :param power_num: The exponent to which the values will be raised.
    :param result: Name of the resulting column where the powered values will be stored.
    """

    if not isinstance(power_num, int):
        raise ValueError("Exponent must be an integer.")


    df[result] = df[some_numeric_col] ** power_num

    return df
