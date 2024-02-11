def random_between(df, bottom: int, top: int, result: str):
    """
    Generates random integers between specified bottom and top values in a new column.
    :param bottom: The smallest integer to generate (inclusive).
    :param top: The largest integer to generate (inclusive).
    :param result: Resulting column name
    """
    import numpy as np
    df[result] = np.random.randint(bottom, top + 1, len(df))

    return df
