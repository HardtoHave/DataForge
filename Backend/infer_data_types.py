import pandas as pd


def infer_and_convert_data_types(df):
    """
    Infer and convert datas type in a Pandas DataFrame
    :param df:input dataframe to process
    :return:pandas.dataframe: the dataframe with data types coverted
    """
    for col in df.columns:
        # Attempt to convert to numeric first
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        except(ValueError, TypeError):
            pass

        # Attempt to convert to datetime
        try:
            df[col] = pd.to_datetime(df[col], infer_datetime_format=True, errors='coerce')
            continue
        except (ValueError, TypeError):
            pass

        # Check if the column should be categorical
        if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
            df[col] = pd.Categorical(df[col])
            continue

        # Handle mixed-type columns


    return df


# Test the function with your DataFrame
df = pd.read_csv('sample_data.csv')
print("Data types before inference:")
print(df.dtypes)

df = infer_and_convert_data_types(df)

print("\nData types after inference:")
print(df.dtypes)

# %%
