import pandas as pd

class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def show_summary(self):
        print("Data Summary:")
        print(self.df.describe())
        print("\nInformation:")
        print(self.df.info())

    def get_column_stats(self, column_name):
    
        if column_name in self.df.columns:
            print(f"\nStatistics for column: {column_name}")
            print(self.df[column_name].describe())
        else:
            print("Column not found.")

    def impute_missing_values(self, column_name, strategy='mean'):
        
        if column_name not in self.df.columns:
            print("Column not found.")
            return

        if strategy == 'mean':
            value = self.df[column_name].mean()
        elif strategy == 'median':
            value = self.df[column_name].median()
        else:
            print("Invalid strategy. Use 'mean' or 'median'.")
            return

        self.df[column_name].fillna(value, inplace=True)
        print(f"Missing values in '{column_name}' filled using {strategy}.")


data = {
    'Age': [25, 30, None, 22, 28],
    'Salary': [50000, 60000, 55000, None, 58000]
}

df = pd.DataFrame(data)

# Create object
analyzer = DataAnalyzer(df)

# Call methods
analyzer.show_summary()
analyzer.get_column_stats('Age')
analyzer.impute_missing_values('Salary', 'mean')

# Show updated DataFrame
print("\nUpdated DataFrame:")
print(df)
