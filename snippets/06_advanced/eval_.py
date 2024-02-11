def eval_(df, eval_statement: str, result: str):
    """
    Evaluates a custom statement and calculates the result.
    Note: Please prefer regular snippets to custom evaluate statements and use eval as a last resort.
    :param eval_statement: Statement E.g. col1 + col2 * 10
    :param result: Resulting column name
    """
    df[result] = df.eval(eval_statement)

    return df


eval_.supported_engines = ['pandas']
