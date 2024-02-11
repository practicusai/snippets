def hypot(df, some_col1: str, some_col2: str, result):
    """
    Calculates the hypotenuse of right triangles given the lengths of their legs.
    :param  some_col1: The name of the column containing the first leg lengths.
    :param some_col2: The name of the column containing the second leg lengths.
    :param result: Resulting column name
    """

    import numpy as np

    df[result] = np.hypot(df[some_col1], df[some_col2])
    return df

