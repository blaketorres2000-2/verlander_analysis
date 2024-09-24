import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

def load_data(file_2019, file_2022):
    """
    Load datasets from CSV files.

    Args:
        file_2019 (str): Path to the 2019 data CSV file.
        file_2022 (str): Path to the 2022 data CSV file.

    Returns:
        tuple: DataFrames for 2019 and 2022 data.
    """
    data_2019 = pd.read_csv(file_2019)
    data_2022 = pd.read_csv(file_2022)
    return data_2019, data_2022

def perform_chi2_test(data):
    """
    Perform Chi-Square test of independence on the dataset.

    Args:
        data (DataFrame): DataFrame containing the dataset.

    Returns:
        tuple: Chi2 statistic, p-value, degrees of freedom, expected frequencies, and contingency table.
    """
    contingency = pd.crosstab(data['pitch_type'], data['count'])
    chi2, p, dof, expected = stats.chi2_contingency(contingency)
    return chi2, p, dof, expected, contingency

def print_chi2_results(chi2, p, season):
    """
    Print the Chi-Square test results for a given season.

    Args:
        chi2 (float): Chi-Square statistic.
        p (float): p-value.
        season (str): The season (e.g., '2019', '2022').
    """
    print(f"{season} Chi-Square Test: Chi2 = {chi2:.2f}, p-value = {p:.4f}")

def analyze_independence(p, season):
    """
    Analyze and print whether pitch_type is independent of count.

    Args:
        p (float): p-value from the Chi-Square test.
        season (str): The season (e.g., '2019', '2022').
    """
    if p < 0.05:
        print(f"In {season}, pitch_type is dependent on count (reject null hypothesis).")
    else:
        print(f"In {season}, pitch_type is independent of count (fail to reject null hypothesis).")

def calculate_residuals(contingency, expected):
    """
    Calculate residuals from the contingency table and expected frequencies.

    Args:
        contingency (DataFrame): Contingency table of observed frequencies.
        expected (DataFrame): Expected frequencies from Chi-Square test.

    Returns:
        DataFrame: Residuals rounded to one decimal place.
    """
    residuals = contingency - expected
    return residuals.round(1)

def print_residuals(residuals, season):
    """
    Print the Chi-Square residuals.

    Args:
        residuals (DataFrame): Residuals from the Chi-Square test.
        season (str): The season (e.g., '2019', '2022').
    """
    print(f"\n{season} - Chi-square residuals:")
    print(residuals)

def most_likely_pitch(contingency_table, data):
    """
    Determine the most likely pitch type and its expected speed for each count.

    Args:
        contingency_table (DataFrame): Contingency table of observed frequencies.
        data (DataFrame): DataFrame containing the dataset.

    Returns:
        dict: Most likely pitch type and average speed for each count.
    """
    most_likely = {}
    for count in contingency_table.columns:
        subset = data[data['count'] == count]
        avg_speeds = subset.groupby('pitch_type')['release_speed'].mean()
        most_likely_pitch_type = avg_speeds.idxmax()
        avg_speed = avg_speeds.max()
        most_likely[count] = (most_likely_pitch_type, avg_speed)
    return most_likely

def print_most_likely_pitch(most_likely, season):
    """
    Print the most likely pitch type and expected speed for each count.

    Args:
        most_likely (dict): Most likely pitch type and average speed for each count.
        season (str): The season (e.g., '2019', '2022').
    """
    print(f"\nMost likely pitch type and expected speed for each count in {season}:")
    for count, (pitch_type, speed) in most_likely.items():
        print(f"Count {count}: Pitch Type = {pitch_type}, Expected Speed = {speed:.1f} MPH")

def plot_pitch_distribution(data, season):
    """
    Plot the distribution of pitch types for each count.

    Args:
        data (DataFrame): DataFrame containing the dataset.
        season (str): The season (e.g., '2019', '2022').
    """
    contingency = pd.crosstab(data['pitch_type'], data['count'])
    contingency.plot(kind='bar', figsize=(12, 8))
    plt.title(f'Pitch Type Distribution by Count in {season}')
    plt.xlabel('Pitch Type')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.legend(title='Count')
    plt.tight_layout()
    plt.show()

def main():
    # Load datasets
    data_2019, data_2022 = load_data('verlander_2019.csv', 'verlander_2022.csv')

    # Perform Chi-Square tests
    chi2_2019, p_2019, dof_2019, expected_2019, contingency_2019 = perform_chi2_test(data_2019)
    chi2_2022, p_2022, dof_2022, expected_2022, contingency_2022 = perform_chi2_test(data_2022)

    # Print Chi-Square test results
    print_chi2_results(chi2_2019, p_2019, '2019')
    print_chi2_results(chi2_2022, p_2022, '2022')

    # Analyze and print independence
    analyze_independence(p_2019, '2019')
    analyze_independence(p_2022, '2022')

    # Calculate and print residuals
    residuals_2019 = calculate_residuals(contingency_2019, expected_2019)
    residuals_2022 = calculate_residuals(contingency_2022, expected_2022)
    print_residuals(residuals_2019, '2019')
    print_residuals(residuals_2022, '2022')

    # Analyze and print most likely pitch types
    most_likely_pitch_2019 = most_likely_pitch(contingency_2019, data_2019)
    most_likely_pitch_2022 = most_likely_pitch(contingency_2022, data_2022)
    print_most_likely_pitch(most_likely_pitch_2019, '2019')
    print_most_likely_pitch(most_likely_pitch_2022, '2022')

    # Plot pitch distribution for 2019 and 2022
    plot_pitch_distribution(data_2019, '2019')
    plot_pitch_distribution(data_2022, '2022')

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
