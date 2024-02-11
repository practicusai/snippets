def factorial(df, some_col: str, result: str):
    """
    Returns the factorial of a number. The factorial of a number is equal to 1*2*3*...* number.    
    :param some_col: Column to calculate
    :param result: Resulting column name
    """
    from scipy.special import factorial as scipy_factorial
    df[result] = df[some_col].apply(scipy_factorial)

    return df

