from src.data_processing import process_data

if __name__ == "__main__":
    df = process_data()
    print(df.head())

