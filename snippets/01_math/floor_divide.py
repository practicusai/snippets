def floor_divide(df, numerator_col: str, denominator_col: str, result: str):
    """
    Calculates the integer quotient of values in two columns.
    :param numerator_col: The name of the column containing the numerator values.
    :param denominator_col: The name of the column containing the denominator values.
    :param result: Resulting column name
    """
    import numpy as np
    
    df[result] = np.floor_divide(df[numerator_col], df[denominator_col])

    return df
