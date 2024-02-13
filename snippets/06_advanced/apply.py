def apply(df, eval_statement: str, result: str):
    """
    Evaluates a custom python statement on ALL columns and calculates the result.
    Note: Please prefer regular snippets to custom evaluate statements and use apply as the last option.
    :param eval_statement: Statement using row['col_name'], E.g. row['col_1'] + row['col_2'] / 2
    :param result: Resulting column name
    """

    expression = f"df.apply(lambda row: {eval_statement}, axis=1)"
    df[result] = eval(expression, {'df': df, '__builtins__': {}})

    return df


apply.supported_engines = ['pandas']
