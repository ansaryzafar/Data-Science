import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def feature_engineering(data):
    # Scale numeric features
    scaler = StandardScaler()
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

    # Encode categorical features
    encoder = OneHotEncoder(sparse=False)
    categorical_columns = data.select_dtypes(include=['object']).columns
    encoded_cats = pd.DataFrame(encoder.fit_transform(data[categorical_columns]), columns=encoder.get_feature_names_out())
    data = pd.concat([data.drop(categorical_columns, axis=1), encoded_cats], axis=1)

    print("Features engineered successfully!")
    return data


# processed_data = feature_engineering(cleaned_data)