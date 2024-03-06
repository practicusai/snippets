def factorial(df, integer_col: str, result: str):
    """
    Calculates the factorial of each value in a specified column, and adds the result as a new column to the DataFrame.
    The factorial of a number is calculated as the product of all positive integers less than or equal to that number.

    :param integer_col: Name of the column whose values are used for factorial calculation.
    :param result: Name of the resulting column where the factorial values will be stored.
    """
    from scipy.special import factorial as scipy_factorial
    df[result] = df[integer_col].apply(scipy_factorial)

    return df

