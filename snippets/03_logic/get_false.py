def get_false(df, result: str):
    """
    Returns False. Usually combined with other snippets.
    :param result: Resulting column name
    """
    df[result] = False

    return df
