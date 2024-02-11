def less_than(df, first_col: str, second_col: str, result: str = ""):
    """
    Compares two columns and returns True if first one is less than the second
    :param first_col: First column to compare
    :param second_col: Second column to compare
    :param result: Resulting column name
    """
    df[result] = df[first_col] < df[second_col]

    return df
