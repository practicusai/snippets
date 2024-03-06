def greater_than_or_equal(df, first_numeric_col: str, second_numeric_col: str, result: str = ""):
    """
    Compares two columns and returns True if first one is greater than ofr equal to the second
    :param first_numeric_col: First column to compare
    :param second_numeric_col: Second column to compare
    :param result: Resulting column name
    """
    df[result] = df[first_numeric_col] >= df[second_numeric_col]

    return df
