def apply_on_column_logic(df, some_col: str, if_logic_eval: str, if_true_eval: str, if_false_eval: str, result: str):
    """
    Evaluates a custom python statement using a single column and calculates the result.
    Statements for all three: if condition, if true, if false.
    Note: Please prefer regular snippets to custom evaluate statements and use apply as the last option.
    :param some_col: Column to calculate
    :param if_logic_eval: A logical statement that generates True or False. E.g. x > 0
    :param if_true_eval: A column name or calculation for True. E.g. x / 2 + 10
    :param if_false_eval: A column name or calculation for True. E.g. x * 2 - 10
    :param result: Resulting column name
    """
    expression = f"df['{some_col}'].apply(lambda x: {if_true_eval} if {if_logic_eval} else {if_false_eval})"
    df[result] = eval(expression, {'df': df, '__builtins__': {}})

    return df
