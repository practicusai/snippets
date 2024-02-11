def conditional_eval(df, if_logic_eval: str, if_true_eval: str, if_false_eval: str, result: str):
    """
    Evaluates custom statements for all three: if condition, if true, if false
    Note: Please prefer regular snippets to custom evaluate statements and use eval as a last resort.
    :param if_logic_eval: A logical statement that generates True or False. E.g. col1 > 0
    :param if_true_eval: A column name or calculation for True. E.g. col2 + col3
    :param if_false_eval: A column name or calculation for True. E.g. (col3 + 10) / 5
    :param result: Resulting column name
    """
    import numpy as np

    df[result] = np.where(df.eval(if_logic_eval), df.eval(if_true_eval), df.eval(if_false_eval))

    return df


conditional_eval.supported_engines = ['pandas']
