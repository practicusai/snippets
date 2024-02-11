def get_none(df, result: str):
    """
    Returns None. Usually combined with other snippets.
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.nan

    return df
