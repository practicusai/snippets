from enum import Enum


class CorrMethods(str, Enum):
    pearson = "pearson"
    kendall = "kendall"
    spearman = "spearman"


def corr(df, some_numeric_col: list[str], corr_method: CorrMethods = CorrMethods.pearson):
    """
    Calculates the correlation of selected columns for each row separately.
    :param some_numeric_col: Columns with numeric values
    :param corr_method: Correlation method to use
    """
    df = df[some_numeric_col].corr(method=str(corr_method)).reset_index()

    return df
