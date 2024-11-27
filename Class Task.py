from scipy.stats import norm
import pandas as pd

def calculate_sample_size_mean(std_dev, margin_of_error, confidence_level=0.95):
    z_score = norm.ppf(1 - (1 - confidence_level) / 2)
    sample_size = (z_score * std_dev / margin_of_error) ** 2
    return round(sample_size)

def calculate_sample_size_proportion(proportion, margin_of_error, confidence_level=0.95):
    z_score = norm.ppf(1 - (1 - confidence_level) / 2)
    sample_size = (z_score ** 2 * proportion * (1 - proportion)) / (margin_of_error ** 2)
    return round(sample_size)

file_path = '/Users/issaxzz/Downloads/population_data.csv'
data = pd.read_csv(file_path)

confidence_level = 0.95
margin_of_error_age = 1
margin_of_error_income = 5000
margin_of_error_proportion = 0.05

std_dev_age = data['age'].std()
std_dev_income = data['income'].std()
proportion_yes = (data['response'] == "Yes").mean()

sample_size_age = calculate_sample_size_mean(std_dev_age, margin_of_error_age, confidence_level)
sample_size_income = calculate_sample_size_mean(std_dev_income, margin_of_error_income, confidence_level)
sample_size_proportion = calculate_sample_size_proportion(proportion_yes, margin_of_error_proportion, confidence_level)

print(f"Sample size to estimate the mean age: {sample_size_age}")
print(f"Sample size to estimate the mean income: {sample_size_income}")
print(f"Sample size to estimate the proportion of 'Yes' responses: {sample_size_proportion}")
