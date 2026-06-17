import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def missing_value_summary(df):
    """
    Return missing value counts and percentages.
    """
    summary = pd.DataFrame({
        "Missing Count": df.isnull().sum(),
        "Missing %": round(df.isnull().mean() * 100, 2)
    })

    return summary.sort_values(
        by="Missing Count",
        ascending=False
    )


def plot_distribution(df, column, bins=30):
    """
    Plot histogram and KDE.
    """
    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=df,
        x=column,
        bins=bins,
        kde=True
    )

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def plot_boxplot(df, column):
    """
    Plot boxplot for outlier detection.
    """
    plt.figure(figsize=(8, 4))

    sns.boxplot(
        x=df[column]
    )

    plt.title(f"Boxplot of {column}")
    plt.tight_layout()
    plt.show()


def calculate_loss_ratio(df):
    """
    Calculate loss ratio.
    """
    return df["TotalClaims"] / df["TotalPremium"]


def calculate_margin(df):
    """
    Calculate underwriting margin.
    """
    return df["TotalPremium"] - df["TotalClaims"]


def plot_scatter(df, x, y):
    """
    Create scatter plot between two variables.
    """
    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x=x,
        y=y,
        alpha=0.6
    )

    plt.title(f"{x} vs {y}")
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df, columns):
    """
    Plot correlation matrix heatmap.
    """
    corr = df[columns].corr()

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()


def plot_bar(data, column, title):
    """
    Plot bar chart.
    """
    plt.figure(figsize=(10, 5))

    data[column].plot(
        kind="bar"
    )

    plt.title(title)
    plt.tight_layout()
    plt.show()
