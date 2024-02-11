def is_number(df, some_col: str, result: str):
    """
    Returns True if all values in a column are numbers, False otherwise.
    :param some_col: Column to check
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = df[some_col].apply(lambda x: np.isreal(x)).all()

    return df
