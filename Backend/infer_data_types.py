import pandas as pd

def infer_and_convert_data_types(df):
    for col in df.columns:
        # Attempt to convert to numeric first
        df_converted = pd.to_numeric(df[col], errors='coerce')
        if not df_converted.isna().all():  # If at least one value is numeric
            # Downcast numeric types if possible, prioritizing integers
            df[col] = pd.to_numeric(df_converted, downcast='integer')
            if df[col].dtype == 'float64':  # If still float, try downcasting to float32
                df[col] = pd.to_numeric(df_converted, downcast='float')
            continue

        # Attempt to convert to datetime
        try:
            df[col] = pd.to_datetime(df[col])
            continue
        except (ValueError, TypeError):
            pass

        if set(df[col].dropna().unique()).issubset({True, False, 1, 0, 'True', 'False', '1', '0'}):
            df[col] = df[col].astype('bool')
            continue
        try:
            df[col] = df[col].apply(complex)
            continue
        except ValueError:
            pass  # Not a complex number column
        # Check if the column should be categorical
        if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
            df[col] = pd.Categorical(df[col])

    return df

# Test the function with your DataFrame
df = pd.read_csv('data_files/sample_data.csv')
print("Data types before inference:")
print(df.dtypes)

df = infer_and_convert_data_types(df)

print("\nData types after inference:")
print(df.dtypes)
