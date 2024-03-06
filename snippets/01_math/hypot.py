def hypot(df, first_numeric_col: str, second_numeric_col: str, result):
    """
    Calculates the hypotenuse of right triangles given the lengths of their legs.
    :param first_numeric_col: Name of the column containing the lengths of the first legs.
                      Must be a numeric type column.    
    :param second_numeric_col: Name of the column containing the lengths of the second legs.
                      Must be a numeric type column.
    :param result: Name of the resulting column where the hypotenuse values will be stored.
    """

    import numpy as np

    df[result] = np.hypot(df[first_numeric_col], df[second_numeric_col])
    return df

