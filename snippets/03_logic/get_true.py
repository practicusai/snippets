def get_true(df, result: str):
    """
    Returns True. Usually combined with other snippets.
    :param result: Resulting column name
    """
    df[result] = True

    return df
