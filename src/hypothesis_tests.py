from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind


def chi_square_test(contingency_table):
    """
    Perform Chi-Square test.
    """
    chi2, p_value, dof, expected = chi2_contingency(
        contingency_table
                                                   )

    return {
        "chi2": chi2,
        "p_value": p_value,
        "dof": dof
           }


def independent_ttest(group_a, group_b):
    """
    Perform Welch's t-test.
    """
    stat, p_value = ttest_ind(
        group_a,
        group_b,
        equal_var=False
                             )

    return {
        "t_statistic": stat,
        "p_value": p_value
           }
