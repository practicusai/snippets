def cos(df, numeric_col: str, result: str):
    """
    Calculates the cosine of the values in a specified column,and adds the result as a new column to the DataFrame.    
    :param numeric_col: Name of the column whose values are to be used for cosine calculation.
    :param result: Name of the resulting column where the cosine values will be stored.
    """
    import numpy as np
    df[result] = np.cos(df[numeric_col])

    return df
