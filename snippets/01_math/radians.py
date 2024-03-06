def radians(df, degrees_col: str, result: str):
    """
    Converts angles from degrees to radians in a column.
    :param degrees_col: Name of the column containing the angles in degrees.
    :param result: Name of the resulting column where the converted angles in radians will be stored.
    """

    import numpy as np

    if degrees_col not in df.columns:
        raise ValueError(f"Column '{degrees_col}' does not exist in the DataFrame.")

    df[result] = np.radians(df[degrees_col])

    return df
