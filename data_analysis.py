import pandas as pd

def read_data(file_path):
    """Reads data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data successfully loaded!")
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: Could not parse the file. Ensure it's a valid CSV.")
        return None

def clean_data(data):
    """Cleans the data by handling missing values and duplicates."""
    if data is None:
        return None
    
    print("Cleaning data...")
    data.drop_duplicates(inplace=True)  # Remove duplicate rows
    data.fillna(data.mean(numeric_only=True), inplace=True)  # Fill missing values with column means

    return data

def analyze_data(data):
    """Performs basic analysis on the data."""
    if data is None:
        return

    print("\nData Summary:")
    print(data.describe())  # Display basic statistics
    print("\nColumn Data Types:")
    print(data.dtypes)

def save_cleaned_data(data, output_file="cleaned_data.csv"):
    """Saves the cleaned data to a new CSV file."""
    if data is not None:
        data.to_csv(output_file, index=False)
        print(f"Cleaned data saved as {output_file}")

def main():
    file_path = input("Enter the path to your CSV file: ")
    data = read_data(file_path)

    if data is not None:
        data = clean_data(data)
        analyze_data(data)
        save_cleaned_data(data)

if __name__ == "__main__":
    main()
