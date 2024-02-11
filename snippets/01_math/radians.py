def radians(df, degrees_col: str, result: str):
    """
    Converts angles from degrees to radians in a column.
    :param degrees_col: The name of the column containing the angles in degrees.
    :param result: Resulting column name
    """
    
    import numpy as np
    df[result] = np.radians(df[degrees_col])

    return df
