def sqrtpi(df, some_numeric_col: str, result: str):
    """
    Computes the square root of (number * pi) for each value in a column.
    The sqrtpi function calculates the square root of the product of the value in the specified column and the mathematical constant pi (π).
    :param some_numeric_col: The name of the column containing the values to calculate the square root of (number * pi).
    :param result: The name of the column where the resulting square root values will be stored.
    """
    import numpy as np

    df[result] = np.sqrt(np.pi) * df[some_numeric_col]

    return df
