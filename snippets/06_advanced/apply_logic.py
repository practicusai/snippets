def apply_logic(df, if_logic_eval: str, if_true_eval: str, if_false_eval: str, result: str):
    """
    Evaluates a custom python statement on ALL columns and calculates the result.
    Statements for all three: if condition, if true, if false and uses row['column_name'] format
    Note: Please prefer regular snippets to custom evaluate statements and use apply as the last option.
    :param if_logic_eval: A logical statement that generates True or False. E.g. row['col_1'] > row['col_2']
    :param if_true_eval: A column name or calculation for True. E.g. row['col_1'] + 10
    :param if_false_eval: A column name or calculation for True. E.g. row['col_2'] * 5
    :param result: Resulting column name
    """

    expression = f"df.apply(lambda row: {if_true_eval} if {if_logic_eval} else {if_false_eval}, axis=1)"
    df[result] = eval(expression, {'df': df, '__builtins__': {}})

    return df


apply_logic.supported_engines = ['pandas']
