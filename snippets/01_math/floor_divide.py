def floor_divide(df, numerator_col: str, denominator_col: str, result: str):
    """
    Calculates the integer quotient of values in two columns, rounding down to the nearest integer.
    This function performs the floor division operation, which divides the values in the numerator column by the values in the denominator column, and then rounds down to the nearest integer.
    :param numerator_col: Name of the column containing the numerator values. Must be an integer type column.
    :param denominator_col: Name of the column containing the denominator values. Must be an integer type column.
    :param result: Name of the resulting column where the quotient values will be stored.
    """
    import numpy as np
    
    df[result] = np.floor_divide(df[numerator_col], df[denominator_col])

    return df
