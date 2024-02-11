def greater_than_or_equal(df, first_col: str, second_col: str, result: str = ""):
    """
    Compares two columns and returns True if first one is greater than ofr equal to the second
    :param first_col: First column to compare
    :param second_col: Second column to compare
    :param result: Resulting column name
    """
    df[result] = df[first_col] >= df[second_col]

    return df
