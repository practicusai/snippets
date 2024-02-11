def degrees(df, some_col: str, result: str):
    """
    Converts radians into degrees.    
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.degrees(df[some_col])

    return df
