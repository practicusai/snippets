def apply_on_column(df, some_col: str, eval_statement: str, result: str):
    """
    Evaluates a custom python statement using a single column and calculates the result.
    Note: Please prefer regular snippets to custom evaluate statements and use apply as the last option.
    :param some_col: Column to calculate
    :param eval_statement: Statement using 'x', where x is the row value. E.g. x/2 + 10
    :param result: Resulting column name
    """
    expression = f"df['{some_col}'].apply(lambda x: {eval_statement})"
    safe_locals = {'x': None}
    df[result] = eval(expression, {'df': df, '__builtins__': {}}, safe_locals)

    return df
