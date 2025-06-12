import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Set your folder path
folder_path = r"C:\Users\kiran\Downloads\ecommerce"

# Step 2: Read and combine all CSV files
all_data = []

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        print("Reading:", file)
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path, low_memory=False)  # Avoid dtype warning
        all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)

# Step 3: Clean column names
combined_df.columns = [col.strip().lower().replace(" ", "_") for col in combined_df.columns]

# Step 4: Remove duplicated columns (important before datetime conversion)
combined_df = combined_df.loc[:, ~combined_df.columns.duplicated()]

# Step 5: Convert 'date' column to datetime
if 'date' in combined_df.columns:
    combined_df['date'] = pd.to_datetime(combined_df['date'], errors='coerce')

# Step 6: Fill missing values smartly
numeric_cols = combined_df.select_dtypes(include=['float64', 'int64']).columns
combined_df[numeric_cols] = combined_df[numeric_cols].fillna(0)

object_cols = combined_df.select_dtypes(include=['object']).columns
combined_df[object_cols] = combined_df[object_cols].fillna('')

# Step 7: Drop duplicates
combined_df.drop_duplicates(inplace=True)

# Optional Step 8: Encode categorical columns (if present)
categorical_cols = ['status', 'fulfilment', 'sales_channel']
le = LabelEncoder()

for col in categorical_cols:
    if col in combined_df.columns:
        combined_df[col] = le.fit_transform(combined_df[col].astype(str))

# Optional Step 9: Scale numerical columns (if needed)
scaler = StandardScaler()
numeric_to_scale = ['qty', 'amount']  # Replace with your relevant numeric columns

for col in numeric_to_scale:
    if col in combined_df.columns:
        combined_df[col] = scaler.fit_transform(combined_df[[col]])

# Step 10: Save final cleaned dataset
combined_df.to_csv("cleaned_ecommerce_data.csv", index=False)
print("✅ Cleaned dataset saved to 'cleaned_ecommerce_data.csv'")
