# Sample snippet code utilizing several features.
# For simpler requirements, you can only add a function like the below my_snippet() and delete the rest of the code


# You can define helper functions and call from your snippet.
def some_helper_function(a_number: float):
    return a_number + 123


# String enums are displayed in a drop-down list int the UI for a better user experience
from enum import Enum
class UserOptions(str, Enum):
    OPTION_1 = "My first option"
    OPTION_2 = "My second option"


def my_snippet(df, some_col: str, some_number: float, optional_number: float | None, some_option: UserOptions, result: str):
    """
    Rename your snippet, and describe what it does here.
    You do not need to document the first param (df), and the function return values since they are always a DataFrame.
    :param some_col: Choose a column
    :param some_number: Enter a number
    :param optional_number: Another number
    :param some_option: Please select
    :param result: Result column name
    """

    if some_option == UserOptions.OPTION_1:
        some_number = some_helper_function(some_number)

    import numpy as np
    df[result] = np.add(df[some_col], some_number)

    return df

# ** Parameter Types **
# Please explicitly define snippet function parameters with the below data types:
#   str, int, float, bool, date, datetime, object and String Enums
#   E.g., my_param: str
# Please do not use mixed types, e.g. my_param: int | float  instead, use e.g. my_param: object
# Function parameters can be optional, e.g. my_param: str | None
# If you would like the user to choose a column in the UI for a better UX, end your parameter names with '_col'
#   E.g. my_col: str
# Your parameters can be a list of values, or list of columns, the UI will behave accordingly.
#   E.g. my_param: list[str]  or  my_col: list[str]
# List params can be declared optional too, e.g. my_col: list[str] | None

# ** Advanced Functionality **
# In order to use advanced functionality, make sure your code runs on Worker by uncommenting the below
# my_snippet.worker_required = True


def test_snippet(df):
    # You can optionally add some test code here.
    # Only use use test_snippet() function name for the UI tests to work.
    # Please note that the snippet function (e.g. my_snippet) must be the last function defined, except test_snippet()

    df = my_snippet(
        df=df,
        some_col="CRIM",
        some_number=10,
        optional_number=None,
        some_option=UserOptions.OPTION_2,  # you can use the string value of the enum too
        result="result",
    )
    return df


# Uncomment the below to test the snippet from another editor
# if __name__ == '__main__':
#     import pandas as pd
#     _df = pd.read_csv("boston.csv")
#     _df = test_snippet(_df)
#     print(_df.head())
