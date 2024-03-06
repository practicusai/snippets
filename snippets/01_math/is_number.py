def is_number(df, some_numeric_col: str, result: str):
    """
    Returns True if all values in a column are numbers, False otherwise.
    :param some_numeric_col: Name of the column to check. Must be a numeric type column.
    :param result: Name of the resulting column where the boolean value indicating whether all values are numbers will be stored.
    """

    import numpy as np

    df[result] = df[some_numeric_col].apply(lambda x: np.isreal(x)).all()

    return df
