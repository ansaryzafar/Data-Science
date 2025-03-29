import pandas as pd

def clean_data(filepath):
    # Load the data
    data = pd.read_csv(filepath)

    # Remove duplicates
    data = data.drop_duplicates()

    # Handle missing values (example: fill with mean)
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        data[column] = data[column].fillna(data[column].mean())

    # Remove rows with extreme outliers (based on z-score threshold)
    from scipy.stats import zscore
    data = data[(zscore(data.select_dtypes(include=['float64', 'int64'])) < 3).all(axis=1)]

    print("Data cleaned successfully!")
    return data


# cleaned_data = clean_data('data/raw_dataset.csv')