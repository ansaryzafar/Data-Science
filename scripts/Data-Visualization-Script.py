import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    # Histogram of numeric columns
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        sns.histplot(data[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.savefig(f'images/{column}_distribution.png')

    # Heatmap of correlations
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.savefig('images/correlation_heatmap.png')

    print("Visualizations saved successfully!")


# visualize_data(processed_data)